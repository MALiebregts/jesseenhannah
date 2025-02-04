
from django.contrib import admin
from django.urls import path
from agenda import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/', views.agenda_view, name='agenda'),
]

