## Simple Linear Regression

The simple linear regression is used to solve the regression problem statements.
Simple linear regression contains only 1 Independent feature and 1 dependent feature.

Independent feature: The feature which is not dependent on any other feature, in simple words independent features won't change if we change data of any other feature. (variable which we use for predicting target)

Dependent feature: The feature which is dependent on other features, i.e. it would change by changing in any other feature. (target variable)

Regression problem statements means where we have to predict the continuous data and not a categorical data.

**Regression Problem statements**
1) Predict the price of rooms based on the number of rooms.
2) Predict salary based on year of experience.

**Objective of Simple linear regression**
The main aim of simple linear regression is to find the best fit line so that the sum of the difference between the actual data point and the predicted data point is lowest which is called as error or residual.

We will pick up that model from which we are getting the sum of the difference is lowest or the error is minimal i.e the best fit line.


### **Mathematics behind the best fit line**
The best fit line is basically the equation of straight line, and the equation is given as,

y = m(x) + c 
OR
y = B0 + B1(x)   (B = beta)

- In the above equations, c or B0 called as **intercept**

Intercept is basically the point on y-axis where the best fit line is meeting to y-axis.
i.e. when x = 0, what is the default y value.

exa:- What is the salary of an employee having 0 years of experience?

- B1 or m is the slope of best fit line.

With the unit movement in x-axis what is the movement in y-axis is called as slope

In terms of choosing the best fit line, we first have to draw multiple lines and then choose best out of it.
for drawing multiple lines, we need to change the values of m/B1 and c/B0

and drawing multiple lines and choosing best line out of it is called as training the model.

### **Cost Function**

J(B0, B1) = 1/m sum[h(B(xi)) - yi]^2

- (h(B(xi)) - yi) this term is giving us the predicted data - actual data
- We are dividing by 1/m bcoz the above term is called as Mean Squared Error
- Dividing by m bcoz the cost function is mean squared error so to take the mean we are dividing by m

Now our aim is to reduce the cost function J(B0, B1) value by changing values of B0 & B1 i.e. intercept and slope.

h(B(xi)) = B0 + B1(x)

### **gradient descent curve**

Now let's consider our best fit line is passing fron origin 
it means at B0 = 0, h(B(xi)) = B1(x)

**1st case**
Now if we have B1 = 1, then the equation becomes

h(B(xi)) = 1....when x = 1
h(B(xi)) = 2....when x = 2
h(B(xi)) = 3....when x = 3

The cost function becomes,

- J(B1) = 1/m sum (h(B(xi)) - yi)^2
- J(B1) = 1/3 sum [(1-1) + (2-2) + (3-3)]^2
- J(B1) = 0

**2nd case**
Now if we have B1 = 0.5, then the equation becomes

h(B(xi)) = 0.5....when x = 1
h(B(xi)) = 1......when x = 2
h(B(xi)) = 1.5....when x = 3

The cost function becomes,

- J(B1) = 1/m sum (h(B(xi)) - yi)^2
- J(B1) = 1/3 sum [(0.5-1)^2 + (1-2)^2 + (1.5-3)^2]
- J(B1) = 1/3 * (0.25+1+2.25)
- J(B1) = 3.5/3
- J(B1) = 1.16

Now similary by changing the values of B1, we will get different values for cost function.
and if we plot the values of cost functions against J(B1) and B1 we will get the parabola curve called as **gradient descent curve.**

Now on the gradient descent curve, whatever cost function value is at lowest point we will select that as our best fit line value.
And the lowest point on gradient descent curve is called **Global Minima**

Our machine learning model will need to select the B1 value in such as case that we will reach to the global minima point, and for this we use **Convergence Theorem**

### **Convergence Theorem** (optimize the changes of B1 value)

Repeat untill the convergence

{
    Bj : Bj - alpha (del/del Bj)*(J(Bj))
}

Now by taking the derivative w.r.to B0 and B1 we will get the below terms,

{
    B0 : B0 - alpha (del/del B0)*(1/m sum (h(B(xi)) - yi)^2)
    B0 : B0 - alpha (1/m sum (h(B(xi)) - yi))

    B1 : B1 - alpha (del/del B1)*(1/m sum (h(B(xi)) - yi)^2)
    B1 : B1 - alpha (1/m sum (h(B(xi)) - yi)) * xi
}


Here alpha = learning rate
(del/del Bj)*(J(Bj)) = slope of the point on the gradient descent

Slope of that point can be +ve or -ve based on the Right side of the slope line.
- If the right side of line pointing towards down then the slope is -ve
- If the right side of the line pointing towards up then slope is +ve.

Now if the slope is -ve, 
- Bj = Bj - alpha (-ve)
- Bj = Bj + alpha

**It means the B value will increase and will tends towards the global minima.**

Similarly,
Now if the slope is +ve, 
- Bj = Bj - alpha (+ve)
- Bj = Bj - alpha

**It means the B value will descrease and will tends towards the global minima.**

At global minima we will get out best fit line bcoz the cost function will be lowest, and cost function is nothing but the sum of the errors i.e. sum (predicted point - actual point)

alpha = learning rate decides the speed of the convergence.
- If the alpha value is very less, our model will require lot of time to come to global minima
- and if the alpha value is very high, it will jump from one side to other and again require a lot of time to come to global minima.
- **So generally we choose alpha = 0.001**

## Questions on Linear Regression

1) What is linear regression?
- The linear regression is the model which predicts the dependent variable value based on the changing of indepndent variable. It shows the linear relationship between independent & dependent variables.

2) How we can calculate error in linear regression?
Error means the difference between the predicted point and actual data point.
- Mean squared Error (MSE)
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

3) What is the difference between loss and cost function?
- Loss function is the error value of a single data point
- Cost function is the average error value of all the data points

4) Difference between MAE, MSE, RMSE?
- MAE is Mean Absolute Error which is we just take the average of the magnitude of error term 
- MSE is Mean Squared Error which is we take the squared average of the error term.
- RMSE is Root Mean Squared Error which is the square root of MSE.

5) How Gradient descent works in linear regression?
- The equation of linear regression is given as y = mx + c and we have to minimize the error term that is the difference between the actual data point and the predicted data point.
- So in order to minimize the cost function we try and error with multiple m & c values an the process of the chaning m & c and finding the mimimum cost function value is called Gradient descent.

6) What does the itercept term means?
- The intercept meaning is what will be predicted value when the best fit line is passing from origin.
- In simple words, what will be y value when x  = 0.

7) Assumptions of Linear regression?
- The Assumptions of Linear regression are basically to check whether our fitted model is good or not.
- The should be linear relationship between actual and predicted data.
- The residuals or errors should be normally distributed.
- The relationship between residuals and the predicted data, they should be uniformly distributed which is also called as Homoscedacity.


8) How does the hypothesis testing used in linear regression?

9) How would you decide the importance of variable for multiple linear regression?

10) Difference between R2 and adjusted R2?




