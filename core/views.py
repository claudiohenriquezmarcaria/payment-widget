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
        'LoggedInUser':user
    }
    return render(request, 'index.html', context)

def get_creditcards(logged_in_user):
    mid = logged_in_user.mid
    response = requests.get('https://api-marcariacore-qa.marcaria.host/api/v1.0/users/14747/payments',verify=False)
    creditCardsAPI = response.json()

    #if request.htmx:
    #    return render(request, 'partials/creditcard_list.html',{'creidtcards':creditCardsAPI})
    
    return creditCardsAPI

def step1(request):
    user = request.user  # You can use user info here
    data_to_send = {
        "user_email": user.email,
        "value": request.POST.get("data"),
    }

    try:
        api_response = requests.post(
            "https://external-api.com/endpoint/",
            json=data_to_send,
            headers={"Authorization": "Bearer YOUR_API_TOKEN"}
        )
        api_response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return api_response.json()

    return api_response.json()