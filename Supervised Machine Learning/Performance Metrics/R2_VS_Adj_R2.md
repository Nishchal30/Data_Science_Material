## Performance Metrics

**1) R-squared:-**

R - squared = 1 - SS_res/SS_total

SS_res -> Sum of squares of residual
SS_total -> Total sum of squares

R - squared = 1 - sum (yi - y^)^2 / sum (yi - ybar)^2

**If the model is fitted well then numerator will be small & denominator will be higher**
Hence,

- R - squared = 1 - small number
- R - square <= 1 (Always)

**If R - square = 0.85 we can say that the model is 85% accurate.**

If the case is reversed like if the numerator term is smaller than the denominator then 

R - square = 1 - higher value
R - square = -ve value

R- square wil be -ve when the best fit line is far away from the data points so the error will be higher than but the average line of y values

**If the R - square value is negative then the model is very bad**

**2) Adjusted R-square:-**

Adjusted R-square is used when we have multiple independent features and out of many features we have to select only relevant features which are important to predict dependent variable.

exa: If we have size of house, location, no of bedrooms, gender features as independent features
and we have dependent features as price of house
- then if we use R-square by using size of house, location, no of bedrooms this 3 features the R-square value may increase.
- But if we use gender feature also which might not relevant to dependent feature then R-square may decrease or there will no change.
- So to select only relevant independent features we use Adjusted R-square.


Adjusted R-square = 1- [(1 - R-square)(N-1)] / [N - P - 1]
Here,
N = no of data points
P = no of independent features

Now how does this works,
- If we predict price of house with size of house then R-square can 65% & Adjusted R-sqaure can be 63%
- If we predict price of house with size of house & location then R-square can 75% & Adjusted R-sqaure can be 73% 
- If we predict price of house with size of house, location & no of bedrooms then R-square can 85% & Adjusted R-sqaure can be 83% 
-If we predict price of house with size of house, location, no of bedrooms & Gender then R-square can 88% but Adjusted R-sqaure can be 85% or may lesser than that. 