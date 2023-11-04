from django.urls import path
from . import views

urlpatterns = [
   # path("progol/", views.progol, name ="progol"),
    path("usuarios/", views.usuarios, name ="usuarios"),
    path("saveUser/", views.saveUser, name ="saveUser"),
    path("deletUser/<str:id>/", views.deletUser, name="deletUser"),
    path("editUser/<str:id>/", views.editUser, name="editUser"),
    path("subirVideo/<str:id>/", views.subirVideo, name="subirVideo"),
    path("listarVideos/<str:id>/", views.listarVideos, name="listarVideos"),
    path("editVideo/<str:id>/", views.editVideo, name="editVideo"),
]


