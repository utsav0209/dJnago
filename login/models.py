from django.db import models
from django.contrib.auth.models import User
from django.core.validators import *
import uuid
# Create your models here.


class Client(models.Model):
	USERID = models.UUIDField(primary_key = True , default=uuid.uuid4)
	User = models.OneToOneField(User, on_delete=models.CASCADE)
	username = models.CharField(max_length=20)
	phone_number = models.CharField(validators=[MinLengthValidator(10), MaxLengthValidator(13)], max_length=13) #add a phone number regex for validation
	state = models.CharField( max_length=20 )
	#username = models.CharField(max_length=20)
	name = models.CharField(max_length=50)
	city = models.CharField(max_length=20)
	address = models.TextField(max_length=100)
	email = models.TextField(default='abc@xyz.com', max_length=100)