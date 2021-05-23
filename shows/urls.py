from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('shows',views.all_shows),
    path('shows/new',views.create),
    path('shows/<int:show_id>',views.one_show),
    path('shows/<int:show_id>/edit',views.edit),
    path('shows/<int:show_id>/delete',views.delete),
]