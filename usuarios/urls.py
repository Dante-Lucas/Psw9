from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('cadastro/', views.cadastro, name="cadastro"),
    path('login/',views.login, name="login"),
    path('logout/',views.logout, name="logout"),
    path('change_password/',auth_views.PasswordChangeView.as_view(template_name='registration/troca_senha.html'), name="troca_senha"),
    path('change_password_success/', auth_views.PasswordChangeDoneView.as_view(template_name = 'registration/troca_feita.html'), name="password_change_done"),
    path('reset_password/',auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(), name="reset_password_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(), name="reset_password_complete"),
    
]