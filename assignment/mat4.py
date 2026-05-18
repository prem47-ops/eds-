# Import libraries
import pandas as pd
import numpy as np

# ML libraries
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, confusion_matrix

# -----------------------------
# STEP 1: Load Real Dataset (Iris)
# -----------------------------
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target

print("Dataset Preview:\n", df.head())

# -----------------------------
# STEP 2: LINEAR REGRESSION
# Goal: Predict sepal length
# -----------------------------
X_reg = df[['sepal width (cm)', 'petal length (cm)', 'petal width (cm)']]
y_reg = df['sepal length (cm)']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)

# Train model
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

# Predictions
y_pred = lr_model.predict(X_test)

# Evaluation
print("\n===== LINEAR REGRESSION =====")
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# -----------------------------
# STEP 3: KNN CLASSIFIER
# Goal: Classify flower species
# -----------------------------
X_cls = df.drop('target', axis=1)
y_cls = df['target']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X_cls, y_cls, test_size=0.2, random_state=42)

# Train model
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Predictions
y_pred_knn = knn.predict(X_test)

# Evaluation
print("\n===== KNN CLASSIFIER =====")
print("Accuracy:", accuracy_score(y_test, y_pred_knn))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_knn))

# -----------------------------
# STEP 4: Test with New Data
# -----------------------------
sample = np.array([[5.1, 3.5, 1.4, 0.2]])
prediction = knn.predict(sample)

print("\nNew Sample Prediction (KNN):", prediction)

print("\n===== MODEL EXECUTION COMPLETED =====")
