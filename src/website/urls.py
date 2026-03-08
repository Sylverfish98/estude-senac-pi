from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('agenda/', views.agenda, name='agenda'),
    path('materias/', views.materia, name='materia'),
    path('materias/nova/', views.materia_criar, name='materia_criar'),
    path('materias/<int:pk>/', views.materia_detalhe, name='materia_detalhe'),
    path('materias/<int:pk>/editar/', views.materia_editar, name='materia_editar'),
    path('materias/<int:pk>/deletar/', views.materia_deletar, name='materia_deletar'),
    path('topics/<int:pk>/toggle/', views.topic_toggle_completed, name='topic_toggle_completed'),
    path('topics/<int:pk>/deletar/', views.topic_deletar, name='topic_deletar'),
]
