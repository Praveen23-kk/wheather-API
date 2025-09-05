# 🌦️ Weather API Django Web App

A simple and elegant Django-based web application that fetches and displays real-time weather data from the OpenWeatherMap API.

## 📖 Project Description

This project allows users to get the current weather information for any city in the world. It's built with Django and uses the OpenWeatherMap API to fetch real-time data. This application is a great starting point for anyone looking to build a web app with Django and integrate with a third-party API.

## 🚀 Features

-   **Real-Time Weather Data:** Get up-to-date weather information.
-   **Search by City:** Users can search for any city to get weather details.
-   **Detailed Information:** Displays temperature, humidity, pressure, weather conditions, and coordinates.
-   **User-Friendly Interface:** A clean and simple UI for easy use.
-   **Error Handling:** Gracefully handles invalid city names and API errors.

## 📦 Requirements

-   Python 3.8+
-   Django 4+
-   Requests

## ⚙️ Installation Guide

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/your-username/weather-api.git](https://github.com/your-username/weather-api.git)
    cd weather-api
    ```

2.  **Create a Virtual Environment:**
    ```bash
    python -m venv venv
    ```
    Activate the environment:
    -   **Windows:** `venv\Scripts\activate`
    -   **macOS/Linux:** `source venv/bin/activate`

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: You'll need to create a `requirements.txt` file. See the section below.)*

4.  **Get Your API Key:**
    -   Go to [OpenWeatherMap](https://openweathermap.org/) and create a free account.
    -   Navigate to the "API keys" tab and get your API key.

5.  **Set Up Environment Variables:**
    -   In `wheatherapp/settings.py`, add the following line at the end of the file:
        ```python
        WEATHER_API_KEY = 'your_openweathermap_api_key'
        ```
    -   **Important:** For a production environment, it's recommended to use environment variables to keep your API key secure.

6.  **Apply Migrations:**
    ```bash
    python manage.py migrate
    ```

7.  **Run the Server:**
    ```bash
    python manage.py runserver
    ```
    The application will be running at `http://127.0.0.1:8000/`.

## `requirements.txt`

Create a file named `requirements.txt` in the root of your project and add the following lines:
