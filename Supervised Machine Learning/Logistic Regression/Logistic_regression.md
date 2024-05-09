## Logistic Regression 

Logistic Regression is a classfication algorithm, though it's name suggests a regression algorithm but it is a classification algorithm.

exa:- 
Let's take one dependent and one independent variable use case

Study Hours    |    Result (Pass/Fail)
    2          |          Fail
    3          |          Fail 
    4          |          Fail
    5          |          Fail
    6          |          Pass
    7          |          Pass
    8          |          Pass
    9          |          Fail


Q.1) Can we solve the above problem using regression algorithm?

We can plot this data on graph study hours on X-axis and Pass/Fail on Y-axis as 0 for Fail & 1 for Pass.

Now some points will be on x-axis as result fail = 0 
and some points will be on y = 1 as Pass

So we will draw a best fit line, accroding to the best fit line we can make some assumptions like,

If y <= 0.5 the output will be 0
and if y > 0.5 the output will be 1.

so let's say a person studying for at least 6 hours will be going to pass, less than that will fail.

**In this we are able to solve the problem with linear regression also.
Then why do we need logistic regression?**

Now if we have more numbers like 15, 16 hours as outliers and then plot a best fit line
as the linear regression disadvantage the line will tend towards the outliers and the previous threshold values will change.

Now let's say the person studying for 7 hours will going to fail, and this proves the model is not performing well.

Now if we have value like 18 hours on X-axis then by the best fit line it will predict the Y-value beyond 1, but we don't understand the Y value beyond 1 and 0.
So for this the logistic regression will flatten a best fit line on Y-value 0 & 1 using **Sigmoid Function**

Sigmoid function = 1 / 1 + e^-z   where z = B0 + B1x

**The output of sigmoid function will always be 0 to 1.**

### **cost function of logistic regression**

First we create best fit line here in logistic regression also and then we flatten the line.
so the equation of best fit line is,

J(B0, B1) = 1/m sum (h(B(xi)) - yi)^2

h(B(x)) = sigmoid (B0 + B1x) where  z = B0 + B1x
h(B(x)) = sigmoid (z)
h(B(x)) = 1 / 1 + e^-z
h(B(x)) = 1 / 1 + e^-(B0 + B1x)   where  0 <= h(B(x)) => 1

and the threshold value will always be 0.5 if h(B(x)) > 0.5 means 1
and if h(B(x)) <= 0.5 means 0.


**Problem with the above equation**
There are two types of function 

Non-convex function :-
The function has many local mimima i.e. they don't have single global mimina like the linear regression cost function MSE they are called as Non-convex function.
So here the coefficient value will come to one local minima and will get stuck assuming it's a global minima.
exa:- Logistic regression.

Convex functions :- 
The functions who have only one gloabl minima for their cost functions like MSE in linear regression are called as Convex functions.
exa:- Linear regression


So the logistic regression cost function is a non convex function after applying the sigmoid function on top of the MSE, hence we cannot use that cost function so there is a new cost function for logistic regression called as Logloss.


### **Logloss Cost function**

cost (h(B(xi)), yi) = {
                        -log(h(B(x)))  if y = 1       h(B(x)) = 1 / 1 + e^-(B0 + B1x) 
                        -log(1 - h(B(x))) if y = 0
                        }

cost (h(B(xi)), yi) = -y (log(h(B(x)))) - (1 - y) log (1 - h(B(x)))
by putting y = 0 & 1 in the above eqn we will get the above values.
This will become the Convex function now.

and then we will minimize the value of this cost function by changing the coefficients value B0, B1 by using Convergence Algorithm given as ,

{
    Bj : Bj - alpha (del/del Bj)*(J(Bj))
}  for j = 0 & 1


## **Logistic Regression using Multiclass classification**

To perform this we need to split multi-class classification problem into multiple binary classification datasets and train a binary classification model each.

There are below two methods to perform this task
1) One vs Rest 
2) One vs One

1) One vs Rest:
For example, given a multi-class classification problem with examples for each class ‘red,’ ‘blue,’ and ‘green‘. This could be divided into three binary classification datasets as follows:

- Binary Classification Problem 1: red vs [blue, green]
- Binary Classification Problem 2: blue vs [red, green]
- Binary Classification Problem 3: green vs [red, blue]


**Python Implementation**
LogisticRegression(multi_class='ovr')
Also we have OneVsRestClassifier class in python for this.


2) One vs One:
Like one-vs-rest, one-vs-one splits a multi-class classification dataset into binary classification problems. Unlike one-vs-rest that splits it into one binary dataset for each class, the one-vs-one approach splits the dataset into one dataset for each class versus every other class.

For example, consider a multi-class classification problem with four classes: ‘red,’ ‘blue,’ and ‘green,’ ‘yellow.’ This could be divided into six binary classification datasets as follows:

- Binary Classification Problem 1: red vs. blue
- Binary Classification Problem 2: red vs. green
- Binary Classification Problem 3: red vs. yellow
- Binary Classification Problem 4: blue vs. green
- Binary Classification Problem 5: blue vs. yellow
- Binary Classification Problem 6: green vs. yellow

The formula for calculating the number of binary datasets, and in turn, models, is as follows:

(NumClasses * (NumClasses – 1)) / 2
We can see that for four classes, this gives us the expected value of six binary classification problems:

- (NumClasses * (NumClasses – 1)) / 2
- (4 * (4 – 1)) / 2
- (4 * 3) / 2
- 12 / 2
- 6


**Python Implementation**
SVC(decision_function_shape='ovo')

model = SVC()
# define ovo strategy
ovo = OneVsOneClassifier(model)

## **Interview Question**

1) Can logsitic regression is used for multiclass classification problem, if yes how?
Ans - The answer is yes, we can perform logistic regression o multiclass target variable, but then it is called as Multiomial Logistic Regression.

To perform this we need to split multi-class classification problem into multiple binary classification datasets and train a binary classification model each.

There are below two methods to perform this task
1) One vs Rest 
2) One vs One


2) What is the major difference between logistic regression and SVC?
Ans - Both are designed to perform Binary classification problem by default, but we can perform multinomial classification problem by tweaking the algorithms.

- Logistics is a linear model, which helps to classify the target class based on sigmoid function with linear dependent features.
- SVC is a non-linear model that finds the hyperplane to seperate the classes.
- Logistic is simple and easy to interpret, it works well when there is linear relationship between independent and dependent features.
- SVC when we use non-linear kernels, can be complex to interpret.


3) Why logistics regression is called as regression and not classification even if it is a classification algoritm?

ans:
- So it is not an independenly a classification algorithm, it is based on linear regression itself.
- But we apply sigmoid function on top of it which converts the values in probabilities.
- Hence it is a classification algorithm, but the output we get is 0 & 1 which is a regression numbers so it is called as regression in name.




