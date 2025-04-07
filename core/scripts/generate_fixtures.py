from core.models import CreditCard, User
from django.utils import timezone

# Register your models here.
def run():

    User.objects.get_or_create(first_name='Claudio', last_name='Henriquez')

    users = User.objects.all()

    CreditCards = [
        {"number":"4111111111111111","holder":"Testing testor 1", "expiration":"07/28","cvc":"123"},
        {"number":"1234567890123456","holder":"Testing testor 1", "expiration":"07/28","cvc":"123"}
    ]

    for cc in CreditCards:
        CreditCard.objects.get_or_create(number=cc["number"],holder=cc["holder"],expiration=cc["expiration"],cvc=["cvc"], owner=users[0])


    listCreditCards = CreditCard.objects.all()
