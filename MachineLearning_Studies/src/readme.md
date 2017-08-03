Author: Manish Rai <br>
Email: manish.rai21bit@gmail.com, rai00007@umn.edu <br>

=============================================================================

CSCI 5525 - This directory contains python scripts for the following based on the learnings from the book Pattern Recognition and Machine Learning, by Christopher M. Bishop.

There are 4 executable python scripts:
    1. Fisher: Fisher Discriminant Analysis + Multivariate Gaussian Classifier for multi-class classification problem
    2. SqClass: Least Square Discriminant for multi-class classification problem
    3. logisticRegression: Logistic Regression for two-class classification problem
    4. naiveBayesDiscrete: Naive Bayes Model with Univariate Gaussian Approximation for multi-class classification problem

Requirements for running python scripts:
    python 2.7
    matplotlib 1.4.3 (optional, only for 'plot_naivebayes_logreg.py')

Requirements for the dataset:
    1. Must be in .csv format
    2. Header is not allowed in the dataset
    3. Row for cases, column for features
    4. The first column should be the indicator of classes
    5. Missing value is not allowed in the dataset
    6. Logistic Regression in this project only supports two-class problems
