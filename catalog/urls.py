#from django.urls import path
#from django.urls import include

#urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('catalog/', include('catalog.urls')),
from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    #url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    url(r'^author/$', views.AuthorListWiew.as_view(), name='author'),
    url(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
]