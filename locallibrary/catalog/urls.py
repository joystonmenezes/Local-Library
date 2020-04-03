from django.urls import path
from catalog import views


urlpatterns=[
    path('',views.index,name='index'), #index is the unique name for this url mapping
    path('books/',views.BookListView.as_view(),name='books'),
    path('book/<int:pk>',views.BookDetailView.as_view(),name='book-detail'),
]
