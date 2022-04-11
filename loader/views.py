from django.shortcuts import render
import requests
from urllib.request import urlretrieve



def show(request):
    URL_APOD = "https://api.nasa.gov/planetary/apod"
    date = '2020-02-22'
    params = {
        'date': date,
        'api_key':apiKey,
        'hd':'True'
    }
    response = requests.get(URL_APOD,params=params).json()
    print(response)
    data= {'url': response.get('hdurl'), 'explanation': response.get('explanation'), 'tittle': response.get('title')}
    context= {
        'data': data
    }
    return render(request, "home.html", context)


