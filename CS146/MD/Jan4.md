_CS 146_ 
_LEC_
_Jan4_

### Major theme:
- **Side-effects**, or **impurity**
- Programs that do things
- Imperative programming
- Languages:
	- Impure racket
	- C
	- Low level machine

### Why functional first?
- **Side effects - change the state of the world**
	- Text printed to screen
	- Keystrokes collected from keypads
	- Values of variables change
- ** The state of the world affects the program**
	- `(define (f x) ( + x y))`
	- Depends on the value of y
- Thus, the semantics of an imperative program must take into account the current state of the world, even while changing teh state of the world. There is a temporal component inherent in the analysis of imperative programs. It's not "what does this do?" but "what does this do at this point in time?"


### Why study imperative programming?
- "The world is imperative"
	- Machines work by mutating memory
	- Even functional programs are executed imperatively
- Is the world being constantly _**mutating**_ or _**reinvented**_?
	- When a character is on the screen, does that change the world or created a new one?
- Either way, imperative programming matches real-world experiences
	- But a functional worldview may offer a unique take on side-effects

### Prereq
- Proof, big-O, analysis, lambda
- Language: full racket, C (no seashell)

### Recall from CS135/145
- Structural Recursion: the structure of the program matches the structure of the data










