
from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name='homepage'),
    path('delete/<int:id>',views.Delete_record,name='delete'),
]
