from django.shortcuts import render
from .models import Destination

# Create your views here.


def index(request):

    dest1 = Destination()
    dest1.name = 'Trivandrum'
    dest1.desc = 'The City of Legends'
    dest1.img = 'destination_1.jpg'
    dest1.price = "780"

    dest2 = Destination()
    dest2.name = 'Kollam'
    dest2.desc = 'The City of Legends Only'
    dest2.img = 'destination_2.jpg'
    dest2.price = "740"

    dest3 = Destination()
    dest3.name = 'Kochi'
    dest3.desc = 'The City of Legendss'
    dest3.img = 'destination_3.jpg'
    dest3.price = "720"

    dests = [dest1, dest2, dest3]
    return render(request, 'index.html', {'dests': dests})
