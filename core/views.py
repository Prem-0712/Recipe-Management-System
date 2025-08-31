from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from user.models import Profile

@login_required
def home(request):
    return render(request, 'core/home.html')

def login(request):

    if (request.method == 'POST'): 
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if (user is not None):
            auth.login(request, user)
            messages.success(request, "Login succefully done...")
            return redirect('home')
        
        else:
             messages.error(request, "passwords don't match", extra_tags='confirm_password')
             return redirect('register')

    return render(request, 'core/login.html')

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if (password == confirm_password):
            
            if User.objects.filter(email=email).exists():
                messages.error(request, 'The email is already taken', extra_tags="email")
                return redirect("register")
            
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'The username is already taken', extra_tags="username")
                return redirect('register')
            
            else:
                new_user = User.objects.create_user(first_name = first_name, last_name = last_name, username = username, email = email, password = password)
                new_user.save()

                user_creadentials = auth.authenticate(username = username, password = password)
                auth.login(request, user_creadentials)
                get_new_user = User.objects.get(username = username)
                new_profile = Profile.objects.create(user = get_new_user)
                new_profile.save()
                messages.success(request, 'Account created successfully !!')
                return redirect('home')



        else:
            messages.error(request, "The password's doesn't match", extra_tags="confirm_password")
            return redirect('register')

    return render(request, 'core/register.html')

def logout(request):
    auth.logout(request)
    messages.success(request, 'logout successful')
    return redirect('login')