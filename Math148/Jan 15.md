# Jan 15

- ***Theorem***

  Suppose $f:[a,b] \rightarrow \mathbb{R}$ is bounded and continuous except at finitely many points, then $f$ is integrable. 

- ***Strategy***

  Suppose discontinuities are at $c_1 < c_2 < \cdots < c_t$. Recall that 

  $U(f,p) - L(f,p) = \sum_{i=1}^n (M_i-m_i)(t_i-t_{i-1})$ 

  -  Our old approach: $(M_i-m_i)$ is bounded because $f$ is bounded.
  - But now we have discontinuities, so we can't really find a $\mu$ to bound $(M_i - m_i)$. 
  - New strategy: when we can't control $(M_i - m_i)$, we need to control $(t_i - t_{i-1})$. 
  - We make the intervals containing $c_i$'s very very small.

- ***Set up***

  - Get points $r_1, r_2, \ldots, r_{2t}$ so that $c_j \in (r_{2j-1}, r_{2j})$ for each $j = 1$ to $t$. 
  - and $\sum_{j=1}^T (r_{2j}-r_{2j-1}) < \frac{epsilon}{4\sup|f|}$. 
  - We know $f$ is bounded so $\sup |f| = c < \infty$. 
  - Let $a=r_0, b = r_{2j+1}$, on each subinterval $[r_{2j}, r_{2j+1}]$ for $j = 1$ to $t$. 
  - Note that $f$ is continuous on each subinterval! (Because all the break points are contained in the set of $\{r_i\}$. 
  - Then for each of $[r_{2j},r_{2j+1}]$, we can find $\delta_j > 0$ so that if $x,y \in [r_{2j},r_{2j+1}]$ and $|x-y|<\delta_j$, then $|f(x)-f(y)| < \frac{\epsilon}{2(b-a)}$. 
  - Partition $[r_{2 j}, r_{2j+1}]$ into finitely many subintervals of length $\leq \delta_j$. 
  - Our partition of $[a,b]$ consists of all the $r_j$ and all the points we used to divide the intervals $[r_{2j},r_{2j+1}]$. The total number of partitions is finite! We call these (after further divided) points $\{t_i\} _{i=1}^N$. (We don't know how many there are)

- ***Computation***

  $U(f,p) - L(f,p) = \sum_{i=1}^N (M_i-m_i)(t_i-t_{i-1})$

  ​				$\displaystyle = \sum_{i \text{ where } [t_{i-1}, t_i] = [r_{2j-1}, r_{2j}]} (M_i-m_i)(t_i-t_{i-1}) + \sum_{\text{all other } i} (M_i-m_i)(t_i-t_{i-1})$ 

  - Note that the two parts are bounded for different reasons!

    - We controlled the first part by controlling $(t_i-t_{i-1}) $.
    - We controlled the second part by limiting $(M_i-m_i)$. 

  - Recall that $f$ is bounded, so $|f(x)| \leq sup|f| = c \Rightarrow -c \leq f(x) \leq c$. 

  - Part 1

    $\displaystyle = \sum_{i \text{ where } [t_{i-1}, t_i] = [r_{2j-1}, r_{2j}]} (M_i-m_i)(t_i-t_{i-1})  \leq \sum_{[t_{i-1}, t_i] = [r_{2j-1}, r_{2j}]} 2c(t_i-t_{i-1})​$ 

    $\displaystyle \leq \sum_{j=1}^t 2c(r_{2j}-r_{2j-1}) \leq 2c \cdot \frac{\epsilon}{4c} = \frac{\epsilon}{2}$. 

  - Part 2

    $ = \sum_{j=1}^t (\sum_{[t_{i-1}, t_i] \subset [r_{2j}, r_{2j+1}], t_i \text{partition} [r_{2j}, r_{2j+1}]} (M_i-m_i)(t_i-t_{i-1}) $ 

    Note that $\displaystyle M_i - m_i = \sup f|_{[t_{i-1}, t_i]} - \inf f|_{[t_{i-1},t_i]}$

    and since width $\leq \delta_j$ 

    the whole thing $\displaystyle \leq \frac{\epsilon}{2(b-a)}$. 

  - Think about this!!

- ***Measure Zero***

  - Say $E \subset \mathbb{R}$ has <u>measure zero</u> if $\forall \epsilon > 0$ there are countably many open intervals $I_j, j=1,2,3,\ldots$, such that $E \subset \cup_1^\infty I$, and $\sum_{j=1}^\infty \text{length} I_j \leq \epsilon, ie. $ $\sum_{j=1}^N \text{length} I_j \leq \epsilon \;\forall N)$. 
  - A set of points capable of being enclosed in intervals whose total length is arbitrarily small.



- ***Theorem***
  - A bounded function $f:[a,b]\rightarrow \mathbb{R}$ is integrable iff the set of discontinuities of $f$ has measure zero. 
  - Should be intuitive, consider how we proved the last theorem.
  - Monotonic, bounded functions have countable discontinuities, thus it is integrable. _Interesting connection here._

