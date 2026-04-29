# 🛒 E-Commerce Fraud Guard AI: Behavioral Risk Engine
**An end-to-end Machine Learning solution for high-scale transaction security.**

![Project Status](https://img.shields.io/badge/Status-Live-green)
![Data Scale](https://img.shields.io/badge/Data-1.47M_Transactions-blue)
![Model](https://img.shields.io/badge/Model-Random_Forest-orange)

## 📌 Project Overview
This project addresses the critical challenge of e-commerce fraud by moving beyond static rules to dynamic **Behavioral Fingerprinting**. By analyzing **1.47 million transactions**, this AI identifies fraudulent patterns based on user behavior, network anomalies, and temporal risks.

## 🧠 Core AI Intelligence (15+ Engineered Features)
The system's predictive power comes from high-intent behavioral features:
* **Bot Detection:** Analyzing `Session Speed` and `Transaction Velocity`.
* **Fraud Ring Identification:** Tracking `IP Sharing` and `Address Sharing` counts.
* **Temporal Risk:** Evaluating `Account Age` vs. `Transaction Hour` to flag "Dark Hour" anomalies.

## 📊 Dashboard & Visualization
The project features a multi-page **Streamlit Dashboard** for real-time decision transparency:
1. **Transaction Risk Scoring:** A probability gauge for instant "Go/No-Go" decisions.
2. **Behavioral Breakdown:** Visualizing why a transaction was flagged (Feature Importance).
3. **Geospatial Insights:** Mapping transaction origins to detect location-based fraud clusters.

## 🛠️ Technical Stack
* **Core:** Python, Pandas, Scikit-Learn
* **UI/UX:** Streamlit
* **Data Management:** Git LFS (Large File Storage) for 700MB+ dataset versioning.
* **Architecture:** Random Forest Classifier (Optimized for low False-Positives).

## 🚀 How to Run Locally
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Poojaprasad16/Fraud-Guard-AI.git](https://github.com/Poojaprasad16/Fraud-Guard-AI.git)
   cd Fraud-Guard-AI
