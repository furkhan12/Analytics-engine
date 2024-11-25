from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import UserVisit,FeatureUsage
from .models import *
# Create your views here.

@login_required
def track_visit(request):
    UserVisit.objects.create(user=request.user) # Creatng a new UserVisit record
    return redirect('dashboard') # redirect to dashboard

# hlpr function to track feature usage
@login_required
def use_feature(request, feature_name):
    FeatureUsage.objects.create(user=request.user, feature_name=feature_name) # Creatng a new FeatureUsage record
    return redirect('dashboard')



# 5 features
#decorater for the security feature i.e only authenticated users can access
@login_required
def profile_view(request):
    return use_feature(request, 'Profile View') #Tracking the 'Profile View' 

@login_required
def upload_photo(request):
    return use_feature(request, 'Upload Photo')

@login_required
def send_message(request):
    return use_feature(request, 'Send Message')

@login_required
def like_post(request):
    return use_feature(request, 'Like Post')

@login_required
def comment_on_post(request):
    return use_feature(request, 'Comment on Post')






@login_required
def dashboard(request):
    user_visits=UserVisit.objects.filter(user=request.user).count() #for counting the user visits
    feature_usages=FeatureUsage.objects.filter(user=request.user).values('feature_name').annotate(count=models.Count('feature_name'))  # Aggregating the feature usage data
    context={
        'user_visits': user_visits,
        'feature_usages':feature_usages,
    }
    return render(request,'analytics/dashboard.html',context)  # Rendering the dashboard template

