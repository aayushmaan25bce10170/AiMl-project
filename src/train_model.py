import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

df = pd.read_csv("data.csv")
df = df.drop(['ID','age_desc','relation'], axis=1)

df['austim'] = df['austim'].map({'yes':1,'no':0})

df = pd.get_dummies(df)

X = df.drop('austim', axis=1)
y = df['austim']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)

print("Accuracy:", acc)

pickle.dump(model, open("model.pkl", "wb"))

print("Model saved!")


import matplotlib.pyplot as plt

# Feature importance
importances = model.feature_importances_
features = X.columns

# Sort for better graph
indices = importances.argsort()[-10:]  # top 10 features

plt.figure()
plt.barh(range(len(indices)), importances[indices])
plt.yticks(range(len(indices)), [features[i] for i in indices])
plt.xlabel("Importance")
plt.title("Top Feature Importance")

plt.show()