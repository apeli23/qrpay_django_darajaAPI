from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
import uuid
# Create your models here.

# create model 'Product' to store the app's product items
class Product(models.Model):     
    item = models.CharField(max_length=200)     
    
    def __str__(self):
        return self.item
# Create model 'Transactions'to store the dbase's contact and amount field. 
class Transactions(models.Model): 
    item = models.ForeignKey(Product, blank=True, null=True, on_delete=models.CASCADE)
    contact = models.IntegerField(default=0)
    amount = 1
    # create field 'code' which will contain the qr_code
    code = models.ImageField(upload_to='qr_codes', blank=True)
    # 'uuid' field to contain uuid
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    
    # now we overwrite the save method with the following function.
    def save(self, *args, **kwargs):
        # declare a dynamic url to stk
        link =  'http://192.168.100.29:8000/api/v1/transaction/complete/'+self.uuid.hex+'/'
        # create a qr code based on this link
        qrcode_img = qrcode.make(link)
        # construct a new image based on parameters size and color
        canvas = Image.new('RGB', (440,440), 'white')
        # paste the qr code to the canvas image
        canvas.paste(qrcode_img)
        # set up the qr code file name
        fname = f'qr_code-{self.item}.png'
        # create an in memory file name 
        buffer = BytesIO()
        # pass in the buffer to the canvas
        canvas.save(buffer,'PNG')
        # create a file object and pass it to the 'code' imagefield
        self.code.save(fname, File(buffer), save=False)
        # close the canvas
        canvas.close()
        # save
        super().save(*args, **kwargs)

    
    