## Exploratory Data Analysis (EDA)

The core machine learning pipeline consists of
1) Data Ingestion
2) Exploratory Data Analysis (EDA)
3) Data Pre-processing (Feature Engineering)
4) Model Building
5) Model Evaluation

There are three types of data:
1) Structured Data:- contains tabular data or which have target feature available in data.
2) Unstructured Data:- Contains video, image, text etc data.
3) Semi-structured Data:- Contains XML, JSON format data.


Now to again divide above Structured data in different parts:
1) Discrete Data:- This contains only integer that, which cannot be float such as No of chocolates
2) Continuous Data:- The data which can be integer as well as float such as Height, weight
3) Nominal Categorical Data:- Categorical data in which order of data dosen't matter such as gender
4) Ordinal Categorical Data:- Categorical data in which order is important such as Education.


There are three types of analysis on features:
1) Univariate Analysis:- Univariate analysis means the analysis performed on a single feature.
2) Bivariate Analysis:- Bivariate analysis means the analysis performed on two features.
3) Multivariate Analysis:- Multivariate analysis means the analysis performed on multiple features.



### **Steps to perform EDA**
1) Profile of the data
2) Statistical analysis
3) Graph based analysis

1) Profile of the data: Contains the analysis on following features
- No of rows
- No of columns
- Missing values
- No of categorical features
- No of numerical features
- No of duplicate records
- Datatype & datasize

2) Statistical Analysis: This will contain mainly the statistical interpretation of the data
- Measure of central tendancy like mean, median, mode.
- Variance of features
- Correlation, covariance of features
- different tests like t-test, z-test
- Skewness & Kurtosis of features

3) Graph based analysis: The analysis based on visual interpretation of features
- Boxplot
- Scatterplot
- Pie chart
- Histogram
- Kernel density estimation plot (kde plot)
- Heatmap


**Based on the EDA we can do some conclusion and interpretation about the data, and on the basis of that conclusion we can do pre-processing of data.**

### **Types of pre-processing or Feature engineering we can do on the data**
- Handling missing value
- Handling of outliers
- Handling duplicate data
- Scaling of the data
- Transformation of data like (log transformation, boxcox transformation)
- Encoding such as one hot encoding
- Handling imbalance data
- Feature selection
- Dimentionality reduction such as PCA




