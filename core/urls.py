from django.contrib.auth import views as auth_views
from django.urls import path

from .views import home, contact, signup
from .forms import LoginForm

app_name = "core"

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path("signup/", signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name="core/login.html", authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]