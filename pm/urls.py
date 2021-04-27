from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.IndexView.as_view()),
    path('select/',views.SelectView.as_view()),

]