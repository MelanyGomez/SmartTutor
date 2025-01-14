from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse

from .forms import LoginForm, UserRegistrationForm

# autenticacionUsuarios/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'account/home.html')


# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], 
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Usuario autenticado')
                else:
                    return HttpResponse('El usuario no esta activo')
            else:
                return HttpResponse('La información no es correcta')
    else:
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})    
    
@login_required
def dashboard(request):
    return render(request, 
                  'account/dashboard.html')

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # aun no guardamos el usuario
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                #encriptamos la contra
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
        return render(request,
                      'account/register.html',
                      {'user_form': user_form}) 