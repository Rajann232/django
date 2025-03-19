from project.urls import path
from .views import home
urlpatterns=[
    path('home/',home)
]