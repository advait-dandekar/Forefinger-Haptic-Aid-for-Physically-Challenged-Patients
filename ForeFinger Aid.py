#NEW CODEEEEE
# Import necessary libraries
import machine
import utime
import BlynkLib
import network

# Blynk setup
BLYNK_AUTH = 'eRga85RPV-v9sUmhkDWk89kdipcGn3Xg'  # Replace with your Blynk Auth Token
WIFI_SSID = 'Airtel_7471'  # Replace with your Wi-Fi SSID
WIFI_PASSWORD = 'air45747'  # Replace with your Wi-Fi password

# Initialize Wi-Fi connection
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(WIFI_SSID, WIFI_PASSWORD)

while not wifi.isconnected():
    pass
print('Connected to Wi-Fi:', wifi.ifconfig())

# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Define pin connections
X_Pin = 26
Y_Pin = 27
Z_Pin = 28
Motor_Pin = 14  # Pin for the vibration motor

# Create ADC objects for each axis
adc_x = machine.ADC(machine.Pin(X_Pin))
adc_y = machine.ADC(machine.Pin(Y_Pin))
adc_z = machine.ADC(machine.Pin(Z_Pin))

# Create a Pin object for the vibration motor
motor_pin = machine.Pin(Motor_Pin, machine.Pin.OUT)

# Function to read and process signals from the ADXL335
def read_acceleration(adc):
    # Read the ADC value and convert it into voltage
    voltage = adc.read_u16() * 3.3 / 65535
    # Convert the voltage to acceleration (assuming 3.3V supply)
    acceleration = (voltage - 1.65) / 0.330  # Conversion factor in g's
    return acceleration

# Function to activate the vibration motor
def activate_motor(duration_ms):
    motor_pin.on()  # Turn on the motor
    utime.sleep_ms(duration_ms)  # Wait for the specified duration
    motor_pin.off()  # Turn off the motor

# Function to check for significant movements and send notifications
def check_movement(x, y, z):
    # Define thresholds for movement detection
    horizontal_threshold = 1.00  # Threshold for horizontal movement
    vertical_threshold = 1.00  # Threshold for vertical movement
    diagonal_threshold = 1.00

    # Check for significant horizontal movement
    if abs(x) > horizontal_threshold:
        print("Warning: Significant horizontal movement detected!")
        activate_motor(1000)  # Vibrate for 200 milliseconds
        blynk.virtual_write(4, "Warning: Significant horizontal movement detected!")

    # Check for significant vertical movement
    if abs(y) > vertical_threshold:
        print("Warning: Significant vertical movement detected!")
        activate_motor(1000)  # Vibrate for 200 milliseconds
        blynk.virtual_write(4, "Warning: Significant vertical movement detected!")

    # Check for excessive z-axis movement, which could indicate instability
    if abs(z) > diagonal_threshold:  # Adjust this threshold as needed
        print("Warning: Sudden vertical movement detected!")
        activate_motor(1000)  # Vibrate for 200 milliseconds
        blynk.virtual_write(4, "Warning: Sudden diagonal movement detected!")

# Main loop
while True:
    blynk.run()  # Run Blynk to keep the connection active

    # Read the acceleration values from the ADXL335
    x = read_acceleration(adc_x)
    y = read_acceleration(adc_y)
    z = read_acceleration(adc_z)

    # Send the acceleration data to Blynk
    blynk.virtual_write(1, x)  # Send x-axis value to Virtual Pin V1
    blynk.virtual_write(2, y)  # Send y-axis value to Virtual Pin V2
    blynk.virtual_write(3, z)  # Send z-axis value to Virtual Pin V3

    # Print the acceleration values
    print("X: {:.2f}g, Y: {:.2f}g, Z: {:.2f}g".format(x, y, z))

    # Check for significant movements and send notifications
    check_movement(x, y, z)

    # Wait before reading again
    utime.sleep(1)
