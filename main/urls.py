from django.urls import path
from main.views import \
    show_main, create_candy_entry, show_xml, show_json, show_xml_by_id, \
    show_json_by_id, register,login_user, logout_user, edit_candy, delete_candy, \
    add_candy_entry_ajax, create_candy_flutter

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-candy-entry', create_candy_entry, name='create_candy_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-candy/<uuid:id>', edit_candy, name='edit_candy'),
    path('delete/<uuid:id>', delete_candy, name='delete_candy'),
    path('create-mood-entry-ajax', add_candy_entry_ajax, name='add_candy_entry_ajax'),
    path('create-flutter/', create_candy_flutter, name='create_mood_flutter'),
]