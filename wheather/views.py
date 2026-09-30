from django.shortcuts import render
import os
import requests

API_KEY = os.environ.get("OPENWEATHER_API_KEY", "")


def wheather(request):
    data = {}
    if request.method == 'POST':
        city = request.POST.get('city', '').strip()
        data["query"] = city
        try:
            res = requests.get(
                "https://api.openweathermap.org/data/2.5/weather",
                params={"q": city, "units": "metric", "appid": API_KEY},
                timeout=8,
            )
            d = res.json()
            if res.status_code != 200:
                data["error"] = str(d.get("message", "City not found")).capitalize()
            else:
                w = d["weather"][0]
                data.update({
                    "city": d.get("name", city),
                    "country_code": d["sys"].get("country", ""),
                    "coordinate": f"{d['coord']['lat']:.2f}, {d['coord']['lon']:.2f}",
                    "temp": round(d["main"]["temp"]),
                    "feels_like": round(d["main"]["feels_like"]),
                    "temp_min": round(d["main"]["temp_min"]),
                    "temp_max": round(d["main"]["temp_max"]),
                    "humidity": d["main"]["humidity"],
                    "pressure": d["main"]["pressure"],
                    "wind": round(d["wind"]["speed"] * 3.6),
                    "description": w["description"],
                    "main": w["main"].lower(),
                    "icon": w["icon"],
                })
        except requests.RequestException:
            data["error"] = "Network error. Please try again."
    return render(request, 'weather.html', data)
