# Stat 230 - Week 1

### Course Info
- Weekly quiz/assignment due Wednesday midnight
- Grade breakdown
	- Quizzes (9 * 1% = 9%)
	- Assignments (3 * 3.33% = 10%)
	- Piazza (6%)
	- Midterm (15%)
	- Final (60%)

***
### Week 1
##### Learning Outcomes
1. Define a probability model and dtermine probabilities of events using counting techniques
2. Solve problems about probability and samples spcaes from chapter 1 and 2 of the course ntoes.
<br>
---
##### What is Probability?
- A strong likelihood of chance of something;
- The relative possibility an event will occur;
- The ratio of the number of actual occurrences to the total number of possible occurrences.

**Remark**. In this course, we will consider experiements that have several possible outcomes and are repeatable.
**Remark.** Among the three definitions listed below, the classical definition and the relative frequency definition are consistent with one another if we are careful in constructing our model.
<br>
###### Definition. _Classical Definition of Probability_
Let $S$ be the set of all possible distinct outcomes of a random experiment. Then the probability of an _event_ is 
$$ \frac{\text{Number of ways the event can occur}}{\text{Total number of outcomes in } S}$$

**Example.** The probability of rolling an even number in one row of a fair die is 3/6: there are three possible ways for the event to occur: {1, 2, 3}, and total sample space:{1, 2, 3, 4, 5, 6}
<br>
######Definition. _Relative Frequency Definition_
The probability of an event in an experiment is the (limiting) proportion or fraction of times the event occurs in a very long (theoretically infinite) series of (independent) repetitions of the experiment. 

**Example.** If a coin is tossed 10000 times, and heads appears 4992 times, then the probability of heads equals 0.4992.
<br>
######Definition. _Subjective Probability_
The probability of an event is a "best guess" by a person making the statement of the chances that the event will happen.
<br>
---
##### Mathematical Models in Probability
###### What characteristics does a *random* experiment have?
1. It should have more than one possible outcome.
2. We should be able to repeat the experiement under similar conditions.
3. It may (or may not) have equally likely outcomes.

###### What is a probability model?
1. A _sample space_ of all possible outcomes of a random experiment must be defined.
2. A set of _events_ is defined. An event is a subset of hte sample space, to which we can assign a probability.
3. A way of _assigning probabilities_, which are numbers between 0 and 1, to events is specified.
<br>
---
#####Random Experiements and Sample Spaces
######Definition. _Random Experiement_
When we repeat the experiment under _controlled conditions_ (repetitions are called **trials** of the experiment) different outcomes may occur.
######What properties does it have?
- We should be able to repeat it.
- Different outcomes may occur on different trials.
- Outcomes have probabilities associated with them.

######Definition. _Sample Space_
A sample space, $S$, is the set of distinct outcomes for an experiments or process, with the property that in a single trial, one and only one of these outcomes occur. The outcomes in a sample sapce are called _sample points_, or _points_.

######Definition. _Discrete Sample Spaces_
A **discrete sample space**, $S$, is one with a **finite** number of sample points or **countably many** sample points.
<br>
---
#####Definition of an Event
######Definition. _Event_
An event, $A$, defined on a discrete sample space, $S$, is a subset of $S$.

######Definition. _Simple Event_
If the event $A\subset S$ consists of only one sample point then A is acalled a **simple event**.

######Definition. _Compound Event_
If the event $A\subset S$ consists of two or more sample points then $A$ is called a **compound event**. $A$ is said to **occur** on a trial of the experiment if one of the simple events in $A$ occurs.
<br>
---
##### Probability Distributions
######Definition. _Probability Distribution on $S$
Let $S = \{a_1, a_2, a_3, ...\}$ be a discrete sample space.
Let $P(a_1), P(a_2), P(a_3), ...$ be a set of numbers associated with the sample points $a_1, a_2, a_3, ...$ such that:
1. $0 \leq P(a_i) \leq 1, i = 1, 2, ...$
2. $\sum_{i=1}P(a_i) = 1$  

Then $P(a_i)$ is called a probability.
The set $\{P(a_i), i=1,2, ...\}$ is called a probability distribution on $S$. 
The events consisting of a single point $a_i$ in the sample space are referred to as **Simple Events**.
<br>
---
#####Probability of an Event
######Definition. _Probability of an Event_
Let $S$ be a discrete sample space.
Let $A$ be an event defined on $S$, i.e. $A\subset S$.
Then $P(a)$, the probability of the event $A$, is the sum of the probabilities corresponding to all the simple events that are in $A$, that is, $P(A) = \sum_{a\in A}P(a)$.

Recall that events consisting of a two or more points such as $A = {a_1, a_2, a_3}$, are referred to as Compound Events. According to the definition above, the probability of $A$ is $P(A) = P(a_1) + P(a_2) + P(a_3)$.
<br>
---
#####Probability Models: Discrete Case
######Definition. _Discrete Probability Model_
A discrete sample space $S = {a_1, a_2, \ldots}$ together with a probability distribution $\{P(a_i), i = 1, 2, \ldots\}$ is referred to as a **discrete probability model**.

<br>
---
####Equally Likely Outcomes
Suppose we have a finite sample space $S = \{a_1, a_2, ..., a_N\}$, where $N < \infty$, with probability distribution on $S$ given by $P(a_i) = \frac{1}{N}, i = 1, \ldots, N$ so that all $N$ outcomes are equally probable.

######Definition. $P(A) for equi-probable outcomes
When all simple events have the same probability, then 
$$P(A) = \frac{|A|}{N}, \forall A\subset S, |A| = \text{size of }A$$

######Definition. Addition Rule
Suppose we can do job 1 in $p$ ways and job 2 in $q$ ways. Then we can do either job 1 **OR** job 2 (but not both) in $p + q$ ways.

######Definition. Multiplication Rule
Suppose we can do job 1 in $p$ ways and, for each of these ways, we can do job 2 in $q$ ways. Then we can do both job 1 **AND** job 2 in $p \times q$ distinct ways.

##### Some useful Combinatorical Symbols
- $n^{(k)} = n \times (n-1) \times \cdots \times (n-k+1) = \frac{n!}{(n-k)!}$
	- $n$ to $k$ factors
	- number of arrangements of $n$ different elements taken $k$ at a time.
- $n!$ 
	- $n$ factorial
	- number of arrangements (permutations) of $n$ different elements taken $n$ at a time.
- $n^k$
	- $n$ to the power $k$
	- number of arrangements of $n$ elements taken $k$ at a time allowing repeats. 
- $\displaystyle\binom{n}{k} = \frac{n^{(k)}}{k!}$
	- If $n \in \mathbb{N}, k \in \mathbb{Z}^+, k \leq n$, then $\binom{n}{k}$ is the number of subsets (combinations) of $k$ elements which may be selected from a set containing $n$ elements.









