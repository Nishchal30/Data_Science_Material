## Ridge Regression (L2 Regularization)

As we know linear regression will alwyas try to overfit the model.
Hence to reduce the overfitting problem in regression problems we can use Ridge regression.

In overfitting cases, the cost function will close to 0 and to reduce the cost function we need to add errors in the model.

In reidge regression, we basically add some extra parameters in the cost function to increase the cost function value.

### **Cost function**
So the cost function of ridge regression is given by,

**Cost function = 1/m sum (h(B(xi)) - yi)^2 + lambda sum(slope)^2**

Now lambda(slope) this extra term is added in the linear regression cost function.
lambda = hyperparameter
slope = slope of the independent variable

**What is relationship between lambda and slope**

**If the lambda value increase the slope value decreases.**
**So the lambda and slope are inversely proportional.**

Let's suppose if we take overfitted model where cost function = 0

Now for this equation,
- 1/m sum (h(B(xi)) - yi)^2 + lambda sum(slope)^2
- 0 + lambda sum(slope)^2
- some +ve number greater than 0

Now again the model will try to reduce the increased cost function value by changing B values.
and by changing B values, the best fit line will get changed.

So in this way our model will not be overfit.

Now the problem in ridge regression is the coefficient of independent variable i.e. B will never be zero as we are squaring the slope value.
If the B value becomes zero then that independent feature will get discarded.


## Lasso Regression (L1 Regularization)
As ridge regression doesn't support B to be zero for selecting important features,
so lasso regression is useful there for feature selection.

**Cost function = 1/m sum (h(B(xi)) - yi)^2 + lambda sum (abs(slope))**

Let's take an example,
h(B(x)) = B0 + B1x1 + B2x2 + B3x3 + .... + Bnxn
h(B(x)) = B0 + 0.54x1 + 0.23x2 + 0.10x3

From the above equation we can say that
If y increases by 1, x1 will increase by 0.54
If y increases by 1, x2 will increase by 0.23
If y increases by 1, x3 will increase by 0.10

Now x3 is the least correlated feature to y right now as the B3 = 0.10, 
and if we keep on changing lambda value B3 will come to 0 so x3 will not be important for y.

As we are just taking the magnitude of slope value so the slope can be zero for some of the features which are not correlated to the dependent feature.


## Elastic Net Regression (Combination of L1 & L2 Regularization)

**Cost Function = 1/m sum (h(B(xi)) - yi)^2 + lambda1 sum(slope)^2 + lambda2 sum (abs(slope))**
                This term can be MAE, MSE, RMSE     ridge C.F                  Lasso C.F





