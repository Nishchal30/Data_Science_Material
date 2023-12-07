## Inferential Statistics

On the basis of sample data from the population, we make some assumptions or conclusions for population. To validate or to prove our made assumptions or conclusions for population are correct we Hypothesis testing.

**Steps to perform Hypothesis testing:**
**step 1) Null Hypothesis:-** The default statement will be considered as null hypothesis.
By default Null hypothesis will always true.

exa:- If we want to perform hypothesis testing on whether the new created medicine has any effect on cancer patients.

so the Null hypothesis will be:
If new medicine will not be effective on cancer patients.


**step 2) Alternative Hypothesis:-** The alternative hypothesis is always the opposite of Null hypothesis.

Exa:- The new medicine has some effect on cancer patients.

**step 3) Perform Experiment:-** Now to perform experiment we need to define confidence interval first.
After defining the confidence interval given below, we will perform experiment.

and in our given example if either heads <= 80 & tails >= 20 or tails <= 80 & heads >= 20, **the no of heads & tails will be in our defined confidence interval so we will accept the Null Hypothesis. i.e. We fail to reject the null hypothesis**
**If the no of heads & tails are beyond our defined confidence interval then we will reject the Null hypothesis & will accept the alternative hypothesis. i.e.  we fail to reject alternative hypothesis**

### **What is confidence interval?**

Let's take an example of tossing a fair coin 100 times.
In this experiment the Null hypothesis would be:
The coin is fair if head comes 50 times and tail comes 50 times.

Now for saying the coin is unfair, we will decide a threshold value of coming heads or tails on the coin.
So let's suppose if we say head comes 80 time i.e. tail comes only 20 times out of 100 then the coin is unfair.

So here we have decided a confidence interval that till either heads = 80 & tails = 20 or Tails = 80 & heads = 20 our coin is fair. Beyond that the coin is unfair.

Confidence Interval = {20,80} this can be decided by the domain expert.


### **Significance Value**

Now to calculate significance value, first we need to decide the confidence interval.
If we say the confidence interval is 95%
then significance value is:

S.V. = 1 - confidence interval  -- subtracting from 1 bcoz total area under normal curve is 1
     = 1 - 0.95 
     = 0.05

Hence significance value is 0.05

Lower fence & Upper fence are two terms that are being used in calculating Confidence interval.

Lower fence & Upper fence are the parts on normal curve outside the confidence interval.
Lower fence is the at the LHS of mean & upper fence is at RHS of mean.

IF CI = 95% then remaining 5% will be distributed as 2.5 % Lower fence & 2.5 % for Upper fence.
 

### **Point Estimate:**
The value of any statistics that estimates the value of parameters is called point estimate.

**What is Statistics & parameters?**
So let's take an example of sample mean xbar and population mean u.

x bar --> u

In inferential statistics we try to find the value of u based on the value of xbar.
xbar = Statistics
u = parameter.

Hence xbar is the point estimate bcoz we are trying to estimat parameter u value based on statistics xbar.

**point estimate (sample mean) +/- margin of error = parameter (population mean)**

Lower CI = point estimate - margin of error
Upper CI = point estimate + margin of error

Formula for margin of error = z alpha/2 (z Significance value/2)  * sigma/root(n)

**Practcal problem**

Q.1) On the quant test of CAT exam, a sample of 25 people has a mean of 520 marks with *population standerd deviation* of 100. Construct a 95% confidence interval about the mean.

--> n = 25, xbar = 520, sigma = 100, CI = 95%
Significance value = 1-0.95 = 0.05

Now lower & upper fence = 0.05/2 = 0.025

- Lower CI = point estimate - margin of error
- Lower CI = z alpha/2 (z Significance value/2)  * sigma/root(n)
- Lower CI = 520 - z 0.05/2 * 100/root(25)
- Lower CI = 520 - z0.025 * 20
- Lower CI = 520 - (z table value of z 0.025) *20 --- (z table value of z 0.025 will be calculated as total area till 0.025 = 1-0.025 = 0.975 and z value of 0.975 is 1.96. 2nd method is directly find where 0.025 is there in ztable that value will be for -0.025 but as curve is symmetrical that same value will be for +0.025)

- Lower CI = 520 - 1.96*20
- Lower CI = 480.8
- Upper CI = 520 + 1.96*20 = 559.2

**Hence the CI range is {480.8, 559.2}**


Q.2) On the quant test of CAT exam, a sample of 25 people has a mean of 520 marks with *sample standerd deviation* of 80. Construct a 95% confidence interval about the mean.

--> Here instead of population standerd deviation, we have given sample standerd deviation.
So the formula for margin of error changes to,

margin of error = x bar +/- t (alpha/2) * s/root(n)
Now to calculate t(alpha/2), we need to calculate degree of freedom 

degree of freedom = n-1 = 25-1 = 24

- Lower CI = x bar - t (alpha/2) * s/root(n)
- Lower CI = 520 - t (0.05/2) * 80/5 --  (t (0.05/2) we have to see in t-table for this with d.f = 24 & t two-tail = 0.05)
- Lower CI = 520 - 2.064 * 16
- Lower CI = 486.97
- Upper CI = 520 + 2.064 * 16
- Upper CI = 553.02


## One tailed / two tailed test
Q. A college in town A has placement rate of 85%. A new college was recently opened & it was found that sample of 150 students had placed with placement rate of 88% with standerd deviation 4%. Does this college has a different placement rate with 95% CI?

--> The above que is for two tailed test, as there mentioned *different placement rate*, it means it can either be less than 85% or greater than so for this we have to focus on both the tails of the curve.

