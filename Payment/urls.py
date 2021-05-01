from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

# app_name = 'Transaction'
urlpatterns = [
    path('access/token', views.getAccessToken, name='get_mpesa_access_token'),
    path('online/lipa', views.lipa_na_mpesa_online, name='lipa_na_mpesa'),
    path('transaction/complete/<str:idcov>/',views.lipa_na_mpesa_online),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)