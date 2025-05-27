from django.shortcuts import render, HttpResponse
import json
import requests
# Create your views here.

def wheather(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=6657d9a4c8c148e5133e6903a993b7a8"
        list_of_data = requests.get(source).json()
        
        data = {
            "city": city,
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ', ' + str(list_of_data['coord']['lat']),
            "temp": round((list_of_data['main']['temp'] - 32) * 5.0/9.0, 2),
            "humidity": str(list_of_data['main']['humidity'])  # Fixed the typo here
        }
    else:
        data = {}
    return render(request, 'weather.html', data)