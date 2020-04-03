from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic


def index(request):
    '''
        View function for home page of the site
    '''
    book_count=Book.objects.all().count()
    book_instance_count=BookInstance.objects.all().count()

    available_instance_count=BookInstance.objects.filter(status__exact='a').count()

    author_count=Author.objects.all().count()

    num_visits=request.session.get('num_visits',0)
    request.session['num_visits']=num_visits+1


    context={ 'num_books': book_count, 'num_instances': book_instance_count, 'num_instances_available': available_instance_count, 'num_authors': author_count, 'num_visits': num_visits, }

    return render(request,'index.html', context=context)


class BookListView(generic.ListView):
    model=Book
    paginate_by=2



class BookDetailView(generic.DetailView):
    model=Book
