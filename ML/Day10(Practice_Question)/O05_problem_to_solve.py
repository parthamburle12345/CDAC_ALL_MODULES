import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from IPython.display import Image, display
from io import StringIO

input_file = "./assets/PastHires.csv"
df = pd.read_csv(input_file)
# print(df.head())

print("=" * 60)
# print(df.info())
# print("=" * 60)

# column_names = ["feature_name", "unique_values", "dtype"]
# df1 = pd.DataFrame([{ "feature_name": col, "unique_values": df[col].nunique(), "dtype": df[col].dtype.name } for col in df.columns])
# print(df1)
# print("=" * 60)

d = {'Y':1,'N':0,'BS':0, 'MS':1, 'PhD':2 }
df.replace(d, inplace=True)


for col in df.select_dtypes(include=np.object_).columns.to_list():
    df[col] = df[col].astype(int)


# scaling the features
features = list(df.columns[:6])
target = df.columns[6]
scaler = StandardScaler()
df[features] = scaler.fit_transform(df[features])


X = df[features]
y = df[target]

# split train and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = tree.DecisionTreeClassifier(random_state=42)
clf = clf.fit(X_train, y_train)
print("Decision Tree Classifier trained successfully.")
print("=" * 60)

# Predicting on the training data itself (for demonstration purposes)
y_pred_train = clf.predict(X_train)
accuracy_train = (y_pred_train == y_train).mean()
print("Accuracy on the training data:")
print(accuracy_train)

# Predicting on test data
y_pred_test = clf.predict(X_test)
accuracy_test = (y_pred_test == y_test).mean()
print("Accuracy on the test data:")
print(accuracy_test)
print("=" * 60)

# Visualize decision tree using matplotlib (native sklearn, no external pydotplus needed)
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 8))
tree.plot_tree(clf, feature_names=features, class_names=['Not Hired', 'Hired'], filled=True, rounded=True)
plt.title("Decision Tree for Past Hires")
plt.savefig("tree.png")
print("Saved tree visualization to 'tree.png'")
plt.close()