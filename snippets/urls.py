from django.urls import path
from snippets import views

urlpatterns = [
    path("snippets/", views.snippet_list),
    path("snippets/user/", views.snippet_user),
    path("snippets/<int:pk>/", views.snippet_detail),
]
