from django.urls import path
from realestate import views


urlpatterns = [
    path('newlisting/', views.generate_listing_description),
  
]

