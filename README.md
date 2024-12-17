---

# **Federated Stress Detector**

Stress is a growing concern that negatively affects the health and well-being of a large portion of the global population. In this project, we address the **challenges of real-time stress classification** while ensuring **user data privacy** and utilizing **low-power edge devices**. 

Our system leverages **Federated Learning**, a flexible local database (**TinyDB**), and the **ESP32 microcontroller** to monitor stress biomarkers, process data locally, and aggregate global models in a privacy-preserving manner.

---

## **Project Overview**

This project introduces an **end-to-end solution** for stress detection through **biomarkers** collected from sensors connected to the ESP32 microcontroller. Key features of the system include:

1. **Federated Learning Framework**: 
   - Training stress classification models **locally** on edge devices.
   - Aggregating local models to build a **global model**, ensuring user data never leaves their devices.
   - Enhancing **data privacy** while enabling collaborative model training.

2. **Real-Time Analysis**:
   - Processing stress biomarkers **in real-time** on low-power hardware (ESP32).

3. **User-Friendly Interface**:
   - Visualizes collected data via intuitive **graphs and dashboards**.
   - Provides actionable insights for stress management.

4. **TinyDB Integration**:
   - A lightweight, flexible **local database** to store user data securely.
   - Users retain full ownership of their data and can export it as needed.

---

## **System Architecture**

The system architecture is designed to operate efficiently on edge devices, ensuring low latency and compatibility with resource-constrained hardware:

![System Diagram](https://github.com/rodrigoguedes09/Federated_Learning_Stress_Detector/assets/61996985/2a7f08ac-e379-4872-86ab-810e54fcc3e9)

---

## **Project Features**

### **1. Home Page Interface**

The home page serves as the main navigation hub, providing easy access to stress data visualization, tips, and settings:

![Home Page](https://github.com/rodrigoguedes09/Federated_Learning_Stress_Detector/assets/61996985/9ede9a3b-aa77-4c21-a5c8-647e4d8144f8)

### **2. Tips Page**

This page offers users actionable tips for managing stress based on collected data and analysis results:

![Tips Page](https://github.com/rodrigoguedes09/Federated_Learning_Stress_Detector/assets/61996985/6f8f9202-f84a-4333-aecd-d1151420ee98)

### **3. Data Visualization**

Users can visualize the data collected from the ESP32 microcontroller through intuitive, real-time graphs:

![Data Visualization](https://github.com/rodrigoguedes09/Federated_Learning_Stress_Detector/assets/61996985/0276c8d6-e177-40c2-a3da-93929ff250dc)

This visualization provides users with a **comprehensive overview** of their stress patterns, helping them make informed decisions.

---

## **Results and Conclusions**

The developed system successfully meets most of its objectives and requirements, demonstrating its **effectiveness for real-time stress classification**. Key outcomes include:

- **User Privacy**: Federated learning ensures that sensitive data remains local to the user's device, maintaining privacy while enabling the benefits of machine learning.  
- **Real-Time Functionality**: Stress biomarkers are processed locally on the ESP32, ensuring low latency and real-time feedback.  
- **Data Ownership**: Users can securely save their stress data locally using the **TinyDB database file**.  

**Unmet Requirements**:
- Functional requirements 2 and 3 remain incomplete but can be addressed in future iterations.

---

## **Future Work**

Several enhancements are planned to improve system performance and usability:

1. **Bluetooth/BLE Communication**: Replace WiFi communication via a router with **direct Bluetooth/BLE** connectivity to reduce infrastructure dependency.  
2. **On-Device Training**: Enable local training and federated learning **directly on the ESP32**, exploring lightweight libraries and alternative technologies.  
3. **Mobile Integration**: Implement the user interface as a **Progressive Web App (PWA)** or develop native apps for **Android** and **iOS** devices, improving accessibility and user experience.

---

## **Technologies Used**

- **ESP32 Microcontroller**: Low-power, real-time edge device for sensor data collection.  
- **Federated Learning**: Local model training and global aggregation for privacy-preserving machine learning.  
- **TinyDB**: Lightweight, flexible local database for secure data storage.  
- **Python**: Backend programming for data handling and model training.  
- **HTML/CSS/JavaScript**: Frontend development for user interface and data visualization.  

---

## **Contributors**

This project was developed by:  
- [Marcelo Custódio](https://github.com/marcelo-custodio)  
- [Rodrigo Guedes](https://github.com/rodrigoguedes09)  

As part of the **Bachelor's degree in Computer Engineering** at the **Federal University of Santa Catarina (UFSC)**, Brazil.

---

## **Final Notes**

This project showcases our knowledge and skills in **embedded systems**, **machine learning**, **edge computing**, and **software development**. By combining these areas, we developed an innovative solution to address stress classification while maintaining user privacy, offering a scalable foundation for future enhancements.

--- 
