from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import indexView,confirmpaymentView,confirmpaymentViewTest
# from .views import index 
from django.conf.urls import url, include 
app_name = 'Payment'
urlpatterns = [
    url(r'^index$', indexView.as_view(), name="index"),
    path('access/token', views.getAccessToken, name='get_mpesa_access_token'),
    path('online/lipa', views.lipa_na_mpesa_online, name='lipa_na_mpesa'),
    path('transaction/complete/<str:id>/',views.lipa_na_mpesa_online),
    # path('index', views.index_page, name="homepage"),
    url(r'^confirm$', confirmpaymentView.as_view(), name="confirmpayment"),
    url(r'^confirmpayment/(?P<pk>[0-9]+)$',confirmpaymentView.as_view(),
         name="confirmpay"),
    url(r'^confirmpayment',confirmpaymentViewTest.as_view(),
         name="confirmpayTest"),
    
]
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)