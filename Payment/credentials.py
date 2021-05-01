import requests
import json
from requests.auth import HTTPBasicAuth
from datetime import datetime
import base64

# create a class called MpesaC2BCredential
class MpesaC2bCredential:
        #  consumer_key variable
    consumer_key = 'Jj8TrQstN3kxRrQx06Etge3UUK73bAmh'
    #  consumer_secret variable
    consumer_secret = 'psa3rMtGLbMPI9Jc'
    #  URL variable for generating the mpesa token
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

# This is the class we are going to use to make a call to mpesa.
class MpesaAccessToken:
    r = requests.get(MpesaC2bCredential.api_URL,
                     auth=HTTPBasicAuth(MpesaC2bCredential.consumer_key, MpesaC2bCredential.consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']
  
# Check Mpesa Daraja documentation to farmiliarize with how the password is generated.
class LipanaMpesaPpassword:
    #  define the format of our transaction timestamp.
    lipa_time = datetime.now().strftime('%Y%m%d%H%M%S')
    # we define our business Shortcode (Paybill no). 
    # In this case, we are use test credentials provided by Safaricom Daraja sandbox.
    Business_short_code = "174379"
    # define the passkey, this information is given in Mpesa sandbox test credentials.
    passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
    # define our password used to encrypt the request we send mpesa API STK push URL. 
    # The password is a base64 string which is a combination of Shortcode+Passkey+Timestamp.
    data_to_encode = Business_short_code + passkey + lipa_time
    # encode our password to base64 string.
    online_password = base64.b64encode(data_to_encode.encode())
    # decode our password to UTF-8
    decode_password = online_password.decode('utf-8')

