from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .materia import Materia
from .form_materia import MateriaForm
from .topic import Topic
from .form_topic import TopicForm
from .form_topic import TopicFormRequiresSubject


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
    materias = Materia.objects.filter(usuario=request.user)

    if request.method == "POST":
        form = TopicFormRequiresSubject(request.POST)
        if form.is_valid():
            topic: Topic = form.save(commit=False)
            topic.data_estudo = timezone.localdate()

            current_count = Topic.objects.filter(
                materia=topic.materia
            ).count()

            topic.index = current_count - 1
            topic.save()
            messages.success(request, "Tópico adicionado!")
            return redirect("materia")
        messages.error(request, "Por favor, corrija os erros do tópico.")
    else:
        form = TopicFormRequiresSubject()

    date_str = request.GET.get("date")
    selected_date = None
    if date_str:
        try:
            selected_date = timezone.datetime.fromisoformat(date_str).date()
        except ValueError:
            selected_date = None

    if selected_date is None:
        selected_date = timezone.localdate()

    topics = (
        Topic.objects.filter(materia__usuario=request.user, data_estudo=selected_date)
        .select_related("materia")
        .order_by("materia__nome", "index", "id")
    )

    selected_date_string = selected_date.strftime('%d/%m/%Y')

    return render(request, 'materia.html', {
        'materias': materias,
        'selected_date': selected_date,
        'selected_date_string': selected_date_string,
        'topics': topics,
        "form": form,
    })


@login_required
def materia_criar(request):
    if request.method == 'POST':
        form = MateriaForm(request.POST)
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
    materia = get_object_or_404(Materia, pk=pk, usuario=request.user)
    if request.method == 'POST':
        form = MateriaForm(request.POST, instance=materia)
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
    materia = get_object_or_404(Materia, pk=pk, usuario=request.user)
    if request.method == 'POST':
        nome = materia.nome
        materia.delete()
        messages.success(request, f'A matéria "{nome}" foi removida de suas tarefas com sucesso.')
        return redirect('home')
    return render(request, 'materia_confirma_exclusao.html', {
        'materia': materia,
    })


@login_required
def materia_detalhe(request, pk):
    materia = get_object_or_404(Materia, pk=pk, usuario=request.user)
    topics = materia.topics.all().order_by("index", "id")

    if request.method == "POST":
        form = TopicForm(request.POST)
        if form.is_valid():
            topic: Topic = form.save(commit=False)
            topic.materia = materia
            topic.save()
            messages.success(request, "Tópico adicionado!")
            return redirect("materia_detalhe", pk=materia.pk)
        messages.error(request, "Por favor, corrija os erros do tópico.")
    else:
        form = TopicForm()

    return render(
        request,
        "materia_detalhe.html",
        {
            "materia": materia,
            "topics": topics,
            "form": form,
        },
    )


@login_required
def topic_toggle_completed(request, pk):
    topic = get_object_or_404(Topic, pk=pk, materia__usuario=request.user)
    if request.method == "POST":
        topic.is_completed = not topic.is_completed
        topic.save(update_fields=["is_completed"])

    # Redirecionar para a página de origem (agenda ou detalhe da matéria)
    next_url = request.POST.get("next")
    if next_url:
        return redirect(next_url)
    return redirect("materia_detalhe", pk=topic.materia_id)


@login_required
def topic_deletar(request, pk):
    topic = get_object_or_404(Topic, pk=pk, materia__usuario=request.user)
    materia_id = topic.materia_id
    if request.method == "POST":
        topic.delete()
        messages.success(request, "Tópico removido.")
    return redirect("materia_detalhe", pk=materia_id)


@login_required
def agenda(request):
    date_str = request.GET.get("date")
    selected_date = None
    if date_str:
        try:
            selected_date = timezone.datetime.fromisoformat(date_str).date()
        except ValueError:
            selected_date = None

    if selected_date is None:
        selected_date = timezone.localdate()

    topics = (
        Topic.objects.filter(materia__usuario=request.user, data_estudo=selected_date)
        .select_related("materia")
        .order_by("materia__nome", "index", "id")
    )

    return render(
        request,
        "agenda.html",
        {
            "selected_date": selected_date,
            "topics": topics,
        },
    )
