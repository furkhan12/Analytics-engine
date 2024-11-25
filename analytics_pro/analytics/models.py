from django.db import models
from django.contrib.auth.models import User

# Create your models here.


#trackng uservisits
class UserVisit(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE) #referenc 2 user
    visit_time=models.DateTimeField(auto_now_add=True)#timestmp of visit


#tracking the usetime i.e usage of feature
class FeatureUsage(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE) #refrnc 2 user
    feature_name=models.CharField(max_length=100) #name of feature
    usage_time=models.DateTimeField(auto_now_add=True) #timestamp of usage
    