## Gaussian or Normal Distribution

- The shape of normal distribution is bell shaped curve, Symmetrical in size means 50% of data lies in the LHS of the mean and 50% data lies in RHS.

- The area under the bell curve will always be 1 i.e 100%
exa:- Generally Age, Height, Weight follows normal distribution.


**Emperical formula of Normal distribution**

The emperical formula says that the data spread in normal distribution is as below:

   u-3sigma | u-2sigma | u-1sigma | u | u+1sigma | u+2sigma | u+3sigma

Also called as 68-95-99.7 rule.


**Asumptions of Normal distribution**
1) Between u-1sigma to u+1sigma 68% of data lies withing this range only.
i.e. Within 1 standerd deviation to left & right from the mean, 68% of data is spread.

2) Between u-2sigma to u+2sigma 95% of data lies withing this range only.
i.e. Within 2 standerd deviation to left & right from the mean, 95% of data is spread.

3)Between u-3sigma to u+3sigma 99.7% of data lies withing this range only.
i.e. Within 3 standerd deviation to left & right from the mean, 99.7% of data is spread.


## Standerd Normal Distribution

Let's assume X follows Normal distribution with (u, sigma)
now we can covert X -> Y & Y follow Standerd Normal Distribution with (u = 0, sigma = 1)
This can be done using z - square technique or standerdization.

**Z-score formula**

z-score = (xi - u/sigma)/sq root(n) where sigma/sq root(n) = standerd error

We apply this formula on each & every value. Hence while applying this formula on every variable, n = 1 always.

z-score = (xi - u/sigma)/sq root(n) = (xi - u/sigma) as n is 1.

**Why do we want to convert Normal to Standerd Normal**

let's take an example-

Age(years)  |   Weight (Kg)  | Height (cms)
  24        |       72       |   150
  27        |       58       |   160

At the end of the day we will apply some machine learning algorithms on the above data.
Now in the backend machine learning algorithms means apply some mathematical calculation on the data.

Now if the scale of the data is such a high, then the calculation will take much high time.
So to bring all the data points to the same scale, we need to apply z-score formula.

**This whole process inshort we called as Standerdization bcoz of u = 0 & sigma = 1**

**Only for scaling purpose we are not using Standerdization, but that also keeps the distribution Normal for the data.**

## Normalization

In Normalization, the data points are converted in the format that we will specify.
i.e. convert data in the range(0 to 4) or (0 to 10) etc.

**1) Min Max Scaler**[0,1]
Converts all the values within 0 to 1, using the below formula. 
 
x scaled = (x - x min) / (x max - x min)

exa:- 
x = [1,2,3,4,5]

x1 = 1-1/5-1 = 0
x2 = 2-1/5-1 = 0.25
x3 = 3-1/5-1 = 0.5
x4 = 4-1/5-1 = 0.75
x5 = 5-1/5-1 = 1

By applying the above formula on x
y = [0, 0.25, 0.5, 0.75, 1]

**Where do we apply Normalization**
- In deep learning, the images are present in the pixels form and pixels ranges from (0 to 256) there we need Normalization technique to convert pixels range from (0 to 256) to (0 to 1)


**Difference between standerdization & Normalization**

1) If the data is scaled too much and the distribution is normal, to scale down the data without disturbing the normal distribution, at that point we use Standerdization.
exa:- Machine Learning

2) Normalization is required only when we have to bring the data in same scale, without bothering about the distribution.
exa:- In CNN image processing, we need to normalize the pixel values.


## Skewed Distribution

Skewed distribution:- When the curve of the distribution tends to only on one size but some data points lies on the other side.

1) Right skewed distribution:- The curve will be on left side of x-axis and the curve is elongated towards right side of x-axis.
exa:- Wealth distribution, Life expectancy

2) Left skewed distribution:- The curve will be on right side of x-axis and the curve is elongated towards left side of x-axis or at the start of axis.

**The relationship between mean, mode and median between Right skewed and Left skewed distributions**

For right skewed distribution :- mean < median < mode
For left skewed distribution :- median < mean < mode


## Log Normal Distribution

**Log normal distribution is applicable only to right skewed data.**

If X follows Log normal distribution and if we apply Y = log base e(X) then, Y follows Normal Distribution.

Similarly vice-versa,

if X follows Normal distribution with (u, sigma) and if we apply exp(X) then, we will get Log Normal distribution.


## Practical Implementation of z-score

Let's take X = {1,2,3,4,5,6,7}
and u = 4, sigma = 1

**Q. What is % of score that falls above 4.25?**

Total area under the curve = 1

z-score = x-u/sigma = 4.25 - 4/1 = 0.25
 
Hence we can say 4.25 falls 0.25 S.D right side to the mean.
Now check the z-value in z-table.

The value in z-table for 0.25 = 0.59
But it gives the value from left to till the our z-score value.
 
Now to find the area above 4.25 is 1-0.59 = 0.41


## Practise Question

Q.1) In India the average IQ is 100 with a standerd deviation of 15. What is the % of population would you expect to have an IQ?
a) Lower than 85
b) Higher than 85
c) Between 85 and 100







