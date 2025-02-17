import streamlit as st
from meta_ai_api import MetaAI

def main():
    # Page configuration
    st.set_page_config(page_title="Weather Assistant", page_icon="🌤️")
    
    # Title and description
    st.title("🌍 Weather Assistant")
    st.write("Get weather information for any country")
    
    # Initialize MetaAI
    llm = MetaAI()
    
    # Create input field
    user_input = st.text_input("Enter a country name:", placeholder="e.g., France")
    
    # Add a button to get weather
    if st.button("Get Weather"):
        if user_input:
            with st.spinner("Fetching weather information..."):
                prompt = f"""You are a weather assistant. Provide weather information for {user_input}.
                Format your response exactly like this:
                - Temperature: 20°C
                - Weather: Sunny
                - Wind: 10 km/h
                - Humidity: 50%

                If the input is not a country, respond with: "I can only provide weather for countries."
                """
                
                try:
                    response = llm.prompt(prompt)
                    st.subheader("Weather Information:")
                    st.info(response["message"])
                except Exception as e:
                    st.error("Error getting weather information. Please try again.")
        else:
            st.warning("Please enter a country name.")

if __name__ == "__main__":
    main()