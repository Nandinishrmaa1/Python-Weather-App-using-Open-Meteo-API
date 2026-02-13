# 🌦️ Python Weather App (CLI)

A command-line Weather Application built using Python that fetches real-time weather data (temperature, wind speed, humidity) for any city.
The app uses the Open-Meteo API, includes proper error handling, stores search history, and provides a menu-based interface.

# 🚀 Features

- User input validation (name & city)

- City → Latitude/Longitude conversion (Geocoding API)

- Real-time weather data:

  - Temperature

  - Wind Speed

  - Relative Humidity

- Weather status classification (Hot / Warm / Cool / Cold)

- Date & time display

- File-based weather history (weather_history.txt)

- Menu-driven CLI:

  - Check Weather

  - View History

  - Exit

- Exception handling:

  - No internet

  - Timeout

  - Invalid city

  - Missing history file

# 🛠 Tech Stack

- Python

- Requests (API handling)

- REST APIs

- File Handling

- Exception Handling

# 📂 Project Structure
```
weather_app.py
weather_history.txt
README.md
```

# ▶ How to Run

1. Clone this repository:

```
git clone <your-repo-link>
```

2. Install dependencies:

```
pip install requests
```

3. Run the app:

```
python weather_app.py
```

# 🧠 What I Learned

- Working with REST APIs in Python

- Handling real-world errors (network issues, invalid input)

- Writing modular code using functions

- File handling for persistent data

- Building menu-based CLI applications

# 📌 Sample Output
```
Menu:
'1' -> Check weather
'2' -> View history
'3' -> Exit
Enter your choice : 1

Enter your name : Nandini
Enter your city : Indore

Hello Nandini!
Weather in Indore:
Date: 13 February 2026
Time: 14:10

Temperature : 28°C
Wind Speed : 12 km/h
Relative Humidity : 45%
Weather Status: Warm

2026-02-13 | Indore | 28°C | Warm

```

# 🌟 Future Improvements

- GUI version (Tkinter)

- Flask web version

- Weather forecast charts

- Colored terminal output

# 💌 Author

Nandini Sharma
