# Jan 10 Tutorial
---
#####Bash: file as input and output
```java
> x # save output to x
< x # read input from x
# these two can be combined
```

#####Bash: compile file.c
```bash
gcc hello.c -o hello # compile <hello.c> to output <hello>
./hello # you can run it in command line
```

#####Bash: more file stuff and diff
```bash
x | y: the eoutput of x as input of y
x && y: execute x and y from left to right
diff: compare two files; no outputs means the two files are the same.
# you can use diff to check if ur output is the same as expected.
```

#####$\heartsuit$Haskell$\heartsuit$: pattern-matching
```Haskell
data Lst = Empty 
		 | Cons Integer Lst
         
len :: Lst -> Integer
len Empty = 0 
len (x:xs) = 1 + len xs

map :: (Integer -> Integer) -> Lst -> Lst
map _ Empty = Empty
map f (x:xs) = (cons (f x) (map f xs))

foldl :: (Integer -> Integer -> Integer) -> Integer -> Lst -> Lst
foldl _ z Empty = z
foldl f z (x:xs) = foldl f z' xs
	where z' = f z x
```
```Haskell
prepend :: Integer -> [[Integer]] -> [[Integer]]
prepend i [] = [i]
prepend i (n:ns) = [i n] : prepend i ns
```
