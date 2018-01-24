# Chapter 1. Linear Equations

## 1.1 Fields.

> <u>Summary:</u>
>
> ​	Not much is going on in this section. We mainly talk about the axioms of an algebraic field, with a brief touch on characteristic of a field.

### Field Axioms

- Addition
  - Associative
  - Commutative
  - Unique inverse
  - Unique identity
- Multiplication
  - Associative
  - Commutative
  - Unique inverse
  - Unique identity
- Addition and Multiplication
  - Distributive

---

### Characteristic

***Definition.*** 

​	The **characteristic** of a ring $R$, is defined to be the smallest number of times one must use the ring's multiplicative identity element (1) in a sum to get the additive identity element (0); the ring is said to be characteristic zero if this sum never reaches the additive identity.

***Remark.***

​	That is, $\text{char}(R)$ is the smallest positive number $n$ such that $\overbrace{1 + \cdots + 1}^{n \text{ summands}} = 0$ if such a number $n$ exists, and $0$ otherwise. The characteristic may also be taken to the exponent of the ring's additive group, that is, the smallest positive $n$ such that $\underbrace{a + \cdots + a}_{n \text{ summands}} = 0$ for every element $a$ of the ring. 

***

## 1.2 Systems of Linear Equations.

> <u>Summary:</u>
>
> ​	In this section, we formalize the process of solving systems of linear equations by elimination, introduce the concept of linear combination, and end with the conclusion that equivalent systems have the same set of solutions.

### System of Linear Equations

***Definition.***

​	Suppose $\mathbb{F}$ is a field. We consider the problem of finding $n$ scalars (elements of $\mathbb{F}$) $x_1, \ldots, x_n$ which satisfy the conditions

​						$$\begin{align*} A_{11}x_1 + A_{12}x_2 + &\cdots + A_{1n}x_n = y_1 \\A_{21}x_1 + A_{22}x_2 + &\cdots + A_{2n}x_n = y_2 \\ &\cdots \\ A_{m1}x_1 + A_{m2}x_2 + &\cdots + A_{mn}x_n = y_m\end{align*}$$			$(1.1)$

where $y_1, \ldots, y_m$ and $A_{ij}, 1 \leq i \leq m, i \leq j \leq n$, are given elements of $\mathbb{F}$. We call (1.1) a **system of $m$ linear equations in $n$ unknowns.** Any $n$-tuple $(x_1, \ldots, x_n)$ of elements $\mathbb{F}$ which satisfies each of the equations in (1.1) is called a **solution** of the system. If $y_0 = y_1 = \cdots = y_m = 0$, we say this system is **homogeneous**, or that each of the equations is homogeneous.

---

### Linear Combination

***Definition.***

​	For the general system (1.1), suppose we select $m$ scalars $c_1, \ldots, c_m$, multiply the $j$th equation by $c_j$, and then add. We obtain the equation

​						$$\begin{align*} &\phantom{aii}(c_1A_{11} + \cdots + c_mA_{m1})x_1\\ &+ (c_1A_{12} + \cdots + c_mA_{m2})x_2 \\ &+ \qquad \qquad\cdots \\&+ (c_1A_{1n} + \cdots + c_mA_{mn})x_n\\ &-------------\\ &= c_1y_1 + \cdots + c_my_m\end{align*}$$

Such an equation is called a **linear combination** of the equations in (1.1). Evidently, any solution of the entire system of equations (1.1) will also be a solution of this new equation. _This is the fundamental idea of the elimination process._ That is, if we have another system of linear equations

​							$$ \begin{align*} B_{11}x_1 + &\cdots + B_{1n}x_n = z_1 \\  &\cdots\\ B_{k1}x_1 + &\cdots + B_{kn}x_n = z_k \end{align*}$$					$(1.2)$

in which each of the $k$ equations is a linear combination of the equations in (1.1), then every solution of (1.1) is a solution of this new system. However, some solutions to the new system might not be valid solutions to the old system, since each equation in the original system might not be a linear combination of some equations in the new system. But when each equation in each system is a linear combination of the equations in the other system, we say that two systems of linear equations are **equivalent**. 

---

### Equivalent Systems Have the Same Set of Solutions

***Theorem 1.***

​	Equivalent systems of linear equations have exactly the same solutions. 

---

## 1.3 Matrices and Elementary Row Operations.

