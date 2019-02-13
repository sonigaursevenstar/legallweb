from django.conf import settings
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
   is_client = models.BooleanField(default=False)
   Hourly_fee = models.FloatField(null=True, blank=True)
   Phone_number = models.CharField(max_length=45) 
   Calendar_name = models.CharField(max_length=20) 
class Genre(models.Model):
 """Model representing a book genre."""
 name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')
def __str__(self):return self.name
 # Used to generate URLs by reversing the URL patterns

class Book(models.Model):
 """Model representing a book (but not a specific copy of a book)."""
 title = models.CharField(max_length=200)

 # Foreign Key used because book can only have one author, but authors can have multiple books
 # Author as a string rather than object because it hasn't been declared yet in the file
 author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
 
 summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
 isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
 
 # ManyToManyField used because genre can contain many books. Books can cover many genres.
 # Genre class has already been defined so we can specify the object above.
 genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
 #1
 
 
 #1
 def __str__(self):return self.title
 
 def get_absolute_url(self):return reverse('book-detail', args=[str(self.id)])

# changed
#def get_absolute_url(self):return reverse('BookListView', args=[str(self.id)])
import uuid # Required for unique book instances

class BookInstance(models.Model):
 """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
 id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
 book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True) 
 imprint = models.CharField(max_length=200)
 due_back = models.DateField(null=True, blank=True)

 LOAN_STATUS = (
 ('m', 'Maintenance'),
 ('o', 'On loan'),
 ('a', 'Available'),
 ('r', 'Reserved'),
 )

 status = models.CharField(
 max_length=1,
 choices=LOAN_STATUS,
 blank=True,
 default='m',
 help_text='Book availability',
 )

 class Meta:ordering = ['due_back']

 def __str__(self):return f'{self.id} ({self.book.title})'
class Author(models.Model):
 first_name = models.CharField(max_length=100)
 last_name = models.CharField(max_length=100)
 date_of_birth = models.DateField(null=True, blank=True)
 date_of_death = models.DateField('Died', null=True, blank=True)

 class Meta: ordering = ['id']
 
 def get_absolute_url(self): return reverse('author-detail', args=[str(self.id)])

 def __str__(self):return f'{self.last_name}, {self.first_name}'
 
class Abhi(models.Model):
 fname = models.CharField(max_length=100)
 lname = models.CharField(max_length=100,null=True)
 date_of_birth = models.DateField(null=True, blank=True)
 date_of_death = models.DateField('Died', null=True, blank=True)

 class Meta: ordering = ['id']
 
 def get_absolute_url(self): return reverse('abhi-detail', args=[str(self.id)])

 def __str__(self):return f'{self.lname}, {self.fname}'


class Authort(models.Model):
 first_name = models.CharField(max_length=100)
 last_name = models.CharField(max_length=100,null=True)
 date_of_birth = models.DateField(null=True, blank=True)
 date_of_death = models.DateField('Died', null=True, blank=True)

 class Meta: ordering = ['id']
 
 def get_absolute_url(self): return reverse('author-detaill', args=[str(self.id)])

 def __str__(self):return f'{self.last_name}, {self.first_name}'
 
class Headerfooter(models.Model):
 type = models.CharField(max_length=100)
 #content = models.CharField(max_length=200,null=True)
 content= models.CharField(max_length=200,null=True,blank=True)
 #img = models.CharField(max_length=200,null=True)
 img = models.FileField(upload_to='documents/',null=True,blank=True)
 class Meta: ordering = ['id']
 
 def get_absolute_url(self): return reverse('headerfooterupdate', args=[str(self.id)])


 def __str__(self):return f'{self.type}, {self.content},{self.img}' 
 
 # for user registered by admin 
class Personnel(models.Model):
  """user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )"""
  #user = models.OneToOneField(User)
  """user = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,default=True, null=True
  )"""
  user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
  #user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
  #--NAME = models.CharField(max_length=100)
  #--Email_address = models.CharField(max_length=45)
  #--Password = models.CharField(max_length=45)
  #username = models.CharField(max_length=50,null=True, blank=True)
  #--Hourly_fee = models.FloatField(null=True, blank=True)
  #  --Phone_number = models.CharField(max_length=45) 
  #--Calendar_name = models.CharField(max_length=20) 
   # last_login = models.DateTimeField(null=True, blank=True)
   #is_superuser = models.PositiveSmallIntegerField(default=0,null=True, blank=True)
   #first_name = models.CharField(max_length=30,null=True, blank=True) 
   #last_name = models.CharField(max_length=30,null=True, blank=True) 
  #is_staff = models.PositiveSmallIntegerField(default=0)
  #is_active = models.PositiveSmallIntegerField(null=True, blank=True)
  #date_joined=models.DateTimeField(null=True,blank=True)
	
  #def __str__(self):return self.NAME
 
 # def get_absolute_url(self):return reverse('personnel-detail', args=[str(self.id)])
 
 
class Param_values(models.Model):
 
 Parameter_name = models.CharField(max_length=20,default=True,null=True,blank=True)
 Case_NAME = models.CharField(max_length=10,default=True,null=True,blank=True)
 Person_id = models.CharField(max_length=10,default=True,null=True,blank=True)
 Value = models.FileField(upload_to='upload_pdffile/',default=True,null=True,blank=True)
 class Meta: ordering = ['id']
 
 def get_absolute_url(self): return reverse('pdffileupdate', args=[str(self.id)])


 def __str__(self):return f'{self.Parameter_name}, {self. Case_NAME},{self.Person_id},{self.Value}' 
 def delete(self, *args, **kwargs):
        self.Value.delete(save=False)
        super().delete(*args, **kwargs) 
