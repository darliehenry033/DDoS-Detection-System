# Machine Learning DDoS Detection System

## Overview
This project is a **Machine Learning-based DDoS Detection System** designed to identify malicious network traffic in real time. It combines **network traffic analysis** with **supervised learning** to detect Distributed Denial-of-Service (DDoS) attacks.

The system was developed as part of a hands-on cybersecurity lab, where attack scenarios were simulated and analyzed in a controlled environment.

---

## Key Features
- Real-time network traffic monitoring  
- Machine Learning-based attack detection  
- Trained classification model for DDoS vs normal traffic  
- Lightweight and modular design  
- Attack simulation and testing in a virtual lab  

---

## Technologies Used
- Python  
- scikit-learn  
- pandas  
- Scapy  
- Matplotlib  

---

## Machine Learning Model
The detection system uses a **Random Forest Classifier** trained on network traffic data.

### Dataset
- CICIDS2017 dataset  

### Features Used
- Packet rate  
- Flow duration  
- Packet size statistics  
- Traffic patterns  

### Output
- `0` → Normal Traffic  
- `1` → DDoS Attack  

---

## System Architecture

  Network Traffic
│
▼
Packet Capture (Scapy)
│
▼
Feature Extraction
│
▼
ML Model Prediction
│
▼
DDoS Alert

## Future Improvements
- Deep learning-based detection (LSTM / Neural Networks)
-	Web-based monitoring dashboard
-	Containerized deployment using Docker
- Integration with real-time network monitoring tools