> <u>Summary</u>
>
> ​	This section provides us the first taste of the world of matrices; we start to see the use of matrix as a shorthand notation for our system of linear equations. We also defined what elementary row operations are, proved that each ERO has an inverse operation, looked at an equivalence relation row-equivalence, and proved that two homogeneous, row-equivalent systems of linear equations have the same solutions. We then introduced the concept of "row-reduced" matrix and proved that each matrix can be reduced to one such matrix by carefully manipulating each row in the matrix. Be sure to understand the definition of "row-reduced" matrix and theorems 3 and 4 discussed in this section as they will be used quite often to prove more advanced results.

### First Interpretation of a Matrix

***Definition.***

​	We shall now abbreviate the system (1.1) by writing $AX = Y$, where 

​				$A = \begin{bmatrix} A_{11} & \cdots & A_{1n} \\ \vdots & & \vdots \\ A_{m1} & \cdots & A_{mn}\end{bmatrix}, X = \begin{bmatrix}x_1 \\ \vdots \\ x_n\end{bmatrix}, Y = \begin{bmatrix}y_1 \\ \vdots \\ y_m \end{bmatrix}$ .

We call $A$ the **matrix of coefficients** of the system. An $m \times n$ **matrix over the field** $\mathbb{F}$ is a function $A$ from the set of pairs of integers $(i,j), 1 \leq i \leq m, 1 \leq j \leq n$, into the field $\mathbb{F}$ ==(David: this is the first way to interpret the concept of "matrix": a function $A : (i,j) \rightarrow \mathbb{F}$, that is, each entry $a_{ij}$ contains an element from $\mathbb{F}$)==.  The **entries** of the matrix $A$ are the scalars $A(i,j) = A_{ij}$, and quite often it is most convenient to describe the matrix by display its entries in a rectangular array having $m$ rows and $n$ columns, as above. $X$ is an $n \times 1$ matrix; $Y$ is an $m \times 1$ matrix. For now, we can treat $AX = Y$ just as a shorthand notation for our system of linear equations ==(David: this is the first way to interpret the equation $AX = Y$, later on we will look at more interesting interpretations. You can see this as a (naive) justification of why we need the matrix representation in mathematics)==. 

---

### Elementary Row Operations and Its Implications

***Definition.***

There are three **elementary row operations** on an $m \times n$ matrix $A$ over the field $\mathbb{F}$: 

1. multiplication of one row of $A$ by a non-zero scalar $c$;
2. Replacement of the $r$th row of $A$ by row $r$ plus $c$ times row $s$, $c$ can be any scalar and $r \ne s$. 
3. Interchange two rows of $A$. 

An elementary row operation is thus a special type of function (rule) $e$ which associate an $m \times n$ matrix $e(A)$ with each $m \times n$ matrix $A$. One can precisely describe $e$ in the three cases as follows:

1. $e(A)_{ij} = A_{ij} \quad \text{if} \quad  i \ne r,  \quad e(A)_{rj} = cA_{rj}$.
2. $e(A)_{ij} = A_{ij} \quad \text{if} \quad  i \ne r,  \quad e(A)_{rj} = A_{rj} + cA_{sj}$.
3. $e(A)_{ij} = A_{ij} \quad \text{if} \quad  i \ne r, s,  \quad e(A)_{rj} = A_{rj}, e(A)_{sj} = A_{rj}$.

In defining $e(A)$, we don't really care about $n$, the number of columns, but we do care about $m$, the number of rows. To avoid complications, we agree that an elementary row operation $e$ is defined on the class of all $m \times n$ matrices over $\mathbb{F}$, for some fixed $m$ but any $n$. In other words, a particular $e$ is defined on the class of all $m$-rowed matrices over $\mathbb{F}$. 



***Theorem 2.***

​	To each elementary row operation $e$ there corresponds an elementary row operation $e_1$, of the same type as $e$, such that $e_1(e(A)) = e(e_1(A)) = A$ for each $A$. In other words, the inverse operation (function) of an elementary row operation exists and is an elementary row operation of the same type. 



***Definition.***

​	If $A$ and $B$ are $m \times n$ matrices over the field $\mathbb{F}$, we say that $B$ is **row-equivalent** to $A$ if $B$ can be obtained from $A$ by a finite sequence of elementary row operations.



***Remark.***

​	Row-equivalence is an equivalence relation (reflexive, symmetric, transitive).



***Theorem 3.***

