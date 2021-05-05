from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import indexView,paymentView
# from .views import index 
from django.conf.urls import url, include 
# app_name = 'Transaction'
urlpatterns = [
    url(r'^index$', indexView.as_view(), name="index"),
    path('access/token', views.getAccessToken, name='get_mpesa_access_token'),
    url(r'^access/token$', paymentView.as_view(), name="homepage"),
    # path('online/lipa', views.lipa_na_mpesa_online, name='lipa_na_mpesa'),
    path('transaction/complete/<str:id>/',views.lipa_na_mpesa_online),
    # path('index', views.index_page, name="homepage"),
    
    
]
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)