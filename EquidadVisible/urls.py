from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from juego import views as juego_views
from test_p import views as test_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('juego/', include('juego.urls')),
    path('test/', test_views.test, name='test'),
    path('login/', user_views.loginPage, name='login'),
    path('logout/', user_views.logoutUser, name='logout'),
    path('register/', user_views.registerPage, name='register'),
]