​	If $A$ and $B$ are row-equivalent $m\times n$ matrices, the homogeneous system of linear equations $AX = 0$ and $BX = 0$ have exactly the same solutions.

***Proof.***

​	Suppose we pass from $A$ to $B$ by a finite sequence of elementary row operations:

​							$$A = A_0 \rightarrow A_1 \rightarrow \cdots \rightarrow A_k = B$$.

It is enough to prove that the systems $A_jX = 0$ and $A_{j+1}X= 0$ have the same solutions, ie. that one elementary row operation does not disturb the set of solutions. So suppose that $B$ is obtained from $A$ by a single elementary row operation. No matter which of the three types the operation is, each equation in the system $BX = 0$ will be a linear combination of the equations in the system $AX = 0$. Since the inverse of an elementary row operation is an elementary operation, each equation in $AX=0$ will also be a linear combination of the equations in $BX=0$. Hence these two systems are equivalent, and by ***Theorem 1*** they have the same solutions.

---

### Row-Reduced Matrices and Its Implications

***Definition.*** 

An $m\times n$ matrix $R$ is called **row-reduced** if:

1. The first non-zero entry in each non-zero row of $R$ is equal to $1$. 
2. Each column of $R$ which contains the leading non-zero entry of some row has all its other entries $0$.

***Remark.***

​	One example of a row-reduced matrix is the $n\times n$ **identity matrix $I$**. This is the $n \times n$ matrix defined by 

​						$$I_{ij}=\delta_{ij} =\begin{cases}1 \qquad \text{if} \quad i = j \\ 0 \qquad \text{if} \quad i \ne j \end{cases}$$ .

$\delta$ here is the **Kronecker delta**. 



***Theorem 4.***

​	Every $m \times n$ matrix over $\mathbb{F}$ is row-equivalent to a row-reduced matrix. 

***Proof.***

​	Let $A$ be an $m \times n$ matrix over $\mathbb{F}$. If every entry in the first row of $A$ is $0$, then condition (1) is satisfied. If row 1 has a non-zero entry, let $k$ be the smallest positive integer $j$ for which $A_{1j} \ne 0$. Multiply row 1 by $A_{1k}^{-1}$, and then condition (1) is satisfied with regard to row 1. Now for each $i \leq 2$, add $(-A_{ik})$ times row 1 to row $i$. Now the leading non-zero entry of row 1 occurs in column $k$, that entry is $1$, and every other entry in column $k$ is $0$.

​	Now consider the matrix which has resulted from above. If every entry in row 2 is $0$, we do nothing to row 2. If some entry in row 2 is different from $0$, we multiply row 2 by a scalar so that the leading non-zero entry is $1$. In the event that row 1 had a leading non-zero entry in column $k$, this leading non-zero entry of row 2 cannot occur in column $k$; say it occurs in column $k_r \ne k$. By adding suitable multiples of row 2 to the various rows, we can arrange that all entries in column $k_r$ are $0$, except the $1$ in row 2. The important thing to notice is this: In carrying out these last operations, we will not change the entries of row 1 in columns $1, \ldots , k$; nor will we change any entry of column $k$. Of course, if row 1 was identically $0$, the operations with row 2 will not affect row 1. 

​	Working with one row at a time in the above manner, it is clear that in a finite number of steps we will arrive at a row-reduced matrix. 

---

## 1.4 Row-Reduced Echelon Matrices.

> <u>Summary:</u>
>
> ​	Continue from section 1.3, we now define a even more handy representation of a "nice" matrix -- the row-reduced echelon matrix. Since we only need a finite sequence of interchanges to bring a row-reduced matrix to its row-reduced echelon form, we conclude that each matrix would have its unique row-reduced echelon matrix as well. Moreover, we proved two crucial theorems on homogeneous systems, please make sure you understand the logic behind them. And last, we talked about inhomogeneous systems, how to determine if there exists a solution, and if so how to find them.

### Row-Reduced Echelon Matrix and Its Implications

***Definition.***

An $m\times n$ matrix $R$ is called a **row-reduced echelon matrix** if 

1. $R$ is row-reduced;
2. Every row of $R$ which has all its entries $0$ occurs below every row which has a non-zero entry;
3. If rows $1, \ldots, r$ are the non-zero rows of $R$, and if the leading non-zero entry of row $i$ occurs in column $k_i, i = 1, \ldots, r$, then $k_1 < k_2 < \cdots < k_r$. 



