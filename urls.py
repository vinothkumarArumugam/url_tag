
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('geeks',views.geeks_view ,name='template1'),
    path('pyetho',views.nav_view ,name='template2' ),
]
