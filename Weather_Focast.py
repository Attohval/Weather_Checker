import requests
api_key = "" #Define your API key first
       #Program created by Valentine Attoh
base_url = "http://api.openweathermap.org/data/2.5/weather?" #Set your URL

print("WEATHER CHECKER")  
city_name = input("Enter city name: ") #Prompt user for the city name

#Complete URL with the city name and API key
complete_url = base_url + "q=" + city_name + "&appid=" + api_key + "&units=metric"

response = requests.get(complete_url) #Make a GET request to the complete_url
      #Program created by Valentine Attoh
data = response.json()#Parse the JSON data received from the API

if response.status_code == 200: #Check if the response contains the expected data
    try:
        main = data["main"]
        weather = data["weather"][0]
        #Program created by Valentine Attoh
        # Extract relevant data        
        temperature = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        weather_description = weather["description"]
        
        # Print the weather details
        print("")
        print(f"Temperature: {temperature}°C")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Weather description: {weather_description}")
        #Program created by Valentine Attoh
    except KeyError:
        print("Error: Unable to retrieve weather data. Please check the city name and try again.")
else:
    print(f"Error: {data['message']}")
