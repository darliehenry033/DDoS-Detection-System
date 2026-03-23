import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

data = pd.read_csv("Syn.csv", low_memory=False)


X = data[[' Bwd Packet Length Min','Bwd Packet Length Max',' Bwd Packet Length Mean']]
y = data[' Label']

X_train, X_test, y_train, y_test = train_test_split(
  X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier( random_state=42)

model.fit(X_train, y_train)


accuracy = model.score(X_test, y_test)

print("Model accuracy: ", accuracy)
joblib.dump(model, "ddos_model.plk")
