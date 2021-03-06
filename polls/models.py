from django.db import models
import datetime
from django.utils import timezone

class Question(models.Model):

	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('发布时间')

	def __str__(self):
		return self.question_text

	def day_before(self):
		return timezone.now() - datetime.timedelta(days=1) <= self.pub_date <= timezone.now()
		day_before.short_description = 'Published recently?'

class Choice(models.Model):

	question = models.ForeignKey(Question,on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text

		
