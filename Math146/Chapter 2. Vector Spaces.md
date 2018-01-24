# Chapter 2. Vectors Spaces



## 2.1 Vector Spaces



***Definition.***

​	A **vector space** over a field $\mathbb{F}​$ is a set of elements called vectors equipped with an addition and a scalar multiplication:

- A field $\mathbb{F}$ of scalars
- A set $\mathbb{V}$ of objects, called vectors;


- $+ : (u,v) \mapsto u + v, u, v \in \mathbb{V}$. ==(Under addition, my vectors should behave as a additive group. You can treat this addition as our normal addition over a field.)==
  - Commutativity
  - Associativity
  - Unique additive identity $0$, the _zero vector_.
  - Unique additive inverse 
- $ \cdot : (\alpha, v) \mapsto a\cdot v, \alpha \in \mathbb{F}, v \in \mathbb{V}$.
  - Unique multiplicative identity $1$
  - Associativity over scalars: $(c_1c_2)\alpha = c_1(c_2\alpha)$.
    - Note that we did **NOT** define the multiplication between two vectors.
  - Distributivity over vectors: $c(\alpha + \beta) = c\alpha + c\beta$
  - Distributivity over scalars: $(c_1 + c_2)\alpha = c_1\alpha + c_2\alpha$



***Example.*** Probably ask prof for more clarifications. 

- The space $\mathbb{F}^n$ is a vector space (it is the motivation for this definition).


- The space $M_{m,n}(\mathbb{F})​$ is a vector space.
  - For $[a_{ij}], [b_{ij}], \in M_{m,n}(\mathbb{F})$, $\alpha \in \mathbb{F}$ , $[a_{ij}] + [b_{ij}] = [a_{ij}+b_{ij}]$, $\alpha[a_{ij}] = [a\alpha_{ij}]$.
- Consider $\square, \diamondsuit, \heartsuit$. Define $\{\alpha\square + \beta \diamondsuit + \gamma \heartsuit : \alpha, \beta, \gamma \in \mathbb{R}\}$ with rules for $\mathbb{F}^3$.  ==(This is just $\mathbb{F}^3$ in disguise, but it is very useful to define vector space in this way)==. 
- Consider the set of polynomials, say $\mathbb{F}[t] = \{a_0 + a_1t+a_2t^2+\cdots+a_nt^n\}$ ==(coefficients from $\mathbb{F}$, with variable $t$)==. This is a vector space with the usual addition and scalar multiplication ==(note the similarity to the last example)==. 
- Let $X$ be a set, let $F(X, \mathbb{F})$ denote the set of functions ==(all functions)== from $X$ to $\mathbb{F}$. 
  - $(f+g)(x) := f(x)+g(x), f,g, \in F(X,\mathbb{F}), x\in X$
- Note: ex.1 and ex.2 are special cases of this example, because an $m\times n$ matrix $A$ can be viewed as a function from $X = \{(i,j):1\leq i \leq m, 1 \leq j \leq n\}$, $(i,j) \mapsto [A]_{ij}$. Similarly for $\mathbb{F}^n$. Actually $\mathbb{F}^n \cong M_{m,n}(\mathbb{F})$. 
- Note: $\mathbb{F}[t] \subseteq F(\mathbb{F}, \mathbb{F})$ -- we cast $x \in \mathbb{F}$ into $\mathbb{F}$ by plugging in $x$ into the polynomial.



***Remark.***

- $V$ defines operations, $\mathbb{F}$ tells you what scalars you can use. 
- ==Ex. The complex numbers $\mathbb{C}$ over the field $\mathbb{R}$.==
  - Scalars: they all live in $\mathbb{R}$. 
  - Note that $\mathbb{C} = \{a + ib\;:\; a,b \in \mathbb{R}\}$. 
    - $\mathbb{C}$ is a two-dimensional vector space over $\mathbb{R}$. 
    - $\mathbb{C} \cong \mathbb{R}^2$: $\mathbb{C}$ is isomorphic to $\mathbb{R}^2$.



***Definition.***

​	Let $\mathbb{V}$ be a vector space over a field $\mathbb{F}$. We say $x \in \mathbb{V}$ is a **linear combination** of the vectors $x_1, \ldots, x_k \in \mathbb{V}$, if there are scalars $a_1, \ldots, a_k \in \mathbb{F}$ such that $x = \sum_{i=1}^k a_ix_i$. 

---

## 2.2 Subspaces

***Definition.***

​	Let $\mathbb{V}$ be a vector space over the field $\mathbb{F}$. A **subspace** of $\mathbb{V}$ is a subset $\mathbb{W}$ of $\mathbb{V}$ which is itself a vector space over $\mathbb{F}$ with the operations of vector addition and scalar multiplication on $\mathbb{V}$. $\mathbb{W}$ satisfies the following axioms:

1. $0 \in \mathbb{W}$.
2. Closed under addition.
3. Closed under multiplication. 

***Remark.***

​	If $\mathbb{W} \subseteq \mathbb{V}$ is a subspace, then $\mathbb{W}$ is a vector space (since it satisfies all the vector space axioms).



***Example.***

1. For any vector space, the zero subspace $\{0\}$ is usually denoted by $0$. Also, $\mathbb{V}$ is a subspace of itself. We call these two the "trivial subspaces". 
2. The space $C(\mathbb{R}, \mathbb{R}) \subseteq F(\mathbb{R}, \mathbb{R})$ ==(C stands for continuous)== is a subspace of the vector space $ F(\mathbb{R}, \mathbb{R})$ of all the functions $\mathbb{R}$ to $\mathbb{R}$. 
   1. $0: x \mapsto 0$ is a continuous (trivial).
   2. $f, g$ continuous $\Rightarrow f + g$ continuous.
   3. $f$ continuous, $\alpha \in \mathbb{R}$ $\Rightarrow  \alpha \cdot f$ continuous.
3. The space of polynomials of degree at most $n$ for some $n \in \mathbb{N}$. This is a subspace of the space of all polynomials.
   1. $0$-polynomial has degree $0 \leq n$.
   2. Scalar multiplication can only reduce the degree ==(scalar won't increase the degree of the polynomial so it is closed.)==
   3. Addition is obviously closed.
4. The space $\displaystyle \left\{\begin{bmatrix} x_1 \\ \vdots \\ x_n \end{bmatrix} \in \mathbb{F}^n : x_1 = 0\right\}$ is a subspace of $\mathbb{F}^n$ but $\displaystyle \left\{\begin{bmatrix} x_1 \\ \vdots \\ x_n \end{bmatrix} \in \mathbb{F}^n : x_1 = 1 \right\}$ is not. 