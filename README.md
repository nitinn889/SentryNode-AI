# SentryNode-AI: Edge-Based Intrusion Detection for Robotics
Project Overview :
This project implements a real-time security sentry for robotic swarms. It utilizes a machine learning model (Random Forest) deployed on a Raspberry Pi 4 to monitor and classify incoming network traffic, identifying potential cyber-attacks (DoS, Probing, R2L) with sub-20ms latency.

## 🛠 Tech Stack
Model: Random Forest Classifier (Scikit-Learn)

Hardware: Raspberry Pi 4 (Edge Node), MacBook Air (Simulation Node)

Backend: Flask REST API

Deployment: Joblib (Serialization), SCP

## 🚀 Implementation Details
Training: Performed in Google Colab using the NSL-KDD dataset.

Serialization: Exported model and LabelEncoders via Joblib to ensure data consistency across ARM and x86 architectures.

Inference: Flask-based API on the Pi handles real-time feature extraction and prediction.

Validation: A custom attack_sim.py script mimics adversarial traffic to stress-test the system.
