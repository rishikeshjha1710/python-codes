import random
import time

class TemperatureSensor:
    def __init__(self):
        self.temperature = 0
    
    def read_temperature(self):
        # Simulate temperature reading
        self.temperature = random.uniform(20, 100)
        return self.temperature

class FireDetector:
    def __init__(self, threshold):
        self.threshold = threshold
        self.sensor = TemperatureSensor()
    
    def check_temperature(self):
        temperature = self.sensor.read_temperature()
        if temperature > self.threshold:
            return True
        return False

class Alarm:
    def ring(self):
        print("ALARM: Fire detected! Sound the alarm!")

def main():
    # Set threshold temperature
    threshold_temperature = 80
    
    # Initialize fire detector and alarm
    fire_detector = FireDetector(threshold_temperature)
    alarm = Alarm()
    
    try:
        while True:
            if fire_detector.check_temperature():
                alarm.ring()
                # For demonstration purposes, halt execution after sounding the alarm
                break
            else:
                print("Temperature normal. Monitoring...")
            time.sleep(1)  # Check temperature every second
    except KeyboardInterrupt:
        print("Program terminated.")

if __name__ == "__main__":
    main()
