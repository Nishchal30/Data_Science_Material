## Mean Squared Error (MSE)

MSE = 1/n sum (y - y^)2

y^ = B0 + B1*x

### **Advantages of MSE**
1) The equation for MSE is quadratic equation, and quadratic equations are differentiable.
2) This equation has only one global minima as the graph for MSE is parabola curve which has only 1 global minima.

### **Disadvantages of MSE**
1) Not robust to outliers
- exa:- If we have outliers then the error term will be very high and the line will be shifted towards the outliers rather than the best fit line.
2) In the error term, we ar changing the original units by squaring the difference between actual and predicted value.
- exa:- If we have salary as dependent variable and we will make the (y - y^)2 so if the salary is in lakhs then we are making lakhs^2 hence the original units are changing.


## Mean Absolute Error (MAE)

MAE =  1/n sum abs(y - y^)

### **Advantages of MAE**
1) Robust to outliers as we are not squaring the error term we are just taking the magnitude of error, hence the line will shift to outliers but not as much as the MSE.
2) The original units will remain unchanged.

### **Disadvantages of MAE**
1) Convergence to global minima will take more time as the cost function is not a quadratic equation.
so for this there is one concept called subgradient.
2) Time consuming


## Root Mean Squared Error (RMSE)

RMSE = root(1/n sum (y - y^)2)
y^ = B0 + B1*x


