from django.shortcuts import render, redirect
from django.shortcuts import render
from django.http import HttpResponse
import requests
from requests.auth import HTTPBasicAuth
import json
from .models import Product, Transactions
import uuid
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.models import User


# import our MpesaAccessToken and LipanaMpesaPpassword classes from mpesa_credentials.py file
from . credentials import MpesaAccessToken, LipanaMpesaPpassword

# Create your views here.
 
def getAccessToken(request):
    consumer_key = 'Jj8TrQstN3kxRrQx06Etge3UUK73bAmh'
    consumer_secret = 'psa3rMtGLbMPI9Jc'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    
    return validated_mpesa_access_token(access_token) 
 
#define our STK push method called lipa_na_mpesa_online.
def lipa_na_mpesa_online(request, id):
    idcov = uuid.UUID(id)
    # path('transaction/complete/<string:uuid>',views.lipa_na_mpesa_online)
    trx = Transactions.objects.get(uuid=idcov)
    # get our mpesa access token
    access_token = MpesaAccessToken.validated_mpesa_access_token
    # define our STK push URL provided by Safaricom.
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    # define our headers where we pass our access token
    headers = {"Authorization": "Bearer %s" % access_token}

    request = {
        # pass our mpesa Shortcode.
        "BusinessShortCode": "174379",
        # pass our mpesa password.
        "Password": LipanaMpesaPpassword.decode_password,
        # define the transaction timestamp.
        "Timestamp": LipanaMpesaPpassword.lipa_time,
        # define the transaction type. Since it’s STK push we use CustomerPayBillOnline
        "TransactionType": "CustomerPayBillOnline",
        # define the amount, in this case, one shilling.
        "Amount": trx.amount,
        # define the phone number sending the money.
        "PartyA": trx.contact,  # replace with your phone number to get stk push
        # define the organization shortcode receiving the funds.
        "PartyB": "174379",
    #    define the mobile number to receive STK pin prompt.
       "PhoneNumber": trx.contact,  # replace with your phone number to get stk push
        
        #  define a valid URL which will receive notification from Mpesa-TOKEN.
        #  Note this should be your confirmation URL.
        "CallBackURL": "https://posthere.io/1bfa-4202-9fb6",
        # define an identifier of the transaction.
        "AccountReference": "apple",
        # define the description of what the transaction is all about.
        "TransactionDesc": "Testing stk push"
    }

    print(request)


    print(headers)

     # get the response from Safaricom mpesa TOKEN.
    response = requests.post(api_url, json=request, headers=headers)
    # print(response)
    # define a response, of course, you can choose 
    # to redirect the user to a different page. 
    # In my case, I respond with HTTP response success.
    return HttpResponse('success')

def index_page(request):
     
    
    return HttpResponse("This is a simple response !") 

class indexView(TemplateView):
    template_name = 'home/index.html'
    def get(self,request ):
        trx = Transactions.objects.all()
        return render(request, self.template_name)

    def post(self, request, pk):
        trx = Transactions.objects.get(id=pk)
        form = contactForm(request.POST)
        trx.item = form.data['item']
        trx.save()
        return redirect('/index/')