***Theorem 5.***

​	Every $m \times n$ matrix $A$ is row-equivalent to a row-reduced echelon matrix.

***Proof.***

​	We know that $A$ is row-equivalent to a row-reduced matrix. All that we need observe is that by performing a finite number of row interchanges on a row-reduced matrix we can bring it to row-reduced echelon form.



***Remark.***

​	Consider the system $RX = 0$, where $R$ is a row-reduced echelon matrix. Let rows $1, \ldots, r$ be the non-zero rows of $R$, and suppose that the leading non-zero entry of row $i$ occurs in column $k_i$. The system $RX=0$ then consists of $r$ non-trivial equations (every other equations are of the form $0x_1 + 0x_2 + \cdots + 0x_n = 0$). Also the unknown ${x_k}_i$ will occur (with non-zero coefficient) only in the $i$th equation ==(David: think about the definition of row-reduced echelon matrix)==. If we let $u_1, \ldots, u_{n-r}$ denote the $(n-r)$ unknowns which are different from ${x_k}_1, \ldots, {x_k}_r$, then the $r$ non-trivial equations in $RX = 0$ are of the form

​								$$\begin{align*} {x_k}_1 &+ \sum_{j=1}^{n-r} C_{1j}u_j = &0 \\ &\vdots &\vdots \\{x_k}_r &+ \sum_{j=1}^{n-r} C_{rj}u_j =&0.\end{align*}$$ 					$(1.3)$

All the solutions to the system of equations $RX = 0$ are obtained by assigning any values whatsoever to $u_1, \ldots, u_{n-r}$ ==(David: they are the free variables in this system)== and then computing the corresponding values of ${x_k}_1, \ldots, {x_k}_r$ from $(1.3)$. 

​	One more interesting observation: if the number $r$ of non-zero rows in $R$ is less than $n$, then the system $RX = 0$ has a non-trivial solution, that is, a solution $(x_1, \ldots, x_n)$ in which not every $x_j$ is $0$. This is because, since $r < n$, we can choose some $x_j$ which is not among the $r$ unknowns ${x_k}_1, \ldots, {x_k}_r$, and we can then construct a solution as above. This observation leads us to one of the most fundamental facts concerning systems of homogeneous linear equations.

---

### Two Crucial Theorems on Homogeneous Systems

***Theorem 6.***

​	If $A$ is an $m\times n$ matrix and $m < n$, then the homogeneous system of linear equations $AX = 0$ has a non-trivial solution.

***Proof.***

​	Let $R$ be a row-reduced echelon matrix which is row-equivalent to $A$. Then the system $AX=0$ and $RX=0$ have the same solutions by ***Theorem 3.*** If $r$ is the number of non-zero rows in $R$, then certainly $r \leq m$, and since $m < n$, we have $r < n$. It follows immediately from our remarks above that $AX=0$ has a non-trivial solution.



***Theorem 7.***

​	If $A$ is an $n \times n$ matrix, then $A$ is row-equivalent to the $n \times n$ identity matrix if and only if the system of equations $AX = 0$ has only the trivial solution.

***Proof.***

​	If $A$ is row-equivalent to $I$, then $AX=0$ and $IX=0$ has the same solutions, ie. the solution must be trivial. Conversely, suppose $AX=0$ has only the trivial solution $X=0$. Let $R$ be an $n\times n$ row-reduced echelon matrix which is row-equivalent to $A$, and let $r$ be the number of non-zero rows of $R$. Then $RX=0$ has no non-trivial solution (because $R$ is associated with $A$). Thus $r \geq n$ (see ***Theorem 6***). But since $R$ has $n$ rows, certainly $r\leq n$, and thus $r = n$. Since this means that $R$ actually a has a leading non-zero entry of $1$ in each of its $n$ rows, and since these $1$'s occur each in a different one of the $n$ columns, $R$ must be the $n \times n$ identity matrix. 

---

### Inhomogeneous Systems and Augmented Matrices

***Remark.***

​	While the homogeneous system always has trivial solution, an inhomogeneous system doesn't need a solution.

***Definition.***

​	We form the **augmented matrix** $A'$ of the system $AX=Y$. This is the $m \times (n+1)$ matrix whose first $n$ columns are the columns of $A$ and whose last column is $Y$.

***Remark.***

