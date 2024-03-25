import random
import time
import requests

# ThinkSpeak Credentials
API_Key = "VZH7SNBKHXEGW8FC"
THINGSPEAK_URL = "https://api.thingspeak.com/update"

# Randomly generate temp, humidity, and CO2 values
def generate_sensor_values():
    temperature = random.uniform(-50, 50)  # Range: -50 to 50 Celsius
    humidity = random.uniform(0, 100)      # Range: 0 to 100%
    co2 = random.uniform(300, 2000)        # Range: 300ppm to 2000ppm
    return temperature, humidity, co2

# Publish values to thingspeak
def publish_to_thingspeak(temperature, humidity, co2):
    data = {
        'api_key': API_Key,
        'field1': temperature,
        'field2': humidity,
        'field3': co2,
    }
    response = requests.get(THINGSPEAK_URL, params=data)
    print(f"Data published to ThingSpeak. Response Code: {response.status_code}")

def main():
    while True:
        temperature, humidity, co2 = generate_sensor_values()
        print(f"Temperature: {temperature:.2f}°C, Humidity: {humidity:.2f}%, CO2: {co2:.2f}ppm")
        
        # Publish the data to ThingSpeak
        publish_to_thingspeak(temperature, humidity, co2)

        # Adjust the sleep time as needed for your simulation speed and ThingSpeak's update frequency limitations
        time.sleep(20)  # ThingSpeak free account has an update limit of once every 15 seconds

if __name__ == "__main__":
    main()