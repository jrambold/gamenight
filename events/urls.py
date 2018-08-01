from django.urls import path

from . import views

app_name = 'events'
urlpatterns = [
    path('', views.index, name='index'),
    path('event/<int:event_id>/', views.event_show, name='eventShow'),
	path('signup/', views.signup, name='signup'),
	path('login/', views.login_view, name='login'),
	path('logout/', views.logout_view, name='logout'),
	path('user/activate/', views.activate, name='activate'),
    path('user/create_event/', views.create_event, name='createEvent'),
    path('user/friend_request/', views.friend_request, name='friendRequest'),
    path('user/frequest/', views.frequest, name='acceptFRequest'),
    path('event/<int:event_id>/change_status/', views.change_status, name='changeStatus'),
    path('event/<int:event_id>/add_game/', views.add_game, name='addGame'),
]
