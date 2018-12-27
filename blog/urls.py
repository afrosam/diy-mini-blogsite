from django.urls import path
from . import views
#from django.views.generic import RedirectView

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.BlogListView.as_view(), name='blogs'),
    path('<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
    path('bloggers/', views.BloggerListView.as_view(), name='bloggers'),
    path('blogger/<int:pk>', views.BloggerDetailView.as_view(), name='blogger-detail'),
    path('search/', views.SearchListView.as_view(), name='search'),
    path('<int:pk>/create', views.CommentCreate.as_view(), name='comment')
]
