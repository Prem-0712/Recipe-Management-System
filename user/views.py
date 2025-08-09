from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def view_profile(request):
    return render(request, 'user/view_profile.html')