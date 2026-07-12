import streamlit as st 
import requests
st.title("WEATHER FINDER -_-")
city = st.text_input("ENTER A CITY NAME: ")
if city:
        api_key = "761737b108da387ae1329c7c3c600658"
        base_url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "appid": api_key,
            "units": "metric"
        }

        response = requests.get(base_url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            st.success(f"**City:** {data['name']}")
            st.metric(label="Temperature", value=f"{data['main']['temp']}°C")
            st.write(f"**Weather:** {data['weather'][0]['description'].title()}")
            st.write(f"**Humidity:** {data['main']['humidity']}%")
        else:
            st.error("City not found or API error")