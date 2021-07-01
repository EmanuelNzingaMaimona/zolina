from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import transaction
from .forms import CreateUserForm, DonorForm
from .models import Donor
from .filters import DonorFilter

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView

from .models import fill_p

# Create your views here.
def home(request):
    return render(request, 'index.html')

class FindListView(ListView):
    model = Donor
    paginate_by = 3
    context_object_name = 'data'

    def get_queryset(self, *args, **kwargs):
        context = {}
        group = self.request.GET.get('group')
        province = self.request.GET.get('province')
        municipe = self.request.GET.get('municipe')

        if group:
            context['group'] = group
        if province:
            context['province'] = province
        if municipe:
            context['municipe'] = municipe

        return Donor.objects.filter(**context)

def getStuff(self, str):
    return self.request.GET.get(str)

def regist(request):
    if request.user.is_authenticated:
        logout_user(request)
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            insta = User.objects.get(username=request.POST.get('username'))
            obj = Donor(
                user = insta,
                name = request.POST.get('name'), 
                phone = request.POST.get('phone'), 
                group = request.POST.get('group'), 
                province = request.POST.get('province'),
                municipe = request.POST.get('municipe'), 
                district = request.POST.get('district')
            )
            obj.save()
            user = form.cleaned_data.get('username') 
            messages.success(request, 'benvenue ' + user)
            return redirect('url_login')
    
    content = {'form': form}
    return render(request, 'regist.html', content)


def find(request):
    data = Donor.objects.all()[:5]

    myfilter = DonorFilter(request.GET, queryset=Donor.objects.all())
    
    content = {'data': data, 'filter': myfilter}
    return render(request, 'find.html', content)

def about(request):
    return render(request, 'about.html')

def v404(request):
    return render(request, '404.html')

def login_user(request):
    if request.user.is_authenticated:
        return redirect('url_home') 
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password') 
            user = authenticate(request, 
                username = username,
                password = password,
                )
            if user is not None:
                login(request, user)
                messages.info(request, 'success')
                return redirect('url_home') 
            else:
                messages.info(request, 'error')
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('url_login')


def perfil(request, pk):
    if not request.user.is_authenticated:
        return redirect('url_login')
    
    insta = Donor.objects.get(user=User.objects.get(username=pk))
    user = request.user
    userform = CreateUserForm(instance=user)
    donorform = DonorForm(instance=insta)
    if request.method == "POST":
        userform = CreateUserForm(request.POST or None, instance=user)
        donorform = DonorForm(request.POST or None, request.FILES or None, instance=insta)
        if donorform.is_valid:
            donorform.save()
            pk=request.POST.get('username')
            messages.success(request, 'Sucessfully updated')
        else:
            messages.error(request, 'sth went wrong')
    
    content = {
        'i': user,
        'user': userform, 
        'form': donorform,
        'email': User.objects.get(username=pk).email,
        'municipe': insta.municipe,
        }

    return render(request, 'perfil.html', content)




def nova_senha(request, pk):
    if not request.user.is_authenticated:
        return redirect('url_login')
    
    insta = Donor.objects.get(user=User.objects.get(username=pk))
    user = request.user
    userform = CreateUserForm(instance=user)
    donorform = DonorForm(instance=insta)
    if request.method == "POST":
        userform = CreateUserForm(request.POST or None, instance=user)
        donorform = DonorForm(request.POST or None, request.FILES or None, instance=insta)
        if userform.is_valid and donorform.is_valid:
            userform.save()
            donorform.save()
            pk=request.POST.get('username')
            messages.success(request, 'Sucessfully updated')
        else:
            messages.error(request, 'sth went wrong')
    
    content = {
        'i': user,
        'user': userform, 
        'form': donorform,
        'email': User.objects.get(username=pk).email,
        'municipe': insta.municipe,
        }

    return render(request, 'perfil.html', content)



'''
@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = CreateUserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Your profile was successfully updated!')
            return redirect('url_teste')
        else:
            messages.error(request,'Please correct the error below.')
    else:
        user_form = CreateUserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'teste.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
    

@transaction.atomic
def registar(request):
    data = {
        'm' : 'Bengo',
        'fill_p': fill_p(),
    }
    user_form = UserForm()
    profile_form = ProfileForm()
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            user = user_form.cleaned_data.get('username') 
            messages.success(request, 'benvenue ' + user)
            return redirect('url_login')
        else:
            messages.error(request,'Please correct the error below.')
    
    content = {'user_form': user_form, 'profile_form': profile_form, 'data': data}
    return render(request, 'teste.html', content)


@login_required
@transaction.atomic
def update_profile2(request):
    if request.method == 'POST':
        user_form = CreateUserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Your profile was successfully updated!')
            return redirect('url_teste')
        else:
            messages.error(request,'Please correct the error below.')
    else:
        user_form = CreateUserForm()
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'teste.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
    '''