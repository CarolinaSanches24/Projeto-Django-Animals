from django.urls import path
from usuarios.views import (cadastroUsers, editar_animal, excluir_animal, logout_view,
    pagina_apos_login, user_login)

urlpatterns = [
    path('cadastroUsers/', cadastroUsers, name ='cadastroUsers'),
    path('user_login/', user_login, name="user_login"),
    path('pagina_apos_login', pagina_apos_login, name='pagina_apos_login'),
    path('logout_view',logout_view, name='logout_view'),
    path('excluir_animal/<uuid:animal_id>/',excluir_animal, name='excluir_animal' ),
    
]