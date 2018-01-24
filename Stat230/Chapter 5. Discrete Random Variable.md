## Chapter 5. Discrete Random Variable

---

## 5.1 Random Variables and Probability Functions

***Remark.*** A **random variable** is a numerical-valued variable that represents outcomes in an experiment or random process. Associated with any random variable is a **range** $A$, which is the set of possible values for the variable. Random variables are always defined for every outcome of the random experiment, that is, for every outcome $a \in S$. For each possible value $x$ of the random variable $X$, there is a corresponding set of outcomes $a$ in the sample space $S$ which results in this value of $x$ (that is, so that $X = x$ occurs). 

***Definition.*** A **random variable** is a function that assigns a real number to each point in a sample space $S$. 

***Definition.*** **Discrete random variables** take integer values or, more generally, values in a countable set. 

***Definition.*** **Continuous random variables** take values in some interval of real numbers. 



***Definition.*** Let $X$ be a discrete random variable with $range(X) = A$. The **probability function** of $X$ is the function $f(x) = P(X = x)$, defined for all $x \in A$. The set of pairs $\{(x, f(x)):x \in A\}$ is called the **probability distribution** of $X$. All probability functions must have two properties, which are $f(x) \geq 0 \; \forall x\in A$, and $\sum_{\text{all }x \in A} f(x) = 1$. By implication, these properties ensure that $f(x) \leq 1$ for all $x$. 

***Definition.*** The **cumulative distribution function** of $X$ is the function usually denoted by $F(x) = P(X \leq x)$, defined for all $x \in \mathbb{R}$. A cumulative distribution function has the following properties: 

- $F(x)$ is non-decreasing for all $x \in \mathbb{R}$
- $0 \leq F(x) \leq 1, \; \forall x \in \mathbb{R}$
- $\lim_{x\to-\infty}F(x) = 0$ and $\lim_{x\to\infty}F(x) = 1$
- $F(x) = P(X \leq x) = \sum_{u \leq x} f(u)$
- If $X$ takes on integer values then for values $x$ such that $x \in A$ and $x - 1\in A$, $f(x) = F(x) - F(x-1)$. 