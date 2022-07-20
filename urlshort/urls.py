from django.urls import path
# Import Views
from . import views

# All Urls
urlpatterns = [
    path('', views.index, name='index'),
    path('app/signup/', views.signup, name='signup'),
    path('app/signout/', views.signout, name='signout'),
    path('app/signin/', views.signin, name = 'signin'),
    path('app/', views.app, name = 'app'),
    path('app/links/', views.links, name = 'links'),
    path('app/create/', views.create, name='create'),
    # Shortend Url
    path('<str:pk>', views.short, name='short'),
]
