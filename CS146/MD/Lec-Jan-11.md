# Lec 2018-01-11 Phil 146: Elementary Meme Design

## Modelling Input
- Infinite sequence of all chars the users will press: $\pi, \delta, \omega, \iota$.
- Accepting input character $\leftrightarrow$ removing a character from $\iota$. 
  <br>

#### Problem
- The sequence may **depend on** the output.
- The users decide what to press **in response to** what is displayed on the screen.
- So, a more realistic model might not assume all input is available at once.
  <br>

#### Alternative
- A request for input yields a functions consuming one or more characters and producing the next program $\pi$, with the input characters substituted for the real request.
- E.g. (define readline (lambda(line) line))
  - If user types "abc", the output is "abc".
- If the entire program is modeled this way, then it reduced to a big nesting of input request functions, one function per prompt; if you supply user input for each prompt, then it yields the final result.
---
## Take input in Racket
#### (read-line): produces a string of all characters pressed until the first `newline`.
- The string you get does not contain that *newline*.
- Little "yellow button" **EOF**: aka I'm done (_me everyday_)

```scheme
(string->list (read-line)) ;; Type "Test" => produces (list #\T #\e #\s #\t)

(define (read-input)
	(define nl (read-line))	;; nl => next line
    (cond
        [(eof-object? nl) empty] ;; if nl == eof, return empty
        [else (cons nl (read-input))])) ;; otherwise, cons nl to next input.

```
```scheme
> (read-input)
hello world ;;type
hello again world ;;type
hello for the third time ;;type
;; press eof
'("hello world", "hello again world", "hello for the third time") ;;output

> (read-input)
;; press eof
'() ;; output an empty list
```
<br>

#### (read-char): extracts one character
###### (peek-char): examines the next character in the sequence, without removing it.

```scheme
(define (my-read-line)
	(define (mrl-h acc)
    	(define ch (read-char))
        (cond
        	[(or (eof-object? ch) (char=? ch #\newline)) (list->string (reverse acc))]
            [else (mrl-h (cons ch acc))]))
    (mrl-h empty))
```
<br>

#### (read): consumes from input and produces an $S$-expression
- No matter how many characters or lines it occupies

```scheme
(define (read)
	(define exp (read))
    (cond
    	[(eof-object? exp) (void)]
        [else (display (<interp> (parse exp)) ;; <interp> exercise
        	  (newline)
              (<repl>)]) ;; <repl> exercise
    (<repl>))
```

## Write our own read
- Process typically happens in 2 steps:


#### _Tokenization_: convert the sequence of raw characters to a sequence of tokens.
- Tokens: meaningful "words"
  - left parenthesis & right parenthesis
  - identifier, representing a name 
  - number
- Convention
  - start with letter $\Rightarrow$ id
  - start with digit $\Rightarrow$ number
- Key observation
  - peeking at the next character tells us what kind of tokens we will be getting and what to look for to complete the token (aka what's valid)
    ​	
```scheme
(struct token (type value))
;; type: kind of token: 'lp, 'rp, 'id, 'num
;; value: "value" of the token: numeric value, name, etc.

;; Helpers
(define (token-leftpar? x) (symbol=? (token-type x) 'lp))
(define (token-rightpar? x) (symbol=? (token-type x) 'rp))

;; read-id: -> (listof char)
(define (read-id)
	(define nc (peek-char)) ;; only peek, don't read!!
    (if (or (char-alphabetic? nc) (char-numeric? nc))
    	(cons (read-char) (read-id)) ;; now read it
        empty))
        
;; read-number: -> (listof char)
(define (read-number)
	(define nc (peek-char)) ;; only peek, don't read!!
    (if (char-numeric? nc)
    	(cons (read-char) (read-number))
        empty))

;; main tokenizer:
;; read-token: -> token
(define (read-token)
	(define fc (read-char))
    (cond
    	[(char-whitespace? fc) (read-token)]
        [(char=? fc #\( ) (token 'lp fc)]
        [(char=? fc #\) ) (token 'rp fc)]
        [(char-alphabetic? fc) (token 'id (<list->symbol> (cons fc read-id)))]
        [(char-numeric? fc) (token 'num (<list->number> (cons fc read-number)))] 
        [else (error "lexical error")]))
```

#### _Parsing_: are the token arranged into a sequence that has a structure of an $S$-expression? If so, produce it. 

```scheme
;; Helper
;; read-list: -> (listof S-exp)

(define (read-list) ;; assume left parenthesis has already been read
	(define tk (read-token)
    (cond 
    	[(token-rightpar? tk) empty]
        [(token-leftpar? tk) (cons (read-list) (read-list))]
        ;; the first read-list is to read the new list
        ;; the second read-list is to finish the current list
        [else (cons (token-value tk) (read-list))]))
        
;; my-read -> S-exp
(define (my-read)
	(define tk (read-token))
    (if (token-leftpar? tk)
    	(read-list)
        (token-value tk)))

;; Exercise
;; Add support for symbols
;; Symbols can start with numbers, as long as they contain at least one letter

;; Handle arbitrary kinds of brackets
;; Need to match
```

