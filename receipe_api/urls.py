import imp
from django.urls import path
from .import views


urlpatterns = [
    path('',views.apiOverview,name='api-overview'),
    path('receipe-list/',views.receipeList, name='receipe-list'),
]
