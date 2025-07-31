from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    
    LogoutView.as_view(template_name=
    LoginView.as_view(template_name=
                      
    # Existing views (e.g., book list and detail view)
    path('', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_book, name='add_book/'),
    path('edit/<int:pk>/', views.edit_book, name='edit_book/'),
    path('delete/<int:pk>/', views.delete_book, name='delete_book/'),
]

