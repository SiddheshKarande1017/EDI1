from django.urls import path
from . import views

urlpatterns=[
path('', views.register, name='register'),
path('login/', views.loginuser, name="login"),
path('home/', views.home, name='home'),
path('problems/', views.problems, name='problems'),
path('logout/', views.logoutuser, name="logout"),
path('topics/', views.topics, name='topics'),
path('discuss/', views.discuss, name='discuss'),
path('pfilter/',views.pfilter,name='pfilter'),
path('tfilter/',views.tfilter,name='tfilter')
]
# path('', views.register, name='register'),
# path('login/', views.loginuser, name="login"),
# path('home/', views.home, name='home'),
# path('problems/', views.problems, name='problems'),
# path('logout/', views.logoutuser, name="logout"),
# path('topics/', views.topics, name='topics'),
# path('discuss/', views.discuss, name='discuss'),

# path('', views.home, name='home'),
#     path('login/', views.loginuser, name="login"),
#     path('register/', views.register, name='register'),
#     path('problems/', views.problems, name='problems'),
#     path('logout/', views.logoutuser, name="logout"),
#     path('topics/', views.topics, name='topics'),
#     path('discuss/', views.discuss, name='discuss'),