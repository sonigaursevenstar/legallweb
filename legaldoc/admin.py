from django.contrib import admin

#from catalog.models import Author, Genre, Book, BookInstance,Setting
from legaldoc.models import Author, Genre, Book, BookInstance,Authort,Abhi,Headerfooter,Personnel
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
 list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
 fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)
# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
 list_filter = ('status', 'due_back')
 fieldsets = (
 (None, {
 'fields': ('book', 'imprint', 'id')
 }),
 ('Availability', {
 'fields': ('status', 'due_back')
 }),
    )
class AuthortAdmin(admin.ModelAdmin):
 list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
 fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
# Register the admin class with the associated model
 admin.site.register(Authort, AuthorAdmin)
@admin.register(Headerfooter) 
class HeaderfooterAdmin(admin.ModelAdmin):
 list_display = ('type', 'content')
 fields = ['type', 'content']
 
"""@admin.register(Personnel) 
class PersonnelAdmin(admin.ModelAdmin):
 list_display = ('type', 'content')
 fields = ['type', 'content'] """
# Register the admin class with the associated model


