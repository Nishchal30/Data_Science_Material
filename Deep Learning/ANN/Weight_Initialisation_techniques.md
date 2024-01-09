## Weights Initialisation Techniques

Weight initialisation is important because of exploiding graident problem
If we assign larger weights in back propogation, the gradient decsent curve will not come to global minima.
It will jump this side to that if we choose higher weights.

There are three weight initialisation techniques

1) Uniform Distribution
2) Xavier / Glorot Intialisation
3) Kaiming he initialisation


## Key Points for weights initialisation:
1) Weights should be small
2) Weights should not be same (the equation becomes same for all neurons and it will not perform extra tasks all neurons will perform same)
3) Weights should have good variance. (The difference within all weights should be good)


## 1) Uniform Distribution:

The formula for uniform distribution weight initialisation is given as,

wij follows Uniform Distribution with [-1/sqrt(no of input), 1/sqrt(no of input)]

Here i = no of inputs, j = no of layers

Exa: If we have 3 input nuerons then the formula becomes,

wij = [-1/sqrt(3), 1/sqrt(3)]


## 2) Xavier / Glorot Intialisation:
In this there are two types of techniques

1) Xavier Normal Intialisation
2) Xavier Uniform Intialisation

1) Xavier Normal Intialisation:

wij follows Normal Distribution with mean 0 and S.D sigma.

where sigma = sqrt(2/(no of input + no of output))

2) Xavier Uniform Intialisation:

wij follows Uniform Distribution with [sqrt(-6/(no of input + no of output)), sqrt(6/(no of input + no of output))]


## 3) Kaiming he initialisation:

Here also we have two techniques

1) He Normal Intialisation
2) He Uniform Intialisation

1) He Normal Intialisation:

wij follows normal distribution with (0, sigma)
where
 
sigma = sqrt(2/(no of input))

2) He Uniform Intialisation:

wij follows uniform distribution with [sqrt(-6/no of input), sqrt(6/no of input)]


## Dropout layer:

By default, ANN also overfit the problem so to control the overfitting we use something called as dropout layer.

- We set some threshold value and with that threshold the no of neurons get deactivated randomly in the hidden layers in forward propogation.
- exa; if we set p = 0.5 then 50% of neurons in the hidden layer will get deactivated.
- We set this threshold with the help of hyperparameters.
- In back propogation, whichever nuerons was deactivated, their weights will not get updated.
- Again in forward propogation, the new neurons will get deactivated and not the same one.

- In test data, we only perform prediction based on whatever equation we get from training data.
- we will multiply the weights with the p-value for the particular layers