​	Suppose we perform a sequence of elementary row operations on $A$, arriving at a row-reduced echelon matrix $R$. If we perform this same sequence of row operations on $A'$, we will arrive at a matrix $R'$ whose first $n$ columns are the columns of $R$ and whose last column contains certain scalars $z_1, \ldots, z_m$. The scalars $z_i$ are the entries of the $m\times 1$ matrix 

​						  			$Z = \begin{bmatrix}z_1 \\\vdots \\z_m\end{bmatrix}$ 

which results from applying the sequence of row operations to the matrix $Y$. By ***Theorem 3***, $AX=Y$ and $RX=Z$ are equivalent and hence have the same solutions. 

​	It is very easy to determine whether $RX=Z$ has any solutions and to determine all the solutions if any exists. For example, say $R$ has $r$ non-zero rows, then the last $r$ equations of $RX=Z$ effectively express ${x_k}_1, \ldots, {x_k}_r$ in terms of the $(n-r)$ remaining $x_j$ and the scalars $z_1, \ldots, z_r$. The last $(m-r)$ equations are 

​									$\begin{align*} 0 &= z_{r+1} \\ &\;\;\vdots \\0 &= z_m\end{align*}$

and accordingly the condition for the system to have a solution is $z_i = 0$ for $i > r$. If this condition is satisfied, all solutions to the system are found just as in the homogeneous case, by assigning arbitrary values to $(n-r)$ of the $x_j$ and then computing ${x_k}_i$ from the $i$th equation.

---

##1.5 Matrix Multiplications.

> <u>Summary:</u>
>
> ​	This is the messy part of matrix operations. We showed how to do multiplications on matrices, and proved its associativity. We then defined what elementary matrices are and linked them with the elementary row operations we learned in section 1.3. Furthermore, this section gives us a new perspective of looking at elementary row operations and matrix multiplication: when we perform an elementary row operation, essentially we are multiplying the corresponding elementary matrix (from the left side) with our matrix, and vice versa. The corollary afterwards is worth thinking about as well: basically, we gave out an alternative definition (in terms of elementary matrices, instead of elementary row operations, see section 1.3.2 definition of row-equivalence if necessary) of row-equivalence.

### Multiplication Rule

***Definition.*** 

- Let $A$ be an $m \times n$ matrix over the field $\mathbb{F}$ and let $B$ be an $n \times p$ matrix over $\mathbb{F}$. The **product** $AB$ is the $m \times p$ matrix $C$ whose $i, j$ entry is 

  ​						$\displaystyle C_{ij} = \sum_{r=1}^n A_{ir}B_{rj}$. 

***Remark.***

- The product of two matrices is defined if and only if the number of columns in the first matrix coincides with the number of rows in the second matrix.
- $I_{m, m}A_{m,n} = A_{m,n}$, $A_{m,n} I_{n, n} = A{m,n}$ 
- $0^{k,m} A_{m,n} = 0^{k,n}, A_{m,n}0^{n,p}=0^{m,p}$.

------

### Multiplication is Associative

***Theorem 8.***

- If $A, B, C$ are matrices over $\mathbb{F}$ such that the produces $BC$ and $A(BC)$ are defined, then so are the produces $AB, (AB)C$ and 

  ​						$$A(BC) = (AB)C.$$

***Proof.***

- Suppose $B$ is an $n \times p$ matrix. Since $BC$ is defined, $C$ is a matrix with $p$ rows, and $BC$ has $n$ rows. Since $A(BC)$ is defined, we may assume $A$ is an $m \times n$ matrix. Thus the product $AB$ exists and is an $m \times p$ matrix, from which it follows that the product $(AB)C$ exists. 

- Now we want to show that $A(BC) = (AB)C$, or $[A(BC)]_{ij} = [(AB)C]_{ij}, \forall i, j$. By definition, 

  ​			$[A(BC)]_{ij} = \sum_r A_{ir}(BC)_{rj}$

  ​					  $= \sum_r A_{ir} \sum_s B_{rs}C_{sj} $

  ​					  $= \sum_r  \sum_s A_{ir}B_{rs}C_{sj} $

  ​					  $= \sum_s  \sum_r A_{ir}B_{rs}C_{sj} $

  ​					  $= \sum_s  (\sum_r A_{ir}B_{rs})C_{sj} $

  ​					  $= \sum_s  (AB)_{is}C_{sj} $

  ​					    $= \left[(AB)C\right]_{ij} $

------

### Elementary Matrix

***Remark.***

