from . import views
from django.urls import path # type: ignore
from django.conf import settings # type: ignore
from django.conf.urls.static import static # type: ignore


app_name = 'dash'

urlpatterns =[
    path('' , views.home , name='home'),
    path('login/' , views.login_view , name='login'),
    path('logout/' , views.logout_view , name='logout'),
    path('signup/' , views.signup_view , name='signup'),
    path('chef/' , views.chef , name='chef'),
    path('cart/' , views.cart , name='cart'),
    path('order/' , views.order , name='order'),
    path('profile/' , views.profile , name='profile'),
    path('menu2/<int:offering_id>/' , views.menu2 , name='menu2'),
    path('dish/<int:singleDish_id>/' , views.singleDish , name='singleDish'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
