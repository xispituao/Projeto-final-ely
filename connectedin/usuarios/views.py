from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.views.generic.base import View
from perfis.models import Perfil
from usuarios.forms import RegistrarUsuarioForm


class RegistrarUsuarioView(View):
    template_name = 'registrar.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = RegistrarUsuarioForm(request.POST)
        if form.is_valid():
            dados_form = form.cleaned_data
            usuario = User.objects.create_user(username=dados_form['nome'],
                                               email=dados_form['email'],
                                               password=dados_form['senha'])
            perfil = Perfil(nome=dados_form['nome'], telefone=dados_form['telefone'],
                            nome_empresa=dados_form['nome_empresa'],
                            usuario_id=usuario)
            perfil.save()
            return redirect('index')

        return render(request, self.template_name, {'form': form})