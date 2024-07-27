from django.urls import path
from django.shortcuts import redirect
from .views import SignUp

urlpatterns = [

    path('signup/', SignUp.as_view(), name='signup'),
    path('', lambda request: redirect('signup', permanent=False)),

]


