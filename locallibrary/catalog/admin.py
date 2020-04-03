from django.contrib import admin
from catalog.models import Author, Genre, Book, BookInstance, Language

#admin.site.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=('title','author','display_genre')
admin.site.register(Book,BookAdmin)

#admin.site.register(Author)

#define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

#register the admin class with the associated model
admin.site.register(Author,AuthorAdmin)




admin.site.register(Genre)
#admin.site.register(BookInstance)

class BookInstanceAdmin(admin.ModelAdmin):
    list_display=('book','language','status','due_back')
    list_filter=('status','due_back')
    fieldsets=((None,{'fields':('book','imprint','id')}),
                ('Availability',{'fields':('status','due_back')}),)



admin.site.register(BookInstance,BookInstanceAdmin)


admin.site.register(Language)
