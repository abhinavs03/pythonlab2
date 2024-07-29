weather_data = [
    {"date": "2024-08-01", "max_temp": 31, "min_temp": 24, "humidity": 70},
    {"date": "2024-08-02", "max_temp": 33, "min_temp": 25, "humidity": 65},
    {"date": "2024-08-03", "max_temp": 29, "min_temp": 22, "humidity": 72},
    {"date": "2024-08-04", "max_temp": 35, "min_temp": 26, "humidity": 60},
    {"date": "2024-08-05", "max_temp": 28, "min_temp": 21, "humidity": 75},
    {"date": "2024-08-06", "max_temp": 30, "min_temp": 23, "humidity": 68},
    {"date": "2024-08-07", "max_temp": 32, "min_temp": 24, "humidity": 67},
    {"date": "2024-08-08", "max_temp": 31, "min_temp": 25, "humidity": 64},
    {"date": "2024-08-09", "max_temp": 34, "min_temp": 27, "humidity": 62},
    {"date": "2024-08-10", "max_temp": 36, "min_temp": 28, "humidity": 59},
]

def find_high_low_temps(data):
    if not data:
        return None, None
    
    max_temp = max(day["max_temp"] for day in data)
    min_temp = min(day["min_temp"] for day in data)
    
    return max_temp, min_temp

def count_days_above_temp(data, temp_threshold):
    return sum(1 for day in data if day["max_temp"] > temp_threshold)

def average_humidity(data):
    if not data:
        return 0
    
    total_humidity = sum(day["humidity"] for day in data)
    return total_humidity / len(data)

if __name__ == "__main__":
    highest_temp, lowest_temp = find_high_low_temps(weather_data)
    print(f"Highest Temperature: {highest_temp}°C")
    print(f"Lowest Temperature: {lowest_temp}°C")

    days_above_30 = count_days_above_temp(weather_data, 30)
    print(f"Number of days with temperatures above 30°C: {days_above_30}")

    avg_humidity = average_humidity(weather_data)
    print(f"Average Humidity: {avg_humidity:.2f}%")


'''
Highest Temperature: 36°C
Lowest Temperature: 21°C
Number of days with temperatures above 30°C: 7
Average Humidity: 66.20%
'''
