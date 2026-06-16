# Weather App using OpenWeatherMap API

A simple Python command-line application that fetches and displays real-time weather information for any city using the OpenWeatherMap API.

## Features

* Get current weather details for any city worldwide
* Display temperature in Celsius
* Show "feels like" temperature
* Display weather conditions (e.g., Clear Sky, Rain, Clouds)
* Show humidity percentage
* Display wind speed
* Basic error handling for invalid city names or API keys

## Technologies Used

* Python 3
* `requests` library
* OpenWeatherMap API

## Prerequisites

Before running the application, ensure you have:

* Python 3 installed on your system
* A valid OpenWeatherMap API key
* The `requests` library installed

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

3. Get your API key from [OpenWeatherMap](https://openweathermap.org/api).

4. Open the Python file and replace:

```python
API_KEY = "API_KEY"
```

with your actual API key:

```python
API_KEY = "your_actual_api_key"
```

## Usage

Run the application using:

```bash
python weather.py
```

When prompted, enter the city name:

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
├── weather.py      # Main application file
├── README.md       # Project documentation
└── requirements.txt
```

## Error Handling

The application handles common errors such as:

* Invalid API key
* City not found
* Failed API requests

Example error message:

```text
Error: 401
City not found or API key is invalid.
```

## API Reference

This project uses the **Current Weather Data API** provided by OpenWeatherMap.

API Endpoint:

```text
https://api.openweathermap.org/data/2.5/weather
```

Documentation:

https://openweathermap.org/current

## Future Improvements

* Add weather forecast support (5-day / hourly forecast)
* Implement graphical user interface (GUI)
* Allow users to search by ZIP code or coordinates
* Add unit selection (Celsius/Fahrenheit)
* Improve exception handling using `try-except`

## License

This project is open source and available under the MIT License.

## Author

Created as a simple Python project to demonstrate API integration and JSON data handling using the OpenWeatherMap Weather API.
