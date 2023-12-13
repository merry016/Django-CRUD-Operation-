from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from .models import Startup
from .forms import startup
from .forms import LoginForm, RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth import logout
from django.db.models import Q


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'

class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse_lazy('login'))

class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')

@login_required
def startapp(req):
    startapp=Startup.objects.all()
    context={'startapp':startapp}
    return render(req,'accounts/startapp.html',context)

@login_required
def createview(request): 
    # dictionary for initial data with  
    # field names as keys 
    # add the dictionary during initialization 
    if request.method=='POST':
        form =startup(request.POST or None) 
        if form.is_valid(): 
            form.save() 
            return redirect('startapp') 
    else:
        form=startup()
    return render(request, 'accounts/create.html',{'form':form}) 

@login_required
def update(request, pk):
    current_startup=get_object_or_404(Startup,pk=pk)
    if request.method=='POST':
        form = startup(request.POST, instance=current_startup)
        if form.is_valid():
            form.save()
            return redirect('startapp')
    else:
        form = startup(instance=current_startup)
        
    return render(request, 'accounts/update.html',{'form': form})

@login_required
def startup_details(request,pk):
    if pk:
        startup_detail= Startup.objects.get(pk=pk)
        return render(request,'accounts/record.html',{'startup_detail':startup_detail})
    else:
        return render(request, 'accounts/error.html', {'error_message': 'Invalid primary key'})
    
@login_required
def startup_delete(request, pk):
    delt = get_object_or_404(Startup, pk=pk)
    if request.method == 'POST':
        delt.delete()
        return redirect('startapp')
    return render(request, 'accounts/delete_startup.html', {'delt': delt})

@login_required

def startup_list(request):
    search_query = request.POST.get('query', '')
    form = startup(request.POST)

    if form.is_valid():
        search_query = form.cleaned_data.get('query', '')

        startups = Startup.objects.filter(
            Q(StartupName__icontains=search_query) | Q(firm__icontains=search_query) |
            Q(Description__icontains=search_query) | Q(Address__icontains=search_query) |
            Q(email__icontains=search_query) | Q(socialmedialink__icontains=search_query) |
            Q(Funding_Status__icontains=search_query))
            # Add more conditions as needed    )
    else:
        # If the form is not submitted or not valid, show all startups
        startups = Startup.objects.all()

    context = {'startups': startups, 'form': form}
    return render(request, 'accounts/startapp.html', context)



#def startup_detail(request, pk):
    #person = get_object_or_404(startup, pk=pk)
    #return render(request, 'person_detail.html', {'person': person})