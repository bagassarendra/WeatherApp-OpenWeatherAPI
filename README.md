# Weather App

A simple weather application built using Python and Tkinter that retrieves current weather data from the **OpenWeatherMap** API. The app allows users to search for weather information by entering the city name and displays the temperature, humidity, wind speed, and weather condition, along with the country's name.

## Features

- Get current weather information (temperature, humidity, wind speed, etc.) for any city.
- Supports multiple units for wind speed and temperature.
- Displays the weather condition and feels-like temperature.
- Simple, user-friendly GUI built using Tkinter.

## Requirements

- Python 3.x
- Libraries:
  - `requests` (for making API requests)
  - `tkinter` (for creating the GUI)
  - `python-dotenv` (for loading the API key securely from `.env` file)

You can install the required libraries using `pip`:

```bash
pip install requests python-dotenv
