from django.urls import path
from restro_admin import views

urlpatterns = [
    path('', views.admin_login,name='admin-login'),
    path('home/',views.admin_home,name='admin-home'),
    path('admin-login-check/',views.admin_login_check,name='admin-login-check'),
    path('logout/',views.admin_logout,name='admin-logout'),

    # state
    path('open_area/', views.open_state, name="open_state"),
    path('save_state/', views.save_state, name="save_state"),
    path('update_state/', views.update_state, name="update_state"),
    path('update_state_data/', views.update_state_data, name="update_state_data"),
    path('delete_state/', views.delete_state, name='delete_state'),

    # City
    path('open_city/', views.open_city, name="open_city"),
    path('save_city/', views.save_city, name="save_city"),
    # path('update_city/', views.update_city, name="update_city"),
    # path('update_city_data/', views.update_city_data, name="update_city_data"),
    # path('delete_city/', views.delete_city, name='delete_city'),

    # Area
    path('area/',views.AreaView.as_view(),name='area')

    # Type
    #path('open_type/', views.open_type, name="open_type"),
    #path('save_type/', views.save_type, name="save_type"),

]
