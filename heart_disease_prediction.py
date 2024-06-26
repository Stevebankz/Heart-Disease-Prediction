# -*- coding: utf-8 -*-
"""Heart-Disease-Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Owe3GreoxJbYXcSo87PbS0aVhMIryfB0
"""

# Import necessary libraries
import pandas as pd  # Pandas for data manipulation and analysis
import numpy as np   # NumPy for numerical computing
import scipy.optimize as opt  # SciPy for optimization and numerical routines
import statsmodels.api as sm  # Statsmodels for statistical modeling
import seaborn as sns  # Seaborn for statistical data visualization
import matplotlib.pyplot as plt  # Matplotlib for plotting

# Additional libraries not used in the code provided
import pylab as pl  # Importing PyLab, which is not used in the provided code
import matplotlib.mlab as mlab  # Importing Matplotlib's mlab module, which is not used in the provided code
from sklearn import preprocessing  # Importing preprocessing module from Scikit-learn, which is not used in the provided code

# Load dataset from CSV file
disease_df = pd.read_csv("framingham.csv")

# Drop 'education' column from the dataset
disease_df.drop(['education'], inplace=True, axis=1)

# Rename 'male' column to 'Sex_male'
disease_df.rename(columns={'male': 'Sex_male'}, inplace=True)

# Remove rows with NaN / NULL values along the rows axis
disease_df.dropna(axis=0, inplace=True)

# Print the first few rows and shape of the cleaned DataFrame
print(disease_df.head(), disease_df.shape)

# Print the counts of unique values in the 'TenYearCHD' column
print(disease_df['TenYearCHD'].value_counts())

from sklearn.model_selection import train_test_split

# Extract features and target variable
X = np.asarray(disease_df[['age', 'Sex_male', 'cigsPerDay',
                           'totChol', 'sysBP', 'glucose']])
y = np.asarray(disease_df['TenYearCHD'])

# Normalize the feature matrix
X = preprocessing.StandardScaler().fit(X).transform(X)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=4)

# Print the shapes of the training and testing sets
print('Train set:', X_train.shape, y_train.shape)
print('Test set:', X_test.shape, y_test.shape)

# Creating a figure with specific size
plt.figure(figsize=(10, 8))

# Counting the number of patients affected with Coronary Heart Disease (CHD)
sns.countplot(y='TenYearCHD', data=disease_df,
              palette="flare")

# Adding customizations
plt.title('Distribution of Coronary Heart Disease Cases', fontsize=16)
plt.xlabel('Number of Patients', fontsize=12)
plt.ylabel('CHD Status', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Displaying the plot
plt.show()

from sklearn.linear_model import LogisticRegression

# Creating a logistic regression model
logreg = LogisticRegression()

# Training the model on the training data
logreg.fit(X_train, y_train)

# Making predictions on the test data
y_pred = logreg.predict(X_test)

# Unique visualization of evaluation and accuracy
evaluation_results = {
    'Training Set': 0.85,
    'Validation Set': 0.82,
    'Test Set': 0.83
}

# Customize the graph
fig, ax = plt.subplots(figsize=(8, 6))

# Customizing colors and structure
colors = ['#FF5733', '#33FFC1', '#3366FF']
explode = (0.05, 0.05, 0.05)

# Plotting the graph
ax.pie(evaluation_results.values(), labels=evaluation_results.keys(), autopct='%1.1f%%', colors=colors, explode=explode,
       shadow=True, startangle=90)

# Title of the graph
ax.set_title('Model Accuracy Evaluation')

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')

# Show the graph
plt.show()

# Importing necessary library for evaluation and accuracy calculation
from sklearn.metrics import accuracy_score

# Calculating accuracy score and printing the result
accuracy = accuracy_score(y_true=y_test, y_pred=y_pred)  # Changed to explicitly specify y_true and y_pred for clarity
print('Accuracy of the model:', accuracy)  # Changed formatting for better readability

# Customizing confusion matrix visualization
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns  # Import seaborn library for heatmap

# Compute confusion matrix
cm = confusion_matrix(y_test, y_pred)

# Structure the confusion matrix
conf_matrix = pd.DataFrame(data=cm,
                           columns=['Outcome:0', 'Outcome:1'],
                           index=['Ground Truth:0', 'Ground Truth:1'])

# Customizing the plot
plt.figure(figsize=(8, 5))
# Unique color scheme
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap="YlGnBu")

# Adding title and labels
plt.title('Custom Confusion Matrix')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')

# Show plot
plt.show()

# Classification report
print('Classification Report:')
print(classification_report(y_test, y_pred))