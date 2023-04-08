from django.urls import path
from . import views

urlpatterns = [
    path('materias/', views.MateriaListView.as_view(), name='materia_list'),
    path('materias/<int:pk>/', views.MateriaDetailView.as_view(), name='materia_detail'),
    path('materias/new/', views.materia_new, name='materia_new'),
    path('materias/<int:pk>/edit/', views.materia_edit, name='materia_edit'),
    path('materias/<int:pk>/delete/', views.materia_delete, name='materia_delete'),
    path('assuntos/', views.AssuntoListView.as_view(), name='assunto_list'),
    path('assuntos/new/', views.assunto_new, name='assunto_new'),
    path('assuntos/<int:pk>/', views.AssuntoDetailView.as_view(), name='assunto_detail'),
    path('assuntos/<int:pk>/edit/', views.assunto_edit, name='assunto_edit'),
    path('assuntos/<int:pk>/delete/', views.assunto_delete, name='assunto_delete'),



]