- When $A$ is a square matrix, the produce $AA$ is defined. We shall denote this matrix by $A^2$. By the above theorem, $(AA)A = A(AA)$, so $AAA$ is also well-defined. In general, the product $AA \cdot A$ ($k$ times) is unambiguously defined, and we shall denote this product by $A^k$. 

- If $B$ is a given matrix and $C$ is obtained from $B$ by means of an elementary row operation, then each row of $C$ is a linear combination of the rows of $B$, and hence there is a matrix $A$ such that $AB = C$. In general there are many such matrices $A$, and among all such it is convenient and possible to choose one having a number of special properties. This leads to the following definition:

  ​

***Definition.***

​	An $m \times n$ matrix is said to be an **elementary matrix** if it can be obtained from the $m \times m$ identity matrix by means of a single elementary row operation. 



***Example.***

​	A $2 \times 2$ elementary matrix is necessarily one of the following:

​	$\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$: exchange rows

​	$\begin{bmatrix} 1 & c \\ 0 & 1 \end{bmatrix}$: $r_1 = r_1 + c \cdot r_2$

​	$ \begin{bmatrix} 1 & 0 \\ c & 1 \end{bmatrix}$: $r_2 = r_2 + c\cdot r_1$

$\begin{bmatrix} c\ne 0 & 0 \\ 0 & 1 \end{bmatrix}$: $r_1 = c \cdot r_1, c \ne 0$

$ \begin{bmatrix} 1 & 0 \\ 0 & c \ne 0 \end{bmatrix}$: $r_2= c \cdot r_2, c \ne 0$

------

### Each Elementary Row Operation Corresponds with a Elementary Matrix

***Theorem 9.***

​	Let $e$ be an elementary row operation, and let $E$ be the $m \times m$ elementary matrix $E = e(I)$. Then, for every $m \times n$ matrix $A$,

​							$$e(A) = EA$$.

***Remark.***

- $e(I)$ means the output of identity matrix $I_m$ after a single elementary row operation.
- ==(David: here is a new perspective of looking at elementary row operations by treating them as some sort of product between $A$ and the corresponding elementary matrix $E$)== 

***Proof.***

- The point of the proof is that the entry in the $i$th row and $j$th column of the product matrix $EA$ is obtained from the $i$th row of $E$ and $j$th column of $A$. 

- The three types of elementary row operations should be taken up separately.

  - $e_1$: exchange two rows.

    - Let $A$ be an $ 2\times 3$ matrix :$A = \begin{bmatrix} a & b & c \\d & e & f\end{bmatrix}$.
    - $E_1$ be the $ 2 \times 2$ elementary matrix $E_1 = e_1(I_m)$: $E_1 = \begin{bmatrix}0 & 1 \\ 1 & 0\end{bmatrix}$. 
    - Perform $e_1$ on $A$ we get $e_1(A) = A' = \begin{bmatrix} d & e & f \\a & b & c\end{bmatrix}$.
    - The product of $E_1A:$  $E_1A = \begin{bmatrix} 0 \cdot a + 1 \cdot d & 0 \cdot b + 1 \cdot e & 0 \cdot c + 1 \cdot f \\ 1 \cdot a + 0 \cdot d & 1 \cdot b + 0 \cdot e & 1 \cdot c + 0 \cdot f \end{bmatrix} = \begin{bmatrix} d & e & f \\a & b & c\end{bmatrix} = A' = e_1(A)$
    - Hence $e_1(A) = E_1A$. 

  - $e_3$: multiply row $r_i$ by a scalar $k$.

    - Let $A$ be an $ 2\times 3$ matrix :$A = \begin{bmatrix} a & b & c \\d & e & f\end{bmatrix}$.
    - $E_2$ be the $ 2 \times 2$ elementary matrix $E_2 = e_2(I_m)$: $E_2 = \begin{bmatrix}  k & 0 \\  0 & 1\end{bmatrix}$. 
    - Perform $e_2$ on $A$ we get $e_2(A) = A' = \begin{bmatrix}  ka & kb & kc \\d & e & f\end{bmatrix}$.
    - The product of $E_2A:$  $E_2A = \begin{bmatrix}  k\cdot a + 0 \cdot d & k \cdot b + 0 \cdot e & k \cdot c + 0 \cdot f \\ 0 \cdot a + 1 \cdot d & 0 \cdot b + 1 \cdot e & 0 \cdot c + 1 \cdot f \end{bmatrix} = \begin{bmatrix} ka & kb & kc \\d & e & f\end{bmatrix} = A' = e_2(A)$
    - Hence $e_2(A) = E_2A$. 

  - $e_2$: replace row $r_j$ by row $r_j$ plus $c \cdot r_s$. 

    - Suppose $r \ne s$. Then 

      ​		$$\displaystyle E_{ik} = \begin{cases} \delta_{ik}, \quad i \ne r \\ \delta_{rk}+c\delta_{sk}, \quad i = r\end{cases}$$ 

    - Therefore,

      ​		$$\displaystyle (EA)_{ij} = \sum_{k=1}^m E_{ik}A_{kj} = \begin{cases} A_{ik}, \quad i \ne r \\ A_{rj} + cA_{sj}, \quad i = r\end{cases}$$

      ​

