# Federated Stress Detector

Stress is a growing concern that negatively affects the health and well-being of a large portion of the global population. In this context, we propose a system that addresses the challenges of stress classification, considering the sensitivity of personal data, real-time analysis and the use of low-power microcontrollers. By utilizing a Federated Learning framework, a real-time display interface, the flexible TinyDB database, and the ESP32 microcontroller, our system collects data through biomarkers and processes it in real-time, training stress classification models locally on edge devices. The federated models are aggregated to obtain a global model, which is then deployed to the devices. Experimental results demonstrate the effectiveness of this system for real-time stress classification, ensuring user privacy and highlighting the compatibility of these functionalities in edge computing.
This was a project developed by Marcelo Custódio [(https://github.com/marcelo-custodio)] and Rodrigo Guedes (https://github.com/rodrigoguedes09), with the objective of applying the necessary knowledge acquired on the Bachelor's degree in computer engineering at the Federal University of Santa Catarina, Brazil.

 ---
 
Basic modeling of the project system:


![image](https://github.com/rodrigoguedes09/Federated_Learning_Stress_Detector/assets/61996985/2a7f08ac-e379-4872-86ab-810e54fcc3e9)



Interface (HomePage)


![image](https://github.com/rodrigoguedes09/Federated_Learning_Stress_Detector/assets/61996985/9ede9a3b-aa77-4c21-a5c8-647e4d8144f8)



Interface (Tips page)


![image](https://github.com/rodrigoguedes09/Federated_Learning_Stress_Detector/assets/61996985/6f8f9202-f84a-4333-aecd-d1151420ee98)



Interface (Data visualization for the user)


![image](https://github.com/rodrigoguedes09/Federated_Learning_Stress_Detector/assets/61996985/0276c8d6-e177-40c2-a3da-93929ff250dc)

The visualization of the data obtained from the ESP32 is displayed in a graph, allowing the user to analyze and have a comprehensive view of their data.



# Conclusions

In general, the obtained results were positive; the developed system fulfills its objectives and requirements, except for functional requirements 2 and 3, and is user-friendly. User privacy can be preserved while still benefiting from machine learning possibilities due to the use of federated learning. The user remains the sole owner of their data and can save it wherever they want by keeping the generated TinyDB database file.

For future work, three changes are anticipated: (i) replacing WiFi communication via a router between the client and the data collector with Bluetooth or BLE, (ii) performing local training and federated learning directly on the ESP32, using other technologies or developing a new library, (iii) implementing the interface on mobile devices, such as a Progressive Web App (PWA) or natively on Android or iOS devices.



