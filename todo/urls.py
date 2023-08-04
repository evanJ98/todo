from django.urls import path
from . import views

urlpatterns = [
    path('addTask/', views.addTask, name = 'addTask'),
    path('mark_as_done/<int:pk>/', views.markAsDone, name = 'markAsDone'),
    path('mark_as_undone/<int:pk>/', views.markAsUnDone, name = 'markAsUnDone'),

    # Edit Feature
    path('edit_task/<int:pk>/', views.editTask, name = 'editTask'),

    # Delete Feature
    path('delete_task/<int:pk>/', views.deleteTask, name = 'deleteTask'),
]