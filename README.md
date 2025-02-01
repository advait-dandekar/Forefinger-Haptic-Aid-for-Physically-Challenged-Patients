# Forefinger-Haptic-Aid-for-Physically-Challenged-Patients

Physical rehabilitation is crucial for individuals recovering from hand injuries, neurological conditions like stroke, or other disabilities that affect fine motor skills and finger mobility. Conventional rehabilitation often requires repeated hand and finger exercises, which patients must practice consistently to regain strength, coordination, and flexibility. However, without consistent feedback, it is challenging for individuals to monitor their movements and ensure they perform exercises accurately. The Forefinger Haptic Aid Device is designed to address this need by providing real-time feedback on finger movement, helping users self-correct and perform exercises more effectively.

The Forefinger Haptic Aid Device combines hardware and IoT to create a wearable tool that provides sensory feedback and remote data monitoring. The device is built around the Raspberry Pi Pico W, a compact and affordable microcontroller with built-in Wi-Fi connectivity, enabling real-time data transmission to an accompanying mobile app. For movement detection, the device utilizes an ADXL335 accelerometer, a 3-axis sensor capable of tracking the tilt and acceleration of the finger in x, y, and z directions. Any unexpected or erratic movements detected by the accelerometer trigger a flat button-type vibration motor, delivering immediate haptic feedback to the user. This helps users maintain smoother, more controlled movements, which is essential for effective rehabilitation. We use the Blynk IoT App for data visualisation on smartphones.

The code can be found in the main.py file. 

Connection Diagram:


![image](https://github.com/user-attachments/assets/4e88c1cc-a6c3-4c03-8334-bb474fdde0a9)
