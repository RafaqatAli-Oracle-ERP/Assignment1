from meta_ai_api import MetaAI

ai = MetaAI()
user_input = input("Enter the country name:")
prompt=f"""You are custom gpt you have to tell about the weather of any country user asked 
                    user asked for {user_input}
                    you have to tell the weather of the country in the following format:
                    - Temperature: 20°C
                    - Weather: Sunny
                    - Wind: 10 km/h
                    - Humidity: 50%
                    - Precipitation: 0 mm
                    - Cloud cover: 50%
                    - Wind direction: North
                    - Wind speed: 10 km/h
                    - Visibility: 10 km
                    - Pressure: 1000 hPa
                    - Dew point: 10°C
                    - UV index: 10
                    - Sunrise: 06:00
                    - Sunset: 18:00
                    - Moon phase: Full moon
                    - Moon illumination: 100%

                    and if the user asked something else you have to tell that you are not able cable of that 
                """
response = ai.prompt(message=prompt)
print(response["message"])
