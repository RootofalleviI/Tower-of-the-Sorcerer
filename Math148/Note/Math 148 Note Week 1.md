# Math 148 Note Week 1

## Area under a Curve

- Consider a bounded function $  f:[a,b] \rightarrow \mathbb{R}$. We know this function is bounded because of the **Extreme Value Theorem**. Let $P$ denotes a partition of $  [a,b]$:

  ​					$$  P : a = t_0 < t_1 < \cdots < t_n = b$$

  This partition divides $ [a,b]$ into subintervals $ [t_{i-1}, t_i], 1 \leq i \leq n$.

  ​

- Let $M, m$ be the supremum and infimum, ie. 

  ​					$$  M_i = sup\{f(x): x \in [t_{i-1}, t_i]\}$$

  ​					$$  m_i = inf\{f(x): x \in [t_{i-1}, t_i]\}$$

  ​

- By the **Extreme Value Theorem**, if $  f$ is continuous, then there exists $  c_i, d_i \in [t_{i-1}, t_i]$ such that $  M_i = f(c_i), m_i = f(d_i)$.
---
## Upper Riemann Sum and Lower Riemann Sum
- ***Formula.***

  ​					$$U(f,p) = \sum_{i=1}^n M_i(t_i - t_{i-1})$$

  ​					$$  L(f,p) = \sum_{i=1}^n m_i(t_i - t_{i-1})$$

  - The value of these two functions depend on the function $  f$ and also the partition $  p$.
  - $  M_i$ and $  m_i$ is the local max/min on the interval $  [t_{i-1}, t_i]$; they are the "height" of the function.
  - Multiplying $  M_i$ and $  m_i$ with the "width" $(t_i - t_{i-1})$, we get a bunch of areas of rectangles. 
  - Taking the sum of all the rectangles, we get an approximation of the area under the curve.

- Note that URS is always an over-estimate; LRS is always an under-estimate. That is,

  ​					$$  \text{LRS} \leq \text{"Area"} \leq \text{URS}$$

  ​					$$  L(f,p) \leq \int_a^b f(x)dx \text{ (if exists)} \leq U(f,p)$$
---
## Refinement
- ***Definition.*** A refinement of partition $  p$ is a partition $  Q$ which contains all the points of $  p$ (and more).

- ***Remark.*** The subintervals don't have to be evenly spaced.

  ​


- *Now what would happen if we use a refined partition to $  L(f,p)$ and $  U(f,0)$?*
  - Since refinement makes $  L(f,p)$ and $  U(f,p)$ better approximations of the actual area, we have the following inequalities:
    ​				$$  U(f,q) \leq U(f,p)$$
    ​				$$  L(f,q) \geq L(f,p)$$
    That is, URS would fall and LRS would rise. 

    ​

- ***Observation.*** Let $  p_i, p_j$ be two partitions of $  [a,b]$. Let $  Q$ be the common refinement of $  p_i, p_j$, ie. $  Q = p_i \cup p_j$. Then we have 

  ​					$$  L(f,p_i) \leq L(f, Q) \leq U(f, Q) \leq U(f, p_j), \quad \forall i, j \in \cup \text{partitions}$$

  Hence, any URS is bounded below by any LRS. From this, we can conclude that 

  ​					$$  I = \inf\{U(f,p)\;|\;\text{all partition of } [a,b] \text{ exists}\}$$
  ​					$$  S = \sup\{L(f,p)\;|\;\text{all partition of } [a,b] \text{ exists}\}$$

  Moreover, 				

  ​	$$  S = \sup\{L(f,p):\text{all partitions }p\} \leq \int_a^b f(x)dx \leq \inf \{U(f,p):\text{all partitions } p\} = I$$

  Thus, if $  S = I$, we have $  S = \int_a^bf(x)dx = I$.

  ​

- ***Definition.*** We say $  f:[a,b] \rightarrow \mathbb{R}$ is integrable over $  [a,b]$ if $$  S = \sup \{L(f,p)\;|\;\text{all } p\} = \inf \{U(f,p)\;|\;\text{all } p\} = I.$$
  We write $  \int_a^b f = I = S$. When $  f$ is positive and continuous, $  \int_a^b f$ is the area under $  f$ over $ [a,b]$

- ***Definition.*** We define the area under $  f$ over $  [a,b]$ for $  f \geq 0$ as $  \int_a^b f$, provided that $  f$ is integrable.
---
## Riemann Sum
- Given any partition $  p$ of $  [a,b]$, say $  p: a = t_0 < \cdots < t_n = b$. Pick $  c_i \in [t_{i-1}, t_i]$, then 

  ​					$$  R(f,p) = \sum_{i=1}^n f(c_i)(t_i-t_{i-1}).$$

  Note that $  L \leq R \leq U$ since $  m_i \leq f(c_i) \leq M_i$.

