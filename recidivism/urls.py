
from django.contrib import admin
from django.urls import path
import recidivism.views as views
urlpatterns = [
    path('',views.home,name='recidivism')
]
