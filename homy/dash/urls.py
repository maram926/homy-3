from . import views
from django.urls import path # type: ignore
from django.conf import settings
from django.conf.urls.static import static


app_name = 'dash'

urlpatterns =[
    path('' , views.home , name='home'),
    path('login/' , views.login_view , name='login'),
    path('logout/' , views.logout_view , name='logout'),
    path('signup/' , views.signup_view , name='signup'),
    path('chef/' , views.chef , name='chef'),
<<<<<<< HEAD
    path('cart/' , views.cart , name='cart'),
    path('menu2/<int:offering_id>/' , views.menu2 , name='menu2'),
    path('dish/<int:singleDish_id>/' , views.singleDish , name='singleDish'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
    path('menu/<int:offering_id>/' , views.menu , name='menu')
]
>>>>>>> 41de42c65ccb23278e9cdf1a79e0f0af041dae83
