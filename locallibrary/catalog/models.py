from django.db import models
from django.urls import reverse
import uuid

# Create your models here.


class Genre(models.Model):
    '''
        model representing book genre
    '''
    name=models.CharField(max_length=100,help_text='Enter a book genre')

    def __str__(self):
        '''
            string representing model object
        '''
        return self.name


class Book(models.Model):
    '''
        model representing a book (not a specific copy)
    '''

    title=models.CharField(max_length=100)
    author=models.ForeignKey('Author',on_delete=models.SET_NULL,null=True)    #assuming that each book will have only one author
    summary=models.TextField(max_length=1000,help_text='Enter a brief description of the book')
    isbn=models.CharField('ISBN',max_length=13,help_text='Enter ISBN number')

    genre=models.ManyToManyField(Genre,help_text='Select an appropriate genre for this book')


    def display_genre(self):
        '''
        Create a string for the genre. This is required to display genre in admin

        '''
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description='Genre'



    def __str__(self):
        '''
            string representing model object
        '''
        return self.title

    def get_absolute_url(self):
        '''
            returns url to access a detail record for this book
        '''
        return reverse('book-detail',args=[str(self.id)])


class BookInstance(models.Model):
    '''
        model representing a specific copy of a book that can be borrowed from the library
    '''
    id=models.UUIDField(primary_key=True,default=uuid.uuid4, help_text='Unique ID for this particular book across the whole library')
    book=models.ForeignKey(Book,on_delete=models.SET_NULL,null=True)
    imprint=models.CharField(max_length=200)
    language=models.ForeignKey('Language',on_delete=models.SET_NULL,null=True)
    due_back=models.DateField(null=True,blank=True)


    LOAN_STATUS=(('m','Maintenance'),('o','On loan'),('a','Available'),('r','Reserved'),)

    status=models.CharField(max_length=1,choices=LOAN_STATUS,blank=True,default='m',help_text='Book availability',)

    class Meta:
        ordering=['due_back']

    def __str__(self):
        '''
            string representing model object
        '''
        return f'{self.id} ({self.book.title})'



class Author(models.Model):
    '''
        model representing an author
    '''

    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    date_of_birth=models.DateField(null=True,blank=True)
    date_of_death=models.DateField('Died',null=True,blank=True)

    class Meta:
        ordering=['last_name','first_name']

    def get_absolute_url(self):
        '''
            returns the url to access a particular author instance
        '''
        return reverse('author-detail',args=[str(self.id)])


    def __str__(self):
        '''
            string representing model object
        '''
        return f'{self.last_name}, {self.first_name}'



class Language(models.Model):
    '''
        model representing a language in which a book might be available
    '''
    name=models.CharField(max_length=100,help_text='Enter script language')

    def __str__(self):
        '''
            string representing model object
        '''
        return self.name
