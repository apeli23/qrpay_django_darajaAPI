from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import indexView,paymentView
# from .views import index 
from django.conf.urls import url, include 
app_name = 'Payment'
urlpatterns = [
    # homepage directory
    url(r'^index$', indexView.as_view(), name="index"),   
    # redirect uniq model objects to payments view
    path('payment/<str:pk>', paymentView.as_view(), name="payment"),  
    # access toke url
    path('access/token', views.getAccessToken, name='get_mpesa_access_token'),
    # initiate stk push url
    path('online/lipa', views.lipa_na_mpesa_online, name='lipa_na_mpesa'),
    # define uccessfull payment url
    path('transaction/complete/<str:id>/',views.lipa_na_mpesa_online),
     
]
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
 