from django.db import models
from django.contrib.auth.models import User
from login.models import models


class Question(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='Question_user')
	heading = models.CharField(max_length=100)
	q_description = models.CharField(max_length=200)
	reports = models.IntegerField(default=0)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return '(%s,%s,%s,%s,%s)' %(self.user,self.heading,self.q_description,self.reports,self.votes)


class Answer(models.Model):
	question = models.IntegerField(default=0)
	ans = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='Answer_user')