
from django.contrib import admin
from django.urls import include, path
from principal.views import base, lista_usuarios, crear_usuario
from django.contrib.auth import views as auth_views
from principal import views
from principal.views import base, lista_usuarios, crear_usuario, login_view, logout_view

urlpatterns = [
    path('', base, name='base'),  # Ruta para la página base.html (página principal)
    path('usuarios/', lista_usuarios, name='lista_usuarios'),  # Ruta para la página lista_usuarios.html
    path('admin/', admin.site.urls),
    path('', include('principal.urls')),
    path('crear-usuario/', crear_usuario, name='crear_usuario'),
    path('login/', auth_views.LoginView.as_view(template_name='principal/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='base'), name='logout'),
    path('accounts/profile/', views.profile_view, name='perfil'),
]
