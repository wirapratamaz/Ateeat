from django.shortcuts import render
from .models import BuyerUser

# Create your views here.
def buyer_user(request):
    buyer_users = BuyerUser.objects.all()
    return render(request, 'buyer_user.html',
                  {
                      'buyer_users': buyer_user
                  })