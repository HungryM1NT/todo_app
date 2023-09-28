from django.urls import path
from app.views import registration, login, logout, add_note, delete_note

app_name = 'app'

urlpatterns = [
    path('registration/', registration, name='registration'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('add_note/', add_note, name='add_note'),
    path('delete_note/<int:note_id>/', delete_note, name='delete_note')
]