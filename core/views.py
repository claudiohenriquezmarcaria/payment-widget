import requests
from django.shortcuts import render
from core.models import CreditCard, User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    creditCards = CreditCard.objects.all()
    user = request.user
    creditCardsAPI = get_creditcards(user)
    users = User.objects.all()
    context = {
        'CreditCards': creditCards,
        'CreditCardsAPI': creditCardsAPI,
        'LoggedInUser':user,
        'Env': 'https://api-marcariacore-qa.marcaria.host'
    }
    return render(request, 'index.html', context)

def get_creditcards(logged_in_user):
    mid = logged_in_user.mid
    response = requests.get('https://api-marcariacore-qa.marcaria.host/api/v1.0/users/14747/payments',verify=False)
    creditCardsAPI = response.json()

    #if request.htmx:
    #    return render(request, 'partials/creditcard_list.html',{'creidtcards':creditCardsAPI})
    
    return creditCardsAPI

