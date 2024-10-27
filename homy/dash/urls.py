from . import views
from django.urls import path # type: ignore


app_name = 'dash'

urlpatterns =[
    path('' , views.home , name='home'),
    path('login/' , views.login_view , name='login'),
    path('logout/' , views.logout_view , name='logout'),
    path('signup/' , views.signup_view , name='signup'),
]