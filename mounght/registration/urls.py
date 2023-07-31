from django.urls import path
from .views import registration, registration_success, logout_view

app_name = 'registration'

urlpatterns = [
    path('registration/', registration, name='registration'),
    path('registration_success/', registration_success, name='registration_success'),
    path('logout/', logout_view, name='logout'),
]
