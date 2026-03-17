import joblib
import numpy as np
from feature_extraction import extract_features

MODEL = joblib.load("ddos_model.pkl")

features = extract_features("traffic.pcap")

features = np.array(features).reshape(1, -1)

prediction = MODEL.predict(features)

if prediction == 1:
  print("DDoS Attack detected")
else:
  print("Normal Traffic")
  