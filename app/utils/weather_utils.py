"""
Util functions for weather route

"""
def extract_temperature(weather_data: dict) -> list[dict]:
    temperatures = []
    print(weather_data)

    for entry in weather_data["timeSeries"]:
        valid_time = entry["time"]
        temperature = entry["data"]["air_temperature"]

        temperatures.append({
            "time": valid_time,
            "air_temperature": temperature
        })
    
    return temperatures