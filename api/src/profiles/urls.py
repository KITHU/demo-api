from django.urls import path
from .views import ProfileViewSet


profile = ProfileViewSet.as_view({
    'get': 'retrieve',
    'patch': 'update'
})

profile_list = ProfileViewSet.as_view({
    'get':'list'
})


urlpatterns = [
    path('profile/<int:pk>/', profile, name="profile"),
    path('profile/', profile_list, name="profile_list"),
]
