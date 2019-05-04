"""Welcome URL's config"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='welcome'),
    path('numbers/<str:numbers>', views.add, name='add'),
    path('chat/<str:name>', views.chat, name='chat'),
    path('sumar-edad/<int:age>', views.suma, name='suma')
]