- Moreover, if $  f$ is continuous, there exists a choice of $  c_i \in [t_{i-1}, t_i]$ such that $  M = f(c_i)$ and $  m = f(c_i')$ 
---
## Characterization Theorem
- ***Theorem.*** Suppose $  f:[a,b] \rightarrow \mathbb{R}$ is bounded. Then $  f$ is integrable iff for all $  \epsilon > 0$ there exists a partition $  p^*$ such that $  U(f,p^*) - L(f,p^*) < \epsilon$.

  ​

- ***Proof.*** 
  - Assume for each $  \epsilon > 0$ there exists a partition $  p_\epsilon$ such that $  U(f,p_\epsilon)-L(f,p_\epsilon) < \epsilon$. We want to show that $  I = S$. Since

    ​		$$  I = \inf\{U(f,p)\;|\;\text{all }p\} \leq U(f,p_\epsilon), \;S = \sup\{L(f,p)\;|\;\text{all }p\} \geq L(f,p_\epsilon),$$

    we have 
    ​		$$  I - S \leq U(f,p_\epsilon) - L(f,p_\epsilon) < \epsilon.$$

    This is true for all $ \epsilon$, thus $  I = S$, and $  f$ is integrable.

  - Now assume that $  f$ is integrable. Let $  \epsilon > 0$. We know (given) $  I = S$.

    ​		$$  I = \inf\{U(f,p)\;|\;\text{all }p\}, \; S = \sup\{L(f,p)\;|\;\text{all }p\}.$$

    Uses the definition of supremum and infimum, pick $  p_1$ such that $  I \leq U(f,p_1) < I+\epsilon/2$ and $  p_2$ such that $  S - \epsilon/2 < L(f,p_2) \leq S$. But $  I = S$,so 

    ​		$$  I - \frac{\epsilon}{2} < L(f,p_2) \leq I \leq U(f,p_1) < I + \frac{\epsilon}{2}.$$

    Let $  p$ be the common refinement for $  p_1, p_2$. Then 

    ​		$$  U(f,p) - L(f,p) \leq U(f,p_1) - L(f,p_2) < \epsilon.$$

    ​

- ***Application***.
  - Show that $  f(x) = x^2 $ on $  [0,1]$.

  - ***Proof.*** Apply the above theorem.

    - Let $  \epsilon > 0$. Choose $ n\in \mathbb{N} $ such that $\frac{1}{n} < \epsilon$. Let $P_n := 0 = t_0 < t_1 < \cdots < t_{n-1} < t_n = 1$ where $t_i = \frac{i}{n}$. 

    - Then $M_i = f(t_i) = (\frac{i}{n})^2$, $m_i = f(t_{i-1}) =(\frac{i-1}{n})^2$ .

      - Then $$\displaystyle U(f, P_n) = \sum_{i=1}^n M_i(t_i-t_{i-1}) = \sum_{i=1}^n (\frac{i}{n})^2 (\frac{i}{n}) = \frac{1}{n^3}\sum_{i=1}^ni^2 = \frac{1}{n^3}\cdot \frac{n(n+1)(2n+1)}{6}$$ 

      $$\displaystyle L(f, P_n) = \sum_{i=1}^n m_i(t_i-t_{i-1}) = \sum_{i=1}^n (\frac{i-1}{n})^2 (\frac{i}{n}) = \frac{1}{n^3}\sum_{i=1}^{n-1}i^2 = \frac{1}{n^3}\cdot \frac{(n-1)n(2n-1)}{6}$$

    - Then 

      $$\displaystyle U(f,P_n) - L(f,P_n) = \frac{(n+1)(2n+1)-(n-1)(2n-1)}{6n^2} = \frac{1}{n} < \epsilon$$ 

    - By the characterization theorem, $f(x) = x^2$ is integrable.

---

## Uniform Continuity

- ***Definition.*** Continuity.

  Let $E$ be a nonempty subset of $\mathbb{R}$ and $f:E\rightarrow \mathbb{R}$.  Then $f$ is said to be _**continuous**_ at a point $a \in E$ if and only if 

  ​		$$\forall \epsilon > 0 \;\exists \delta > 0 \;st.\; |x-a| < \delta \land x \in E  \Rightarrow |f(x)-f(a)| < \epsilon$$

- ***Definition.*** Uniform continuity.

  Let $E$ be a nonempty subset of $\mathbb{R}$ and $f : E \rightarrow \mathbb{R}$. Then $f$ is said to be _**uniformly continuous**_ on $E$ if and only if   

  ​		$$ \forall \epsilon > 0 \; \exists \delta > 0 \; st. \; |u-v| < \delta \land u,v \in E \Rightarrow |f(u)-f(v)| < \epsilon$$ 

- **_Remark_**. Difference between continuity and uniform continuity.

  - Continuity is about a point $a$, such that all points around $a$ behave nicely.
  - Uniform continuity is about every two points in the domain, as long as they satisfy the condition $|u-v| < \delta$.

### Prove that $f(x) = x^2$ is not uniformly continuous.

-  **_Proof._**  Let $\epsilon =1$. Suppose we can find a $\delta$ that works. Consider $x = a, y = a + \frac{\delta}{2}$. $|x-y| < \frac{\delta}{2}$, but $|f(x)-f(y)| = |a^2-a^2-a\delta + \frac{\delta^2}{4}|$. Thus $a \rightarrow \infty \Rightarrow |f(x)-f(y)| > \epsilon$. 

### Prove that $f(x) = \frac{1}{x}$ is not uniformly continuous on $(0, \infty)$. 

- **_Proof._** Let $\epsilon = 1.$ Suppose we can find $\delta$ that works. Let $x = \frac{1}{N}, y=\frac{1}{2N}$, then $|x-y|<\frac{1}{2N} < \delta$ given that $N$ is big enough. But $|f(x)-f(y)| = |\frac{1}{x} - \frac{1}{y}| = |N - 2N| = N > 1 = \epsilon$. 

### Prove if $f(a,b) \rightarrow \mathbb{R}$ and $f'$ is bounded, then $f$ is uniformly continuous.

- _**Proof**_. Since $f'$ is bounded, pick $\mu$ such that $|f'(x)| \leq c$ for all $x\in(a,b)$. Let $\epsilon > 0$. Take $\delta = \frac{\epsilon}{\mu}$. Then if $x,y \in (a,b)$, by **_Mean Value Theorem_** $ \displaystyle \left|\frac{f(x) - f(y)}{x-y}\right| = |f'(t)| \leq \mu$ for $t \in [x, y]$. Rewriting this, we have $|f(x) - f(y)| \leq \mu|x-y|$. Then $|x-y|<\delta = \frac{\epsilon}{\mu} \Rightarrow |f(x)-f(y)| < \epsilon$. 

### Prove if $f[a,b] \rightarrow \mathbb{R}$ is continuous, then $f$ is uniformly continuous.

- **_Proof._** 
  - Suppose false. Let $\epsilon > 0$, then $\delta_\epsilon$ does not exist (fails to exist). That is, $\forall \delta > 0 \; \exists x, y \in dom f \;st\; |x-y|<\delta \rightarrow |f(x)-f(y)| \geq \epsilon$. Think about $\delta = \frac{1}{n}, \; n\in \mathbb{N}$. 
  - For all $n \in \mathbb{N}$, there exists $x_n, y_n \in \text{dom } f = [a,b] \;st.\; |x_n - y_n| < \frac{1}{n}$, but $|f(x_n)-f(y_n)| \geq \epsilon$. 
  - Take sequences $(x_n), (y_n)_{n=1}^\infty \in [a,b]^\mathbb{N}$ (they are bounded sequences), by **_BWT_**, there exists a subsequence $(x_{n_k})$ which converges to $x_0 \in [a,b] = \text{dom } f$. 
  - For $(y_n)_{n=1}^\infty$, $x_n-\frac{1}{n} < y_n < x_n+\frac{1}{n}$ for all $n \in \mathbb{N}$. Then $x_{n_k}-\frac{1}{n_k} < y_{n_k} < x_{n_k}+\frac{1}{n_k}$. By **_SQZ_** $(y_{n_k})_{k=1}^\infty$ converges to $x_0$.
  - Now $f$ is continuous at $x_0$. Since $(x_{n_k}) \rightarrow x_0$, $f(x_{n_k}) \rightarrow f(x_0)$. Similarly, $(y_{n_k}) \rightarrow x_0 \Rightarrow f(y_{n_k}) \rightarrow f(x_0)$. Thus $|f(x_{n_k}) - f(y_{n_k})| = 0$.
  - But $|f(x_{n_k}) - f(y_{n_k})| \geq \epsilon$ for all $k$. This is a contradiction. QED.

---

### Bounded, Continuous Functions are Integrable.

- **_Theorem._** If $f:[a,b]\rightarrow \mathbb{R}$ is continuous (it's automatically bounded by **_EVT_**, and note that integrability only makes sense if $f$ is bounded.), then $f$ is integrable.

- _**Strategy:**_ Show that for all $\epsilon > 0$ there exists partition $p$ such that $U(f,p) - L(f,p) < \epsilon$.

  - Let $p$ be a partition, $a = t_0 < \cdots < t_n = b$. 
  - Let $M_i = \sup f|_{[t_{i-1}, ti]} = \max f|_{[t_{i-1}, ti]} = f(c_i)$ and $m_i = \inf f|_{[t_{i-1}, ti]} = \min f|_{[t_{i-1}, ti]} = f(d_i).$ We know they are attained because of continuity and **_EVT_**. 
  - Then $U(f,p) - L(f,p) = \sum_{i=1}^n M_i(t_i - t_{i-1}) - \sum_{i=1}^n m_i(t_i-t_{i-1}) = \sum_{i=1}^n(M_i - m_i)(t_i-t_{i-1})$
  - We know $(t_i - t_{i-1})$ is a fixed value, and we can control $M_i$ and $m_i$ using uniform continuity, so we can make this sum less than $\epsilon$. 

- **_Proof._** Let $\epsilon > 0$.

  - By the above theorem, $f$ is continuous on $[a,b]$ implies it's uniformly continuous on $[a,b]$. That is, $\displaystyle \forall \epsilon \; \exists \delta \;st\; x, y \in [a,b] \land |x-y| < \delta \Rightarrow |f(x)-f(y)| < \frac{\epsilon}{b-a}$ (we deliberately choose the value $\displaystyle \frac{\epsilon}{b-a}$). 

  - Take any partition $p$ of $[a,b]$, $p : a = t_0 < \cdots < t_n = b$ with the property that the length of each subinterval $|t_i - t_{i-1}| < \delta$. 

  - Now $M_i = \sup f|_{[t_{i-1}, ti]} = \max f|_{[t_{i-1}, ti]} = f(c_i)$ for some $c_i \in [t_{i-1}, t_i]$, $m_i = \inf f|_{[t_{i-1}, ti]} = \min f|_{[t_{i-1}, ti]} = f(d_i)$ for some $d_i \in [t_{i-1}, t_i]$, hence $|c_i - d_i| \leq t_i - t_{i-1} < \delta$. Therefore $\displaystyle |f(c_i) - f(d_i)| < \frac{\epsilon}{b-a}$. 

  - So, 

    $$\displaystyle U(f,p) - L(f,p) \;= \sum_{i=1}^n (M_i - m_i) (t_i - t_{i-1}) $$

    ​		        	$$\displaystyle < \sum_{i=1}^n \frac{\epsilon}{b-a} (t_i - t_{i-1})$$

    ​				$$= \displaystyle \frac{\epsilon}{b-a} \cdot (b-a) = \epsilon$$ 

  - Hence it is integrable. 

---

### Bounded and Monotonic Functions are Integrable.

- **_Theorem._** If $f:[a,b] \rightarrow \mathbb{R}$ is monotonic, then it's integrable.

- _**Proof.**_ 

  - Note that $f$ is bounded by EVT. We prove the case that $f$ is increasing.

  - Let $\epsilon > 0$, take a uniform partition $p_n : a = t_0 < \cdots < t_n$, where $t_j = a + j(\frac{b-a}{n})$. 

  - Since $f$ is increasing, for each interval $[t_{i-1}, t_i]$, $M_i = f(t_i), m_i = f(t_{i-1})$. 

  - Then 

    $$\displaystyle U(f,p) - L(f,p) \;= \sum_{i=1}^n (M_i - m_i) (t_i - t_{i-1}) $$

    ​				$\displaystyle = \frac{b-a}{n} \sum_{i=1}^n f(t_i) - f(t_{i-1})$ -- Note that this is a telescoping sum!

     				$\displaystyle = \frac{b-a}{n} \cdot (f(t_n) - f(t_0))$

    ​				$\displaystyle = \frac{b-a}{n} \cdot (f(b) - f(a))$ 

    ​				$\displaystyle = \frac{c}{n}$ -- where $c$ is some constant.

  - Pick $n$ such that $\displaystyle \frac{c}{n} < \epsilon$.  Then $\displaystyle U(f,p) - L(f,p) = \frac{c}{n} < \epsilon$. Hence $f$ is integrable. 


---

V1.0, 2018-01-14



