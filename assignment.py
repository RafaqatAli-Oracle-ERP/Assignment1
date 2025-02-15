import streamlit as st
import random

# Mock MetaAI class for demonstration
class MetaAI:
    def prompt(self, message):
        # Mock response with random weather data
        temp = random.randint(15, 30)
        humidity = random.randint(40, 80)
        wind_speed = random.randint(5, 20)
        
        mock_weather = f"""You are custom gpt you have to tell about the weather of any country 
        user asked for {message}
        you have to tell the weather of the country in the following format:
        - Temperature: {temp}°C
        - Weather: Sunny
        - Wind: {wind_speed} km/h
        - Humidity: {humidity}%
        - Precipitation: 0 mm
        - Cloud cover: 30%
        - Wind direction: North
        - Wind speed: {wind_speed} km/h
        - Visibility: 10 km
        - Pressure: 1013 hPa
        - Dew point: {temp-5}°C
        - UV index: 7
        - Sunrise: 06:00
        - Sunset: 18:00
        - Moon phase: Full moon
        - Moon illumination: 100%
        """
        return {"message": mock_weather}

def main():
    # Set up page config
    st.set_page_config(page_title="Weather Information", page_icon="🌤️")
    
    # Add title and description
    st.title("🌍 Global Weather Information")
    st.write("Enter a country name to get detailed weather information")
    
    # Initialize MetaAI
    ai = MetaAI()
    
    # Create input field
    user_input = st.text_input("Enter the country name:", "")
    
    # Add a submit button
    if st.button("Get Weather Info"):
        if user_input:
            prompt = f"""You are custom gpt you have to tell about the weather of any country user asked 
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
            
            with st.spinner("Fetching weather information..."):
                response = ai.prompt(message=prompt)
                st.markdown(response["message"])
        else:
            st.warning("Please enter a country name")

if __name__ == "__main__":
    main()
