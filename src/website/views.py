from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .materia import Materia
from .form_materia import MateriaForm



def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Conta criada para {username}! Agora você pode fazer login.')
            return redirect('login')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next', 'home')
                return redirect(next_url)
            else:
                messages.error(request, 'Usuário ou senha inválido..')
        else:
            messages.error(request, 'Por favor, preencha todos os campos.')
    
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    messages.info(request, 'Você saiu do sistema.')
    return redirect('login')


@login_required
def home(request):
    return redirect('materia')

@login_required
def materia(request):
    """Veja aqui as matérias que você já criou"""
    materias = Materia.objects.filter(usuario=request.user)
    return render(request, 'materia.html', {'materias': materias})

@login_required
def materia_criar(request):
    """Crie uma nova matéria"""
    if request.method == 'POST':
        form = MateriaForm(request.POST, request.FILES)
        if form.is_valid():
            materia = form.save(commit=False)
            materia.usuario = request.user
            materia.save()
            messages.success(request, f'A matéria "{materia.nome}" foi criada com sucesso!')
            return redirect('materia')
    else:
        form = MateriaForm()
    return render(request, 'materia_form.html', {
        'form': form,
        'titulo': 'Nova Matéria',
        'btn_label': 'Criar Matéria',
    })

@login_required
def materia_editar(request, pk):
    """Escolha a matéria que pretende editar"""
    materia = get_object_or_404(Materia, pk=pk, usuario=request.user)
    if request.method == 'POST':
        form = MateriaForm(request.POST, request.FILES, instance=materia)
        if form.is_valid():
            form.save()
            messages.success(request, f'A matéria "{materia.nome}" foi atualizada!')
            return redirect('materia')
    else:
        form = MateriaForm(instance=materia)
    return render(request, 'materia_form.html', {
        'form': form,
        'titulo': f'Editar: {materia.nome}',
        'btn_label': 'Salvar Alterações',
        'materia': materia,
    })

@login_required
def materia_deletar(request, pk):
    """Escolha a matéria que deseja remover"""
    materia = get_object_or_404(Materia, pk=pk, usuario=request.user)
    if request.method == 'POST':
        nome = materia.nome
        materia.delete()
        messages.success(request, f'A matéria "{nome}" foi removida de suas tarefas com sucesso.')
        return redirect('home')
    return render(request, 'materia_confirma_exclusao.html', {
        'materia': materia,
    })