# Chapter 4. Probability Rules and Conditional Probability.

---

## 4.1 General Methods

- ***Theorem.***Three rules

  - $P(S) = 1$ 

  - $\forall A \quad 0 \leq P(A) \leq 1$. 

  - $A \subset B \Rightarrow P(A) \leq P(B)$. 

    ​

- ***Definition.*** The complement of $A$ is denoted by $\bar{A}$.

- ***Theorem.*** Probability of the Complement of an Event

  - $P(A) = 1-P(\bar{A})$

  ​

- ***Theorem.*** De Morgan's Laws

  - $\overline{A \cup B} = \bar{A} \cap \bar{B}$
  - $\overline{A \cap B} = \bar{A} \cup \bar{B}$. 

  ​

---

## 4.2 Rules for Unions of Events

- ***Theorem.*** Sum Rule (Union)

  $\displaystyle P(A_1 \cup A_2 \cup \cdots \cup A_n) = \sum_i P(A_i) - \sum_{i<j}P(A_iA_j) + \sum_{i<j<k}P(A_iA_jA_k) - \sum_{i<j<k<l}P(A_iA_jA_kA_l) + \cdots	$

  ***Proof.*** When $n = 3$, you would do $P(A\cup B\cup C) = P(A) + P(B) + P(C) -P(AB) - P(BC) - P(AC) + P(ABC)$; now generalize this formula. 

  ​

- ***Definition.*** Events $A$ and $B$ are **mutually exclusive** if $A \cap B = \emptyset$.

- ***Theorem.*** Sum Rule (Mutually Exclusive Events)

  $P(A_1 \cup A_2 \cup \cdots \cup A_n) = \sum_{i=1}^n P(A_i)	$


****

## 4.3 Intersections of Events and Independence

- ***Definition.*** Events $A$ and $B$ are **independent events** iff $P(A\cap B) = P(A)P(B)$. If the events are not independent, we call the events **dependent**.
- ***Theorem.*** $A$ and $B$ are independent events iff $\bar{A}$ and $B$ are independent events. Similarly $A$ and $\bar{B}$ or $\bar{A}$ and $\bar{B}.$ 

---

## 4.4 Conditional Probability

- ***Theorem.*** The conditional probability of event $A$, given event $B$, is $\displaystyle P(A|B) = \frac{P(A\cap B)}{P(B)}$, provided $P(B) > 0$. 

- ***Remark.*** If $A$ and $B$ are independent, then $P(A\cap B) = P(A)P(B)$, so $\displaystyle P(A|B) = \frac{P(A)P(B)}{P(B)} = P(A)$, provided $P(B) > 0$. 

- ***Theorem.*** Suppose $A$ and $B$ are two events defined on $S$ such that $P(A) > 0$ and $P(B) > 0$. Then $A$ and $B$ are independent events iff either of the following statements is true:

  $P(A|B) = P(A) \quad or \quad P(B|A) = P(B)$. 

---

## 4.5 Product Rules, Law of Total Probability and Bayes' Theorem

- ***Theorem.  Product Rules.*** Let $A, B, C, D, \ldots$ be arbitrary events in a sample space. Assume that $P(A) > 0, P(A\cap B) > 0, P(A\cap B \cap C) > 0$. Then

  ​					$P(AB) = P(A)P(B|A)$

  ​					$P(ABC) = P(A)P(B|A)P(C|AB)$

  ​					$P(ABCD) = P(A)P(B|A)P(C|AB)P(D|ABC)$ 

  ​					$\ldots$ 

- ***Remark.*** In order to remember these rules you can imagine that the events to unfold in some chronological order, even if they do not. For example, $P(ABCD) = P(A)P(B|A)P(C|AB)P(D|ABC)$ could be interpreted as the probability that "$A$ occurs" and then "given $A$ occurs, that $B$ occurs", and etc.



- ***Theorem. Law of Total Probability. Part I.*** Let $A_1, A_2, \ldots, A_k$ be a partition of the sample space $S$ into disjoint (mutually exclusive) events, that is $A_1 \cup A_2 \cup \cdots \cup A_k = S$ and $A_i \cap A_j = \emptyset \text{  if  } i \ne j$.  Let $B$ be an arbitrary events in $S$. Then 

  ​			$\displaystyle P(B) = P(BA_1) + P(BA_2) + \cdots + P(BA_k) = \sum_{i=1}^k P(B|A_i)P(A_i)$. 

- ***Proof.*** Since all events $BA_i$ are mutually exclusive and their union is $B$, that is, $B = (BA_1) \cup \cdots \cup (BA_k)$. Therefore by the addition rule $P(B) = P(BA_1) + P(BA_2) + \cdots + P(BA_k)$. By the product rule, $P(BA_i) = P(B|A_i)P(A)i)$. Thus $\displaystyle P(B) = P(B|A_1)P(A_1) + P(B|A_2)P(A_2) + \cdots + P(B|A_k)P(A_k) = \sum_{i=1}^k P(B|A_i)P(A_i)$. 

- ***Theorem.*** Suppose $A$ and $B$ are events defined on a sample space $S$. Suppose also that $P(B) > 0$. Then

  ​		$\displaystyle P(A|B) = \frac{P(B|A)P(A)}{P(B)} = \frac{P(B|A)P(A)}{P(B|\bar{A})P(\bar{A}) + P(B|A)P(A)}$. 

---

## 4.6 Useful Series and Sums

- ***Binomial Theorem, V2***

  ​								$\displaystyle (1+t)^n = \sum_{x=0}^\infty \binom{n}{x} t^x \; \text{if} \; |t|<1$. 



- ***Exponential Series***

  ​									$\displaystyle e^t = \sum_{x=0}^\infty \frac{t^n}{n!}, \forall t \in \mathbb{R}$. 

  ​									$\displaystyle e^t = \lim_{n\to\infty} \left( 1 + \frac{t}{n}\right) ^n$ 

---

The End

Version 1.0

Jan-01-21 David Duan