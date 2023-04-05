from django.urls import path

#from blogging.views import detail_view
#from blogging.views import list_view

from blogging.views import ListView, DetailView

urlpatterns = [
    path('', ListView.as_view(), name="blog_index"),
    path('posts/<int:post_id>/', DetailView.as_view(), name="blog_detail"),

]