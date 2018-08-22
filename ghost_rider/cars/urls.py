from django.urls import path
from . import views
from django.conf.urls import url, include

from rest_framework.authtoken import views as rest_framework_views

urlpatterns = [
  path('api/cars/', views.CarList.as_view(), name='car-list'),
  path('api/cars/<int:pk>', views.CarDetail.as_view(), name='car-detail'),
  path('api/comments/', views.CommentList.as_view(), name='comment-list'),
  path('api/comments/<int:pk>', views.CommentDetail.as_view(), name='comment-detail'),
  path('api/get_csrf/', views.get_csrf),

    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()), 
    # url('api/api-auth/', include( 'rest_framework.urls', namespace='rest_framework')),
    # url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^get_auth_token/$', rest_framework_views.obtain_auth_token, name='get_auth_token'),
    url(r'^api/users/$', views.UserCreate.as_view(), name='account-create'),

  # url(r'^users/$', views.UserList.as_view()),
  # url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()), 
  # # url(r'^api-auth/', include('rest_framework.urls')), 
  # # url(r'^api-auth/', include( 'rest_framework.urls', namespace='rest_framework')),
  # url('api/api-auth/', include( 'rest_framework.urls', namespace='rest_framework')),

]