***Corollary.*** 

​	Let $A$ and $B$ be $m \times n$ matrices over $\mathbb{F}$. Then $B$ is row-equivalent to $A$ if and only if $B = PA$, where $P$ is a product of $m \times m$ elementary matrices. 

***Proof.***

- Suppose $B = PA$ where $P = E_s \cdots E_2 E_1$ and the $E_i$ are $m \times m$ elementary matrices. Then $E_1A$ is row-equivalent to $A$, and $E_2(E_1A)$ is row-equivalent to $E_1A$, so $E_2E_1A$ is row-equivalent to $A$; and continuing in this way we see that $(E_s\cdots E_1)A$ is row-equivalent to $A$. 
- Now suppose that $B$ is row-equivalent to $A$. Let $E_1, E_2, \ldots, E_s$ be the elementary matrices corresponding to some sequence of elementary row operations which carries $A$ to $B$. Then $B = (E_s \cdots E_1) A$. 

---

## 1.6 Invertible Matrices.

> <u>Summary:</u>
>
> ​	In this section, we look at a unique attribute of (most) square matrices: having a unique inverse matrix. We then provided many useful theorems and corollaries, despite most of them are simply rephrasing statements that were already proven before. Try to understand the logic behind these seemingly complicated statements and you will be fine. 

### Inverses

***Definition.***

​	Let $A$ be an $n \times n$ (square) matrix over $\mathbb{F}$. An $n \times n$ matrix $B$ such that $BA = I$ is called a **left inverse** of $A$; an $n \times n$ matrix $B$ such that $AB = I$ is called a **right inverse** of $A$. If $AB = BA = I$, then $B$ is called a **two-sided inverse** of $A$ and $A$ is said to be **invertible**.



***Lemma.***

​	If $A$ has a left inverse $B$ and a right inverse $C$, then $B = C$. 

***Proof.***

​	Suppose $BA = I = AC$, then $B = BI = B(AC) = (BA)C = IC = C$. 



***Remark.***

- If $A$ has an inverse, then this inverse works on both sides, and is unique.


- A square matrix that is not invertible is called **singular** or **degenerate**. A square matrix is singular if and only if its **determinant** is $0$. Non-square matrices do not have an inverse, but in some cases such a matrix may have a left inverse or right inverse.

---

### Theorems and Corollaries on Inverses

***Theorem 10.***

Let $A$ and $B$ be $n \times n$ matrices over $\mathbb{F}$. 

- If $A$ is invertible, so is $A^{-1}$ and $(A^{-1})^{-1} = A$.
- If both $A$ and $B$ are invertible, so is $AB$ and $(AB)^{-1} = B^{-1}A^{-1}$. 

***Corollary.***

​	A product of invertible matrices is invertible.



***Theorem 11.***

​	An elementary matrix is invertible.

***Proof.***

​	Let $E$ be an elementary matrix corresponding to the elementary row operation $e$. If $e_1$ is the inverse operation of $e$ and $E_1 = e_1(I)$, then $EE_1 = e(E_1) = e(e_1(I)) = I$ and $E_1E = e_1(E) = e_1(e(I)) = I$, so that $E$ is invertible and $E_1 = E^{-1}$. 



***Theorem 12.***

If $A$ is an $n \times n$ matrix, the following are equivalent:

- $A$ is invertible.
- $A$ is row-equivalent to the $n \times n$ identity matrix.
- $A$ is a product of elementary matrices.

***Proof.***

