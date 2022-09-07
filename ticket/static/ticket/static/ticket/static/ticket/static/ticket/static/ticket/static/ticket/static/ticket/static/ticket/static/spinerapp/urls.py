from django.urls import path
from .import views
from django.contrib import admin
urlpatterns = [
    path('browser',views.browser,name="browser"),
    path('index',views.index,name="index"),
    path('show',views.data_show,name="show"),
    path('admin/', admin.site.urls)
]
