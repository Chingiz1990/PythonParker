from django.urls import path

from posts.views import post_list

urlpatterns = [
    path('blog/', post_list)
]