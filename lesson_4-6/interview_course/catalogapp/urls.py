from django.urls import path

from catalogapp import views

app_name = 'catalogapp'

urlpatterns = [
    path('', views.IndexPageView.as_view(), name='index'),
    path('category/<int:pk>/', views.CategoryPageView.as_view(),
         name='category')
]
