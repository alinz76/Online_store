from django.urls import path
from . import views


app_name = 'item'

urlpatterns = [
    path('', views.items, name='items'),
    path('<int:pk>', views.detail, name='detail'),
    path('add/', views.new_item, name='new_item'),
    path('<int:item_id>/delete/', views.delete_item, name='delete_item'),
    path('<int:item_id>/edit/', views.edit_item, name='edit_item'),
]