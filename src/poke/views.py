import requests as req
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(requests):
    context = {'name' : 'TITI', 'listPoke': ['Pikachu', 'Dracafau', 'Salamèche']}
    return render(requests, 'pokeapp/home.html', context)

def team(requests):
    return render(requests, 'pokeapp/team.html')

def about(requests):
    return render(requests, 'pokeapp/about.html')

def search(requests, searchText):
    number = 0
    rserch= req.get("https://pokeapi.co/api/v2/pokemon/"+searchText)
    
    status=rserch.status_code
    if(status!=200):
        context = {'name': status}
        return render(requests,'pokeapp/searcherror.html')
    else:
        result = rserch.json()
        number=result['id']            
        r = req.get("https://pokeapi.co/api/v2/pokemon/"+str(number))
        result = r.json()
        
        type = result['types'][0]['type']['name']
        weight = result['weight']
        image = result['sprites']['other']['home']['front_default']
        name = result['name']

        rinfo = req.get("https://pokeapi.co/api/v2/pokemon-species/"+str(number))
        result = rinfo.json()
            
        color = result['color']['name']
        habitat = result['habitat']['name']

        context = {'name': name, 'color' : color, 'habitat' : habitat , 'weight' : weight , 'type' : type , 'image' : image }  
        return render(requests,'pokeapp/search.html',context)


def pokemon(requests, number):
    r = req.get("https://pokeapi.co/api/v2/pokemon/"+str(number))
    result = r.json()
    
    type = result['types'][0]['type']['name']
    weight = result['weight']
    image = result['sprites']['other']['home']['front_default']
    name = result['name']   

    rinfo = req.get("https://pokeapi.co/api/v2/pokemon-species/"+str(number))
    result = rinfo.json()
    color = result['color']['name']
    habitat = result['habitat']['name']

    context = {'name': name, 'color' : color, 'habitat' : habitat , 'weight' : weight , 'type' : type , 'image' : image }        
    return render(requests,'pokeapp/pokemon.html',context)
