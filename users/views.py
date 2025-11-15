from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.models import User

#def register(response):
#if response.method == "POST":
            #form = RegisterForm(response.POST)
            #if form.is_valid():
                    #form.save()

            #return redirect("/home")
    #else:
        #form = RegisterForm()

    #return render(response, '../plantillas/registration/register.html', {'form':form})

def loginPage(request):
        if request.method=='POST':
                username=request.POST.get('username')
                password = request.POST.get('password')

                try:
                        user = User.objects.get(username=username)
                except:
                        messages.error(request, 'Este usuario no existe')

        context={}
        return render(request, '../plantillas/login_register.html', context)
