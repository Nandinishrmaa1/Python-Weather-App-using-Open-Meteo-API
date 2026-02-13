#package for API handling
import requests
#package for date and time handling
from datetime import datetime

#Function to take user input (name and city)
def input_data():
    while True:
        name = input("Enter your name : ").strip()
        city = input("Enter your city : ").strip()
        if name != "" and city != "":
            return name,city        
        elif name == "" and city != "":
            print("Name is empty")
        elif name != "" and city == "":
            print("City is empty")
        else:
            print("Both are empty")


#Function to get latitude and longitude of a city
def get_coordinates(city):
    #handle error if internet not available
    try:
        url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            
            if "results" in data and len(data["results"]) > 0:
                return data["results"][0]["latitude"] , data["results"][0]["longitude"]
            else:
                print("City not found")
                return None, None
        else :
            print(f"Error : {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("No Internet Connection")
        return None, None
    except requests.exceptions.Timeout:
        print("Request timed out")
        return None,None
    except requests.exceptions.RequestException:
        print("Something went wrong")
        return None,None
    except Exception as e :
        print(e)
        return None,None



#Function to fetch weather data using latitude and longitude
def get_weather(latitude,longitude):
    #handle error if internet not available
    try:
        #api url for fetching weather data based on lat&lon
        url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m,relative_humidity_2m"
        #store response from url
        response = requests.get(url)
        
        if response.status_code == 200:
            #store json response
            data = response.json()
            #return temp,wind speed, humidity
            return data["current"]["temperature_2m"], data["current"]["wind_speed_10m"], data["current"]["relative_humidity_2m"]
        else:
            print(f"Error : {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("No Internet Connection")
        return None
    except requests.exceptions.Timeout:
        print("Request timed out")
        return None
    except requests.exceptions.RequestException:
        print("Something went wrong")
        return None
    except Exception as e:
        print(e)
        return None


#Menu's 1st option 
def check_weather():
# Inside this loop, the following steps occur:
    #1. input from user for name and city, 
    #2. current datetime, 
    #3. lat&lon for city, 
    #4. fetch weather data (temp,wind speed, humidity),
    #5. store info in weather history file
    while True:
        name , city = input_data()
        print(f"Hello {name}!\nWeather in {city}:")
    
        dt = datetime.now() 
        print(f"Date: {dt.strftime('%d')} {dt.strftime('%B')} {dt.strftime('%Y')}\nTime: {dt.strftime('%H')}:{dt.strftime('%M')}")
       
        #lat&lon for city 
        latitude,longitude = get_coordinates(city)
          
        if latitude is not None and longitude is not None:
            #weather info for city based on lat&lon
            result = get_weather(latitude,longitude)
            if result is not None:
                temperature, wind_speed, relative_humidity = result
                print(f"Temperature : {temperature}°C\nWind Speed : {wind_speed}km/h\nRelative Humidity : {relative_humidity}%")
                if temperature >= 30:
                    weather_status = "Hot"
                elif temperature >= 20:
                    weather_status = "Warm"
                elif temperature >= 10:
                    weather_status = "Cool"
                else:
                    weather_status = "Cold"
                print(f"Weather Status: {weather_status}")
                info = f"{dt.strftime('%Y')}-{dt.strftime('%m')}-{dt.strftime('%d')} | {city} | {temperature}°C | {weather_status}"
                print(info)
                with open("weather_history.txt","a") as f:
                    f.writelines([info,"\n"])
    
        else:
            print("Cannot fetch Weather")
    
    
        #for checking another city
        again = input("Do you want to check another city? (yes/no) ").lower()
        if again == 'yes' or again == 'y':
            continue
        else:
            print("goodbye")
            break

#Menu's 2nd option
def view_history():
    #handle error if weather history file not exists 
    try:
        with open("weather_history.txt","r") as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print("No history yet.")



#menu:
def menu(x):
    if x == 1:
        check_weather()
    elif x == 2:
        view_history()
    else:
        print("This is not in menu!")

# This loop runs until the user selects the Exit option
while True:
    #Menu
    print("Menu:")
    print("'1' -> Check weather")
    print("'2' -> View history")
    print("'3' -> Exit")
    #handle error if user enter invalid value 
    try : 
        x = int(input("Enter your choice : "))
        if x == 3:
            break
        menu(x)
    except ValueError:
        print("This input is not valid!")