
from django.shortcuts import render, redirect
import json 
import urllib.request 
from .models import Weather

def index(request): 
    if request.method == 'POST': 
        city = request.POST['city'] 
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=e8ddef56273a5f305a361716e9246e42').read() 
        list_of_data = json.loads(source) 

        data = {
            "name": str(list_of_data["name"]),
            "country_code": str(list_of_data['sys']['country']), 
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']), 
            "temp": str(list_of_data['main']['temp']) + 'k', 
            "pressure": str(list_of_data['main']['pressure']), 
            "humidity": str(list_of_data['main']['humidity']), 
        }
        # Save weather data to database
        wdata=Weather()
        wdata.city=str(list_of_data["name"])
        wdata.country_code=str(list_of_data['sys']['country'])
        wdata.coordinate=str(list_of_data['coord']['lon']) + ' '+ str(list_of_data['coord']['lat'])
        wdata.temp=str(list_of_data['main']['temp']) + 'k'
        wdata.pressure=str(list_of_data['main']['pressure'])
        wdata.humidity=str(list_of_data['main']['humidity'])
        wdata.save()
        bdata=Weather.objects.all().order_by('-timestamp')
        data['bdata']=bdata
        print(data)

        # Redirect to prevent resubmission on refresh
        return redirect('index')
    else: 
        data = {
            'bdata': Weather.objects.all().order_by('-timestamp')
        }
        
    return render(request, "index.html", data) 

def delete_location(request, location_id):
    location = Weather.objects.get(pk=location_id)
    location.delete()
    return redirect('index')
