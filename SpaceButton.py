import serial
import pyautogui
import time

# Replace 'COM_PORT' with the actual COM Port your microcontroller is connected to.
ser = serial.Serial('COM10', 115200, timeout=1)
ser.flush()

while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        if line == "Blink Detected":
            print("Blink Detected")
            
            # Simulate key down           
            pyautogui.keyDown('space')

            # Add a delay for keypress duration (adjust as needed)
            time.sleep(0.5)  # Adjust the duration of the keypress

            # Simulate key up
            pyautogui.keyUp('space')
     
 