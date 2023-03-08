from django.urls import path
from . import views

urlpatterns = [
    path('', views.model_create_view, name='model_add'),
    path('about_autobuddy/', views.load_about, name='load_about'),
    path('autobuddy_estimator/', views.load_autobuddy_estimator, name='load_estimator'),
    path('autobuddy_is_it_fair/', views.load_is_it_fair, name='load_fair'),
    path('autobuddy_make_report/', views.load_make_a_report, name='load_reporter'),
    path('<int:pk>/', views.model_update_view, name='model_change'),
    path('ajax/load-models/', views.load_models, name='ajax_load_models'), # AJAX
]