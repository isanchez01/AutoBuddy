from django.urls import path
from . import views

urlpatterns = [
    path('', views.model_create_view, name='model_add'),
    path('<int:pk>/', views.model_update_view, name='model_change'),
    path('ajax/load-models/', views.load_models, name='ajax_load_models'), # AJAX
]