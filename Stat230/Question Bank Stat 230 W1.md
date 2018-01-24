# Question Bank Stat 230

---

## Week 1.

#### Easy

1. ***Question.*** Given digits 3~8, find the probability that the first digit is 6 and the last digit is 3.

   ***Answer.*** Total permutation = $6!$, the middle 4 numbers have $4!$ permutations, so the total number of permutation is $\displaystyle \frac{4!}{6!}=\frac{1}{30}$. 

   ​

2. ***Question.*** Suppose you hold one of the 100 tickets in a lottery. There are 5 prizes altogether. Assume the draws are without replacement. Find the probability that you win a prize. 

   ***Answer.*** There are 5 winning tickets and 100 tickets in total, thus your probability of winning is $\displaystyle \frac{5}{100} = 0.05%$.

   ​

3. ***Question.*** Find the probability that the letters INDEPENDENT spell INDEPENDENT when they are arranged in a row at random.

   ***Answer.*** Use the formula. Answer is $\displaystyle \frac{3!3!2!}{11!}$. 

   ​

4. ***Question.*** A probability experiment has two steps. There are two possible results for the first step, each of them has 4 and 12 possible results for the second step, respectively. How many possible outcomes are there for this experiment?

   ***Answer.*** $4 + 12 = 16$.

   ​

5. ***Question.*** Evaluate $S = 1 + x + x^2 + x^3 + \cdots + x^n$, given that $-1 < x < 1, x \in \mathbb{R}$. 

   ***Answer.*** $\displaystyle \frac{(1-x^{n+1})}{(1-x)}$ .

   ​

6. ***Question.*** Evaluate $S = 1 + x + x^2 + x^3 + \cdots$, given that $-1 < x < 1, x \in \mathbb{R}$. 

   ***Answer.*** $\displaystyle \frac{1}{1-x}$. 

   ​

7. ***Question.*** Consider the numbers $\{7, 9, 3, 6, 13\}$. How many ways can I order them if I want the start of the sequence be a non-prime?

   ***Answer.*** We have 2 primes, and we can order the rest of the four numbers in $4!$ ways. Thus the answer is $2 * 4! = 48$. 

   ​

8. ***Question.*** Box A contains numbers 1~4; B contains 8~11. Draw one number from each box and both of them are even. How many possible outcomes are there?

   ***Answer.*** $2 \times 2 = 4$. 

   ​

9. ***Question.*** How many different pairs of people can you select from a group of 10 peoples, if the order of selection does not matter? 

   ***Answer.*** Order does matter means it's $_nC_r$. Thus $_{10}C_2 = 45$. 

   ​

10. ***Question.*** How many different pairs of people can you select from a group of 8 persons, if the order of selection does matter?

  ***Answer.*** Order does matter means it's $_nP_r$. Thus $_8P_2 = 56$. 

  ​

#### Medium

1. ***Question.*** Given numbers 1~9, if the digits are randomly arranged in a row, find the probability that the even numbers occur consecutively. 

   ***Answer.*** 

    - Total permutations: $9!$
   - Six possible positions for the even numbers to be in.
   - The four even digits can be permutated in $4!$ different ways and the five odd digits can be permutated in $5!$ different way. 
   - Hence the answer is $\displaystyle \frac{6 \times 4! \times 5!}{9!} = \frac{1}{21}$.

   ​

2. ***Question.*** How many 8-letter words can be formed using an alphabet containing 25 letters? Hint: there is no restriction on how many times a letter may be used in forming a word.

   ***Answer.*** There will be 8 spots and each spot has 25 choices, thus the answer is $25^8$ choices.

   ​

3. ***Question.*** How many numbers are there between 100 and 999 such that at least one of their digits is 1?

   ***Answer.*** There are 900 numbers in total, first count the number of 3-digit numbers that do not have 1 as one of their digits:

    - The rightmost digit can be 0 and 2~8, so 9 choices.

    - The middle digit can be 0 and 2~8, so 9 choices.

    - The leftmost digit can be 2~8, so 8 choices.

    - Overall there are $8 \times 9 \times 9 = 648$ choices. Subtracting 648 from 900 yields 252 as the answer.

      ​

4. ***Question.*** Suppose 11 passengers board a train at A. On its way to B the train will make stops on 6 different stations (A = 0 $\Rightarrow$ 1 $\Rightarrow \cdots \Rightarrow$ 6 = B) where passengers may get off. How many different ways can the passengers disembark?

   ***Answer.*** There are 11 spots and each spot has 6 choices, so the answer is $6 \times 6 \times \cdots 6 = 6^{11}$. 

   ​

5. ***Question.*** Suppose 5 families of 2 people get together. If one representative from each family gives a gift to everyone at the party except people from their own family, how many gifts are given? 

   ***Answer***. Each of the 5 family representatives gives 2 presents to 4 other families. So $5 \times 2 \times 4 = 40$. 

   ​

   ​