​	Let $R$ be a row-reduced echelon matrix which is row-equivalent to $A$. By ***Theorem 9*** (or its corollary), $R = E_k \cdots E_2E_1A$, where $E_1, \ldots, E_k$ are elementary matrices. Each $E_j$ is invertible, and so $A = E_1^{-1} \cdots E_k^{-1} R$. Since products of invertible matrices are invertible, we see that $A$ is invertible if and only if $R$ is invertible. Since $R$ is a (square) row-reduced echelon matrix, $R$ is invertible if and only if each row of $R$ contains a non-zero entry, that is, if and only if $R = I$. We have now shown that $A$ is invertible if and only if $R = I$, and if $R = I$ then $A = E_k^{-1} \cdots E_1^{-1}$. It should now be apparent that the three statements are equivalent statements about $A$. 

***Remark.***

​	An invertible matrix does not contain any rows (think about the bijection for inverses). 



***Corollary.***

​	If $A$ is an invertible $n \times n$ matrix and if a sequence of elementary row operations reduces $A$ to the identity, then that same sequence of operations when applied to $I$ yields $A^{-1}$. 

***Corollary.***

​	Let $A$ and $B$ be $m \times n$ matrices. Then $B$ is row-equivalent to $A$ if and only if $B = PA$ where $P$ is an invertible $m \times m$ matrix.



***Theorem 13.***

For an $n\times n$ matrix $A$, the following are equivalent:

- $A$ is invertible.
- The homogeneous system $AX=0$ has only the trivial solution $X=0$. 
- The system of equations $AX= Y$ has a solution $X$ for each $n \times 1$ matrix $Y$.

***Proof.***

​	According to ***Theorem 7***, statement 3 is equivalent to the fact that $A$ is row-equivalent to the identity matrix. By ***Theorem 12***, statement 1 and 3 are thus equivalent. If $A$ is invertible, the solution of $AX = Y$ is $X = A^{-1}Y$. Conversely, suppose $AX = Y$ has a solution for each given $Y$. Let $R$ be a row-reduced echelon matrix which is row-equivalent to $A$. We wish to show $R= I$. That amounts to showing that the last row of $R$ is not $0$. Let

​										$E = \begin{bmatrix} 0\\ 0\\\vdots \\0\\1\end{bmatrix}$. 

If the system $RX = E$ can be solved for $X$, the last row of $R$ cannot be $0$. We know that $R = PA$, where $P$ is invertible. Thus $RX =E$ if and only if $AX = P^{-1}E$. According to the third statement, the latter system has a solution.



***Corollary.***

​	A square matrix with either a left or right inverse is invertible.

***Proof.***	

​	Let $A$ be an $n \times n$ matrix. Suppose $A$ has a left inverse, ie., a matrix $B$ such that $BA = I$. Then $AX = 0$ has only the trivial solution, because $X = IX = B(AX)$. Therefore $A$ is invertible. On the other hand, suppose $A$ has a right inverse, ie. a matrix $C$ such that $AC = I$. Then $C$ has a left inverse and is therefore invertible. It then follows that $A = C^{-1}$ and so $A$ is invertible with inverse $C$. 



***Corollary.***

​	Let $A = A_1A_2\ldots A_k$ where $A_1, \ldots, A_k$ are $n \times n$ matrices. Then $A$ is invertible if and only if each $A_j$ is invertible. 

***Proof.***

​	We have already shown that the product of two invertible matrices is invertible. Use induction we can see that $A$ is invertible if and only if each $A_j$ is invertible. Suppose now that $A$ is invertible. We first prove that $A_k$ is invertible. Suppose $X$ is an $n \times 1$ matrix and $A_kX = 0$. Then $AX = (A_1\ldots A_{k-1})A_kX = 0$. Since $A$ is invertible we must have $X = 0$. The system of equations $A_kX= 0$ thus has no non-trivial solution, so $A_k$ is invertible. But now $A_1\cdots A_{k-1} = AA^{-1}_k$ is invertible. By the preceding argument, $A_{k-1}$ is invertible. Continuing this way, we conclude that each $A_j$ is invertible.



***Formula.*** 

​	Let $A \in M_{n,n}$ be an invertible matrix. To find $A^{-1}$, construct an augmented matrix $[A|I_n]$, and try to reduce the left side to the identity matrix $I_n$. When you get there, the right half of the augmented matrix is our desired $A^{-1}$. 

---

---

Version 1.0 2018-01-19 01:00 

Version 1.1 2018-01-22 10:37

David Duan