from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home),
    path("show_item/<id>",views.show_item),
    path("view_item/<id>",views.view_item),
    path('login',views.login),
    path('Signup',views.signup),
    path('logout',views.logout),
    path('addToCart',views.addToCart),
    path('showCartItems',views.showCartItems),
    path('home_page',views.home_page),
    path('make_payment',views.make_payment),
]
