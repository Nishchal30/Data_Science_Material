## Measures of Central Tendancy

A measure of central tendancy is a single value that attempts to describe a set of data identifying the central position.

**1) Mean** :- The average of set of numbers
exa:- (1,2,3,4,5)

Mean = 1+2+3+4+5/5 = 15/5 = 3

**There are two types of Mean**

1) Population Mean (u called as meu) :- (sum of no of popluation/no of observations) = (sum xi/N)

exa :- Population Age = {24,23,23,27,21}

population Mean (u) = 24+23+23+27+21/5 = 23.6

2) Sample Mean (x bar) :- (sum of all no of sample/no of observations) = (sum xi/n)

exa :- sample age = {24,21}

Sample Mean (x bar) = 24+21/2 = 22.5

**Always N >> n i.e. Population size >> sample size**

**Practical Application of Mean in Data Science (Feature Engineering)**

Age | Salary | Family size

if some of the rows contains NaN values, Then we cannot drop that values because loss of information,
So we can replace NaN values with the Mean of that particular column.

**While finding the mean of particular column which contains NaN values in some rows, we don't have to count that row of total no of obersvations.**

exa :- if a column contains 8 rows out of which 3 rows are NaN the we have ti divide by 5 in calculating Mean.

**Disadvantages of Mean**
1) If their are outliers in the data, the mean will be shifted towards the outlier and then the standered values will be changed. SO for that we use Median

exa:- age = {1,2,3,4,5} then mean = 1+2+3+4+5/5 = 3
  if  age = {1,2,3,4,5,100} then mean = 1+2+3+4+5+100/6 = 19.6

  So here the mean got shifted so much towards the outlier after adding an outlier in the data.

**2) Median** :- Median is directly the central value of the data.
Steps to find Median :
1) Sort the numbers
2) If the no of elements are even find average of two central elements.
3) If the no of elements are odd, find the central element.

exa :- {1,2,3,4,5,7,8,100,200}
no of elements = 9 = odd
Median = 5 and Mean = 36.66 So here is huge difference between mean & median.

exa :- {1,2,3,4,5,7,8,100,200,210}
no of elements = 10 = even
median = 5+7/2 = 6


**3) Mode** :- Most frequent occuring element

exa :- {1,2,2,3,3,3,4,4,5}
Mode = 3 (3 occurs most of the times)

exa :- {1,2,2,3,3,4,5}
Mode = 2, 3

**Practical Application of Mode in Data Science (Feature Engineering)**

If our data has categorical feature, the we replace NaN values with most occuring value of that column.

exa :- If gender - Male, Female, NaN
Replace NaN with most occuring either Male or Female.


## Measures of Dispersion
1) Variance (sigma sq.) :- Spread of data
2) Standerd deviation (sigma)

1) Variance (sigma sq.):-
There are again two variances

a) Population Variance (sigma sq) :- 
   sigma sq =  sum(xi-u)^2/N
   So basically the numerator term is the distance of each data point from the mean of data. It tells us how the data is spread.

b) Sample Variance (s sq) :-
    s sq = sum(xi - x bar)^2/n-1


2) Standerd Deviation (sigma) :- it is basically the square root of variance.
    The standerd deviation helps to decide how many standerd deviation the data values are falling away from the mean.


## Percentiles 

**Definition** :- A percentile is a value below which certain percentage of value lies.

exa:- 99 Percentiles = It means the person has got the better marks than 99 % of entire class.

exa :- 1,1,2,3,4,56,3,3,6,22,5,76,2,3,4,3,8,5,1. Find out the percentile rank of 8

Step 1) Arrange the data in an ascending order
1,1,1,2,2,3,3,3,3,3,4,4,5,5,6,8,22,56,76

Step 2) Percentile rank of x = No of values below x / n = 15/19 = 78 percentile

exa:- What is the value that exists at 25 percentiles?

Answer:- value = percentile/100 * n
               = 25/100 * 19
               = 19/4
               = 4.7
               = 5th index
               = 2
    
