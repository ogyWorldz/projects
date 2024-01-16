import requests
import pandas as pd
from codes import codes

# OpenWeatherMap API key
API_KEY = ""
BASE_URL = "https://api.openweathermap.org/data/2.5/forecast?"

# Function to pull weather data


def weather_pull():
    data_list = []

    for code in codes:
        ZIP = code
        URL = BASE_URL + "zip=" + str(ZIP) + ",us&appid=" + API_KEY
        forecast = requests.get(URL).json()
        city = forecast['city']['name']

        for entry in forecast['list']:
            snow = entry.get('snow', {'3h': 0}).get(
                '3h', 0)  # Set to 0 if 'snow' is not present
            data = {
                'zipcode': ZIP,
                'city': city,
                'dt_txt': entry['dt_txt'],
                'temp': entry['main']['temp'],
                'feels_like': entry['main']['feels_like'],
                'humidity': entry['main']['humidity'],
                'main': entry['weather'][0]['main'],
                'description': entry['weather'][0]['description'],
                'snow': snow,

                # Add more fields as needed
            }
            data_list.append(data)

    # Create a DataFrame from the list of weather data
    df = pd.DataFrame(data_list)

    # Write the DataFrame to a CSV file
    df.to_csv('weather_data.csv', index=False)

    print("Weather data written to 'weather_data.csv'")
    print(df)


# Execute the weather_pull function
weather_pull()
