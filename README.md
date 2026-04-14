# AI-Based DDoS Detection System (C++ + Python ML Pipeline)

## 📌 Overview
This project is a machine learning–based network traffic analysis system designed to detect abnormal network behavior such as potential DDoS patterns.

The system simulates network traffic using synthetic packet generation and extracts statistical features from PCAP files for classification.

The goal of this project is to demonstrate applied knowledge in:
- Network security fundamentals
- Feature engineering for ML
- Cybersecurity anomaly detection
- System design for real-world data pipelines

---

## 🧠 Project Pipeline

1. Synthetic network traffic generation (normal + anomalous patterns)
2. PCAP file creation using Scapy
3. Feature extraction from network packets
4. Machine learning model training (Random Forest)
5. Traffic classification (Normal vs Anomaly)

---

## 📊 Traffic Simulation Strategy

To ensure safe and controlled experimentation, the dataset includes:

### Normal Traffic
- Standard TCP ACK traffic
- Randomized source IPs and ports
- Low and stable packet rate

### Anomalous Traffic (Simulated)
- Burst-based SYN request patterns
- High-frequency packet generation within short time windows
- Randomized source behavior to simulate distributed activity

---

## ⚙️ Feature Extraction

From each PCAP file, the following features are extracted:

- Total packet count
- SYN packet ratio
- Average packet size

These features are used to represent network behavior in numerical form for machine learning.

---

## 🛠️ Technologies Used

- Python
- Scapy (packet manipulation)
- Pandas (data processing)
- Scikit-learn (machine learning)
- C++ (supporting data processing components)

---

## 📁 Example Workflow

### 1. Generate Synthetic Traffic
- Create normal and anomalous traffic patterns
- Save as `traffic.pcap`

### 2. Feature Extraction
- Parse PCAP file
- Compute statistical features

### 3. Model Training
- Train classifier using labeled dataset
- Evaluate performance

### 4. Prediction
- Classify incoming traffic as:
  - Normal
  - Anomalous

---

## 📈 Model Output

The model classifies network traffic based on learned behavior patterns derived from packet-level features.


---

## 💡 Key Learnings

- Understanding of network packet structure (TCP/IP)
- Feature engineering for cybersecurity ML
- Importance of balanced datasets
- Limitations of synthetic data in real-world generalization
- Detection of burst-based anomalies in traffic flows

---

## ⚠️ Known Limitations

- Synthetic dataset does not fully represent real-world internet traffic
- Limited feature set may reduce detection accuracy in complex scenarios
- Model may require additional tuning for real deployment environments

---

## 🚀 Future Improvements

- Integrate real-world datasets (CICIDS, UNSW-NB15)
- Add time-window based feature extraction
- Implement real-time packet sniffing detection
- Improve anomaly scoring (unsupervised learning)
- Deploy as a real-time monitoring system

---

## 👤 Author
Darlie Henry  
GitHub: https://github.com/darliehenry033