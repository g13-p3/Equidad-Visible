from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from juego_a import views as juego_views
from test_p import views as test_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    #path("register/", user_views.register, name="register"),
    path('juego/', juego_views.juego, name='juego'),
    path('test/', test_views.test, name='test'),
    path('login/', user_views.loginPage, name='login')
]
