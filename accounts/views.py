from django.shortcuts import render
from django.views.generic import  (
    CreateView, TemplateView, UpdateView, FormView
)
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin #função quando sua view é baseada em classe
from django.contrib.auth.forms import PasswordChangeForm

from .models import User
from .forms import UserAdminCreationForm

class IndexView(LoginRequiredMixin, TemplateView ): #verifica se o usuario esta logado para mostrar o template,a ordem dos metodos importa

    template_name = 'accounts/index.html'


class RegisterView(CreateView):

    model = User
    template_name = 'accounts/register.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('index')

class UpdateUserView(LoginRequiredMixin, UpdateView): # O LoginRequiredMixin é para ver se o úsuario nao é nulo

    model = User
    template_name = 'accounts/update_user.html' #templates a serem criados na pasta accounts
    fields = ['name', 'email']
    success_url = reverse_lazy('accounts:index')

    def get_object(self):
        return self.request.user


class UpdatePasswordView(LoginRequiredMixin, FormView):

    template_name = 'accounts/update_password.html'
    success_url = reverse_lazy('accounts:index')
    form_class = PasswordChangeForm

    def get_form_kwargs(self):
        kwargs = super(UpdatePasswordView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


    def form_valid(self, form):
        form.save()
        return super(UpdatePasswordView, self).form_valid(form)



index = IndexView.as_view()
register = RegisterView.as_view()
update_user = UpdateUserView.as_view()
update_password = UpdatePasswordView.as_view()

# Create your views here.
