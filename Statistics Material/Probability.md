## Central Limit Theorem

If we draw samples from population with sample size >= 30, the distribution of sample means drawn will follow a normal distribution.

## Probability

Probability is a measure of a likelihood of occuring an event.
exa:- Tossing a fair coin 
p(Head) = 0.5
p(Tail) = 0.5

**Machine Learning application**

Whenever we have the two groups data, and we have to find the new data point lie in which group, then based on probability we can decide whether the new data point will lie in 1st group or 2nd.

### **1) Mutual Exclusive Events**:- Two events are mutually exclusive, if they cannot occur at the same time.
exa:- Tossing a coin, heads and tails occur at same time is Mutually Exclusive event.

**Addition Rule of Probability for Mutual Exclusive Events**
1) What is the probability of coin landing on heads or tails?

p(A or B) = p(A) + p(B)
= 0.5 + 0.5
= 1

2) What is the probability of getting 1 or 6 or 3 in dice rolling
p(A or B or C) = p(A) + p(B) + p(C)
= 1/6 + 1/6 + 1/6
= 1/2
=0.5


### **2) Non-Mutual Exclusive Events**:- Two events can occur at the same time.
exa:- Picking a card randomly, an event where "Heart" & "King" can come at same event.
In a bag of balls, picking up a red and black ball same time.

1) A bag of marbels contains 10 red, 6 green, 3 with both red & green colors.
When picking randomly, what is the probability of choosing a marble of red or green color?

--> This is an Non - Mutual Exclusive event.

**Addition Rule of Probability for Non- Mutual Exclusive Events**

P(A or B) = p(A) + p(B) - p(A and B)
p(red or green marble) = p(red marble) + p(green marble) - p(Red & green marbles)
= 13/19 + 9/19 - 3/19 -- (Red means only red + 3 marbles which contains red & green both color so 10 + 3 = 13)
= 19/19
= 1


2) In deck of cards, what is the probability of selecting heart or queem card.
p(Heart or Queen) = p(Heart) + p(Queen) - p(Heart and Queen)
    = 13/52 + 4/52 - 1/52
    = 16/52

**Why we subtract *p(A and B)* this term in Non-Exclusive event addition rule, because there is intersection between two events in Non-Exclusive event as both events can occur at same time.**

#### **Dependent Events**:- If one event affects the other event, then that two events are dependent events.
exa:- In bag of marbles, there are 4 white and 3 yellow marbles.
p(White marble) = 4/7 
**Now after drawing one marble, total marbles in bag become 6**
Hence p(yellow marble) = 3/6

Now The second event is affected by occuence of first event, hence this two events are called dependent events.

exa:- In the bag of marbles, we have 4 orange & 3 yellow marbles. What is probability of drawing and orange & yellow marbles?

--> This is an dependent event as after picking one marble, the sample space become change.
p(Orange) = 4/7
p(Yellow given orange has occured) = 3/6

**p(Yellow given orange has occured) this is also called as conditional probability**

p(Orange & Yellow) = p(Orange) * p(Yellow given orange has occured)
     = 4/7 * 3/6
     = 2/7

#### **InDependent Events**:- If one event does not affects the other event, then that two events are independent events.
exa:- What is the probability of rolling a "5" and then "3" with a normal dice.
This is an independent event, there is no connection by occuing 5 at dice & then 3 at dice.

For this we use
**Multiplication rule for Independent Events**
p(A & B) = p(A) * p(B)
    = 1/6 * 1/6
    = 1/36