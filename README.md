# Weather App 🌦️

A simple Python command-line application that fetches real-time weather information for any city using the OpenWeatherMap API.

## Features

* Get current weather data for any city
* Display temperature in Celsius
* Show "feels like" temperature
* Display weather conditions
* Show humidity percentage
* Display wind speed
* Handle invalid city names and API key errors

## Technologies Used

* Python 3
* Requests Library
* OpenWeatherMap API

## Installation

1. Clone this repository:

```bash
git clone https://github.com/your-username/weather-app.git
cd weather-app
```

2. Install the required dependency:

```bash
pip install requests
```

3. Get your API key from OpenWeatherMap.

4. Open the Python file and replace:

```python
API_KEY = "API_KEY"
```

with your actual API key:

```python
API_KEY = "your_api_key"
```

## Usage

Run the program:

```bash
python weather.py
```

Enter the city name when prompted:

```text
Enter city name: London
```

### Example Output

```text
Weather in London, GB
------------------------------
Temperature : 18.5°C
Feels Like  : 17.9°C
Condition   : Broken Clouds
Humidity    : 72%
Wind Speed  : 4.6 m/s
```

## Project Structure

```text
weather-app/
│
├── weather.py
└── README.md
```

## Error Handling

The application displays an error message if:

* The city name is invalid
* The API key is incorrect
* The API request fails

Example:

```text
Error: 401
City not found or API key is invalid.
```

## API Endpoint

```text
https://api.openweathermap.org/data/2.5/weather
```

### Parameters Used

| Parameter      | Description                     |
| -------------- | ------------------------------- |
| `q`            | City name                       |
| `appid`        | OpenWeatherMap API key          |
| `units=metric` | Displays temperature in Celsius |

## Future Improvements

* Add weather forecast support
* Allow temperature unit selection (Celsius/Fahrenheit)
* Improve exception handling using `try-except`
* Develop a graphical user interface (GUI)

## Author

Created as a Python project to demonstrate API integration and working with JSON data using the OpenWeatherMap API.