--> If the que has something like greater than 85% then we will have to focus on right side of tail means one tailed test.
--> If the que has something like less than 85% then we will have to focus on left side of tail means one tailed test.

### **P-value**

The p-value is the probability of observing a test statistic under the assumption that the null hypothesis is true.
In simple words, The p-value tells us how likely it is that our conclusions are true, or if they might have happened just by chance.

- A low p-value (usually less than 0.05) is like finding a strong clue that suggests your conclusions are probably true. In simple words if p -value >= alpha value then accept the Null Hypothesis.
- A high p-value (greater than 0.05) means your findings could easily be explained by chance. In simple words if p -value < alpha value then reject the Null Hypothesis.


## Hypothesis testing practical problem

Q.1) A factory has a machine that fills 80 ml of baby's medicine in a bottle. An employee belives the average amount of baby medicine is not 80 ml. Using 40 samples, he measures the average amount dispersed by the machine to be 78 ml with a standerd deviation of 2.5
Find out:
a) State Null & alternative hypothesis
b) At 95% CI, are there enough evidences to support machine is working properly?

--->

**Null Hypothesis: An average amount of medicine filled is 80 ml & machine is working fine.**
**Alternative hypothesis: An average amount of medicine filled is not 80 ml & machine is not working fine.**

Given:  u = 80 , n = 40, xbar = 78, s = 2.5, CI = 95%

significance value = 1-CI = 1-0.95 = 0.05

z-table value for 1-0.025 = 0.975 = +- 1.96

### **When to perform which test out of z-test & t-test?**

1) When we have given n >= 30 *or* population standerd deviation i.e. sigma is given then we have to use z-test.
2) When we have given n <= 30 *and* sample standerd deviation i.e s is given then we have to use t-test.

Now in our problem we have given with n >= 30 & sample standerd deviation i.e. s is given so we have to use z-test here.

C) Calculate z-statistics,

- z = xbar - u/s/root(n)
- z = 78 - 80/2.5/root(40)
- z = -5.05

d) Conclusion: If z-statistics <= or >= z-table value then we will reject the null hypothesis.
In our case -5.05 < -1.96 hence we have to reject null hypothesis and accept alternative hypothesis.

Q.2) A factory manufactures cars with warrenty of 5 years or more on the engine & transmission. An engineer belives that the engine or transmission will malfunction in less than 5 years. He tests a sample of 40 cars and find the average time to be 4.8 years with a standerd deviation of 0.5
1) state the null & alternate hypothesis.
2) At 2% level of significance are there enough evidences to support the idea that warrenty should be revised?

--> Given, 
The problem is of one - tailed test using z-test.

xbar = 4.8, n = 40, s = 0.5,  alpha = 0.02, u = 5

We have to check the engine or transmission will malfunction in less than 5 years means it's a left -tail test.

Null Hypothesis: The warrenty should not be revised to less than 5 years.
Alternate Hypothesis: The warrenty should be revised to greater than 5 years.

- z - score = xbar - u / s / root(n)
- z - score = 4.8 - 5/ 0.5/root(40)
- z - score = -2.52

So now check the area under the curve at -2.52 in z - table for the p-value

The area under the curve at -2.52 = 0.00587

**Conclusion:** 
a) Here p - value = 0.00587 & alpha = 0.02, if p-value < alpha i.e. 0.00587 < 0.02 hence we will reject the null hypothesis and accept the alternate hypothesis.


Q.3) The average weight of all residents in a town is 168 pounds. A doctor belives the true mean to be diferent. She measured te weight of 36 people and found the mean to be 169.5 pounds with a standerd deviation of 3.9.
a) State the null & alternate hypothesis.
b) CI is 95%, are there enough evidences to accept the null hypothesis?

--> Given,
The above problem is two tailed as we have given only belives the true mean to be diferent so it can either be greater or less than mean.

Null Hypothesis: The average weight of residents is not different than 168
Alternate hypothesis: The average weight of residents is different than 168


xbar = 169.5, u = 168, n = 36, s = 3.9, CI = 95% i.e alpha = 0.05

- z-score = 169.5 - 168/ 3.9/root(36)
- z-score = 2.30

Now find out the p-value for both the tails at z-score 2.30

for negative tail p-value at 2.30 = 0.01072
for positive tail p-value at 2.30 is 1- 0.0892 = 0.0108

total p-value for two tails = 0.01072 + 0.0108 = 0.0208

**Conclusion:**
Hence p-value < alpha i.e. 0.02 < 0.05 hence we will reject the null hypothesis and accept the alternate hypothesis.


Q.4) A tech company belives that the % of residents in town that owns a cell phone is 70%. A marketing maneger belives that this value would be different. He conducts a survey of 200 people and found that 130 responded yes owning a cell phone.
a) State null & alternate hypothesis
b) 95% CI, are there enough evidences to reject the null hypothesis.

--> Given, cell phone % = 70 = 0.7, n = 200, CI = 95% alpha = 0.05

Null Hypothesis: p0 = cell phone proportion in town is not 0.7
Alternate hypothesis: cell phone proportion in town is 0.7

Out of 200, 130 are resonded hence proportion of responded = 130/200 = 0.65

p^ = 0.65
q0 = 1-p0
q0 = 1-0.7 = 0.3

- z-test with proportion = p^ - p0/root(p0q0 / n)
- = 0.65 - 0.70 / root(0.7*0.3/200)
- = -1.54

z-table value for alpha = 0.05 = -1.96

Conclusion: Hence -1.54 > -1.96 hence we fail to reject the null hypothesis.

- p-value = 0.06178 + (1-0.93822)
- p-value = 0.12356

p-value > alpha hence we will fail to reject the null hypothesis.



