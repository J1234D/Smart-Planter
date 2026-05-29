import random

#Fake Sensor Data (for testing only)
def get_sensor_data():
    return {
        "moisture": random.randint(20, 80),
        "ph": round(random.uniform(5.0, 8.0), 1),
        "temperature": random.randint(20, 40)
    }
   