#### Hard

1. ***Question.*** We want to hire people from 5 second-years, 3 third-years and 3 fourth-years. Policy is to always hire at least one third year and one fourth year student. Other than that as many students as are needed can be hired without restriction. How many different ways can a group of students be hired to work?

   ***Answer.*** For any set of $n$ students, the number of ways we can select a subset of any size is $2^n$ (to myself: think of this as the **power set** of the set). Another way to interpret this is that, for each student we have two choices: hire or don't hire. That is, there are two actions with the first student, two with the second, etc. If in addition we impose the restraint that at least one student from the group must be selected, then the possibility that we hire 0 got removed, ie. one possibility removed and our result becomes $2^n - 1$. Hence, the answer is $2^5\times (2^3-1) \times (2^3-1) = 1568$. 

---

## Week 2.

#### Easy

1. ***Question.*** The probability of a randomly selected sample begin in class $A, B, C$, or $D$ is $0.25, 0.25, 0.35,$ and $0.15$, respectively. If a sample is selected at random, what is the probability it is in class $A$ given that it is not in class $D$?

   ***Answer.*** 

   ​	$\displaystyle P(A|\neg D) = \frac{P(A \cap \neg D)}{P(\neg D)} = \frac{P(A)}{P(\neg D)} = \frac{0.25}{0.85} = 0.294$.

   ​

2. ***Question.*** Which of the following are probability functions?

   ***Answer.*** Check two things: 1. $0 \leq f(x) \leq 1, \forall x$, and $\sum f(x) = 1$. 

   ​



3. Let $X$ be a random variable which takes on integer values, and suppose $a$ and $b$ are possible values. Then $a < b \Rightarrow P(X\leq a) \leq P(X \leq b)$.

   ​



4. ***Question.*** 20 balls are randomly placed in 8 baskets numbered 1 through 8. What is the probability that the last ball is put in basket 6?

   ***Answer.*** 1/8.

   ​



5. ***Question.*** 1 out of 1000 births results in fraternal twins; 1 out of 1500 births results in identical twins. Identical twins must be the same sex but the sexes of fraternal twins are independent and we assume each sex the probability is 0.5. If two girls are twins, what is the probability they are fraternal twins?

   ***Answer.*** $\displaystyle P(\text{fraternal}|\text{both girl}) = \frac{P(\text{fraternal} \cap \text{both girl})}{P(\text{both girl})} = \frac{1/1000 \cdot 0.25}{1/1000 \cdot 0.25 + 1/1500 \cdot 0.5} = 0.4585.$

   ​



6. ***Question.*** Three independent events have probability 1/4, 1/3, and 1/2. What is the probability exactly one will occur?

   ***Answer.*** $P(\text{exactly one occurs}) = \frac{1}{4} \cdot (1 - \frac{1}{3}) \cdot (1 - \frac{1}{2}) + \frac{1}{3} \cdot(1-\frac{1}{4})\cdot(1-\frac{1}{2}) + \frac{1}{2}\cdot(1-\frac{1}{4})\cdot (1-\frac{1}{3}) = 0.4583.$



7. For a random variable with cumulative distribution function $F(x)$, $P(X>21) = 1 - F(21)$. 



8. Let $X$ be a random variable which takes on integer values, and suppose $a$ and $b$ are possible values of $X$. Then the statement $P(X \leq a) \leq P(X \leq b) \Rightarrow a < b$ is false. Consider $a = b$. 



9. ***Question.*** 7 students are each picking one course from a list of 10 courses. What is the probability they all pick different courses? assume students choose courses independently of each other.

   ***Answer.*** There are $10^7$ ways for the students to select courses. There are $10^{(7)}$ ways for the students to select different courses. Then the answer is $\displaystyle \frac{10^{(7)}}{10^7}$. 

#### Medium

1. ***Question.*** Binary digits, ie. $0$'s and $1$'s, are sent down a noisy communication channel. They are received as sent with probability $0.9$ but errors occur with probability $0.1$. Assuming that it's equally likely to send $0$'s and $1$'s, what is the probability that a $1$ was sent given that we received a $1$? 

   ***Answer.*** There are four cases: send 1 and receive 1 (0.45), send 1 and receive 0 (0.05), send 0 and receive 0 (0.45), send 0 and receive 1 (0.05). Now given that we received a 1, we have narrowed down our denominator to only case 1 and case 4. That is, 

   ​			$\displaystyle P(\text{send } 1| \text{receive } 1) = \frac{P(\text{send } 1 \cap \text{receive } 1)}{P(\text{receive } 1)} = \frac{0.45}{0.5} = 0.9$.

   ​

