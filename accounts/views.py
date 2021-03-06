from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import SignUpForm,UserUpdateForm

from django.contrib.auth.decorators import login_required
from accounts.models import User
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

def signup(request):
    if request.user.is_authenticated:
        return redirect('notices:home')
    if request.method == 'POST':
        print(request.POST)
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('notices:home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})



@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    form_class = UserUpdateForm
    template_name = 'accounts/my_account.html'
    success_url = reverse_lazy('accounts:my_account')

    def get_object(self):
        return self.request.user