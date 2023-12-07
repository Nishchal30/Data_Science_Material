## Overfitting VS Underfitting (Bias & Variance)

If we have the dataset with 1000 records, then we will divide the dataset into train & test datasets.

- let's say training dataset contains 700 records out of 1000 and we will train our model on this 700 records
- test dataset contains 300 records out of 1000 records and the fitted model will be tested on this 300 records.

Now again further our training dataset which has 700 records, will be divided into two parts
- Training so this can be contain 500 records out of 700 for training the model
- Validation so this can be contain 200 records out of 700 for hyper parameter tuning the model

Now in general,
we need to get very good accuracy in training data and also very good accuracy in test data

**Bias** is related to training data accuracy.
**Variance** is related to test data accuracy.

**when we get very good accuracy in training data we call it as Low Bias**
**when we get very good accuracy in test data we call it as Low Variance**


**When the training data accuracy is very good i.e. Low Bias but the test data accuracy is very low i.e. High Variance called as Overfitting**

**When the training data accuracy is very low i.e. High Bias and the test data accuracy is either low or high i.e. Low/High Variance called as Underfitting**