2. ***Question.*** On a deserted iscap, 50% of the residents play shuffleboard, 45% play poker, 65% garden. If 40% of the residents play poker and garden and 40% of the residents play both shuffleboard and poker, then find the probability that a resident plays poker, given that they garden.

   ***Answer.*** $\displaystyle P(\text{poker}|\text{garden}) = \frac{P(\text{poker} \cap \text{garden})}{P(\text{garden})} = \frac{0.4}{0.65} = 0.62.$

   ​

3. ***Question.*** In a class containing 10 girls and 8 boys, 2 students are selected at random to give out the math papers. What is the probability that the second student chosen is a boy, given that the first one was a girl.

   ***Answer.*** $\displaystyle P(\text{2nd is a boy}|\text{1st is a girl}) = \frac{P(\text{2nd is a boy}\cap \text{1st is a girl})}{P(\text{1st is a girl})} = \frac{(8/17) * (10/18) }{10/18} = 0.4706$



4. ***Question.*** Nine children are seated at random in three rows of three desks. Let $A$="Ming and Yang sit in the same row, "$B$ ="Ming and Yang both sit at one of the four corner desk." Are $A$ and $B$ independent?

   ***Answer.*** 

   - Compute $P(B)$:
     - Total number of sitting patterns: $9!$.
     - Choose two from the four corners for Ming and Yang: $\binom{4}{2}$.
     - Number of permutations for Ming and Yang on these two seats: $2!$.
     - Number of permutations for the rest 7 people: $7!$. 
     - Thus, $\displaystyle P(B) = \frac{\binom{4}{2} \cdot 2! \cdot 7!}{9!} = \frac{1}{6}.$
   - Compute $P(A)$:
     - Total number of sitting patterns: $9!$.
     - Choose one from the three rows for Ming and Yang: $\binom{3}{1}$.
     - Choose two from the three seats in this row: $\binom{3}{2}$.
     - But Ming and Yang can switch seats: $2!$.
     - Number of permutations for the rest 7 people: $7!$.
     - Thus, $\displaystyle P(A) = \frac{\binom{3}{1}\cdot\binom{3}{2}\cdot 2!\cdot 7!}{9!} = \frac{1}{4}.$
   - Compute $P(A\cap B)$:
     - Total number of sitting patterns: $9!$.
     - Choose one from the two rows that have corners: 2 ways.
     - Ming and Yang can switch spots: 2 ways.
     - Number of permutations for the rest 7 people: $7!$.
     - Thus, $\displaystyle P(A\cap B) = \frac{2\cdot2\cdot7!}{9!} = \frac{1}{18}$
   - Since $P(A\cap B) \ne P(A)P(B)$, we conclude that $A$ and $B$ are not independent. 



5. ***Question.*** A box contains blue chips and red chips. A person selects two chips without replacement. If the probability of selecting a blue chip and then a red chip is $\frac{24}{128}$, and the probability of selecting a blue chip on the first draw is $\frac{7}{16}$, find the probability of selecting the red chip on the second draw, given that the first chip selected was a blue chip.

   ***Answer.*** $\displaystyle P(B1) = \frac{7}{16}, P(B1 \cap R2) = \frac{24}{128},$ then $\displaystyle P(R2 | B1) = \frac{P(B1 \cap R2)}{P(B1)} = \frac{24/128}{7/16} = \frac{3}{7}$. 



6. ***Question.*** There are 20 blue balls, 60 red balls, and 30 white balls. What is the conditional probability of choosing a blue ball given that a white ball is not chosen?

   ***Answer.*** $\displaystyle P(\text{blue}|\neg \text{white}) = \frac{P(\text{blue})}{P(\text{blue or red})} = \frac{20}{80} = 0.25.$

#### Hard

 1.  ***Question.*** Suppose six cards are drawn _with replacement_ from a standard deck of 52 cards. What is the probability that all the cards drawn have the same face value? Ignore suits, for example the 10 of spades and the 10 of hearts have the same face value.

     ***Answer.*** Since drawing is done with replacement the events are independent. You do not card what the first card drawn is. All that matters is that the remaining five cards drawn have the same face value as the first. The probability that a drawn card matches the first one is $\frac{1}{13}$. Since the events are independent the probability of all of them happening is just the product of their probabilities. Thus we have five occurrences of $\frac{1}{13}$ multiplied together, or $\left(\frac{1}{13}\right)^5$. 

     ​

2. ***Question.*** Suppose four cards are drawn _with replacement_ from a standard deck of 52 cards. What is the probability that all the cards drawn are $7$'s?

     ***Answer.*** Since drawing is down with replacement the events are independent. The probability of drawing a $7$ for the first card is $\frac{1}{13}$. Since the events are independent, the probability of all of them happening is just the product of their probabilities. Thus the answer is $\left(\frac{1}{13}\right)^4$. 

     ***Remark.*** If the question had asked the probability of drawing four cards with the same face values, the answer would actually be $\left(\frac{1}{13}\right)^3$ because we don't card about what the first card is. See the question above for detailed explanation. 