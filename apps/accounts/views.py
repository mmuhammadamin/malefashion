from .models import Profile
from django.shortcuts import render


# Create your views here.
from ..cart.models import Cart


def profile_view(request):
    profile = Profile.objects.all()
    user = request.user

    cart = Cart.objects.filter(client=user, is_ordered=False).first()


    ctx={
        'profile':profile,
        'cart':cart
    }

    return render(request,'profile.html',ctx)

