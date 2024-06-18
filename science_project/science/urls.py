from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.ScientistList.as_view(), name='scientists'),
    path('scientist/<int:pk>/', views.ScientistDetail.as_view(), name='scientist'),
    path('scientist_create/', views.ScientistCreate.as_view(), name='scientist_create'),
    path('scientist_update/<int:pk>/', views.ScientistUpdate.as_view(), name='scientist_update'),
    path('scientist_delete/<int:pk>/', views.ScientistDelete.as_view(), name='scientist_delete'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'), 
    path('register/', views.RegisterPage.as_view(), name='register'),
]
