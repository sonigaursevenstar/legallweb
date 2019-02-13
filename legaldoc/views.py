from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from legaldoc.forms import DocumentForm, SignUpForm, Person, User
from django.core.files.storage import FileSystemStorage
from django.views.generic.edit import UpdateView
# 17 jan from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404		
# 17 jan from django.shortcuts import redirect
from legaldoc.models import Book, Author, BookInstance, Genre,Headerfooter,Personnel, Param_values
from django.contrib import messages
# for login signup
from django.contrib.auth import authenticate, login

# for login signup
# for password
from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout

from django.db import IntegrityError
from django.db.models.signals import post_save
#for password

from django.contrib.auth.decorators import login_required

from django.views.generic.edit import FormView
from django.views.generic import TemplateView, ListView, CreateView
from django.shortcuts import redirect
from django.contrib.auth.decorators import user_passes_test

def index(request):
    
	 
    if not request.user.is_authenticated:
      return render(request, 'registration/login.html')   
     
	  
    return render(request, 'index.html') 
   
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
  
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
   
    num_authors = Author.objects.count()
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    
    return render(request, 'index.html', context=context)

from django.views import generic

class BookListView(generic.ListView):
    model = Book
paginate_by = 1
def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context
		
class BookDetailView(generic.DetailView):model = Book
from django.shortcuts import get_object_or_404

def book_detail_view(request, primary_key):
    try:
        book = Book.objects.get(pk=primary_key)
    except Book.DoesNotExist:
        raise Http404('Book does not exist')
    
    return render(request, 'catalog/book_detail.html', context={'book': book})
class AuthorListView(generic.ListView):model = Author
paginate_by = 1
def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(AuthorListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context
class AuthorDetailView(generic.DetailView):model = Author

def headerfooterdata(request):
 data = Headerfooter.objects.all()
 context = {
        'data': data,
            }
 return render(request, 'headerfooterdata.html', context=context)
"""class HeaderfooterUpdate(UpdateView):
    model = Headerfooter
    fields = ['type','content']
    template_name_suffix = '_update_form'"""

#class HeaderfooterUpdate(UpdateView):
class HeaderfooterUpdate(UpdateView):
    model = Headerfooter
	
    fields = ['type','img','content']
    template_name_suffix = '_update_form'
	
    def get_success_url(self):
     messages.success(self.request, 'Data updated')
     return '/legaldoc/headerfooterdata'
"""
image upload  using method  
def headerfooter_update_form(request, pk):
    
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
           
    else:
        form = DocumentForm()
    return render(request, 'catalog/simple_upload.html', {
        'form': form
    })"""
	
def simple_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
           
    else:
        form = DocumentForm()
    return render(request, 'catalog/simple_upload.html', {
        'form': form
    })
@login_required
def login(request):
    return render_to_response('index.html')

@user_passes_test(lambda u: u.is_superuser)		
def signup(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
			
            password   = user_form.cleaned_data['password'] 
			
            user.password = make_password(password)
			
            user.save()
			#User = User.objects.create(is_client=True)
            personnel = Personnel.objects.create(user=user)
            messages.success(request,'User Data Saved') 
            return redirect('/legaldoc/userdata')
            #form.save()
            """username = user_form.cleaned_data.get('Email_address')
            raw_password = user_form.cleaned_data.get('Password')
            user = authenticate(Email_address=username, password=raw_password)
            login(request, user,backend='catalog.auth_backends.MyAuthBackend')
            return redirect('/') """

    else:
        #user_form.add_error('password_confirm', 'The passwords do not match')
        user_form = SignUpForm()
    return render(request, 'signup.html', {'form': user_form})	

def loginnnnn(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            password   = user_form.cleaned_data['Password']  
            user.Password = make_password(password)
            user.save()
            #form.save()
            username = user_form.cleaned_data.get('Email_address')
            raw_password = user_form.cleaned_data.get('Password')
            user = authenticate(Email_address=username, password=raw_password)
            login(request, user)
            return redirect('/') 

    else:
        user_form = SignUpForm()
    return render(request, 'signup.html', {'form': user_form})	
	
	
def user_login(request):
    if request.method == 'POST':
        form = Person(request.POST)
        if form.is_valid():
            Email_address = request.POST['Email_address']
            Password = request.POST['Password']
            user = authenticate(request, Email_address=Email_address, Password=Password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated sucessfully')
                else:
                    return HttpResponse('Disable account')
            else:
              return HttpResponse('Invalid Login') 
             #return render(request, 'user_login.html', {})
			 
    else:
        form = Person()
        return render(request, 'user_login.html', {'form': form})	
#for superuser
@user_passes_test(lambda u: u.is_superuser)	
def userdata_view(request):

 data = User.objects.all()
 context = {
        'data': data,
            }
 return render(request, 'userdata.html', context=context)	
 
class UploadPdffileView(CreateView):
    model = Param_values
	
    fields = ['Parameter_name','Case_NAME','Person_id','Value']
    template_name_suffix = '_pdffile_form'
    success_url = '/legaldoc/pdffiledata'
    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('Value')
        messages.success(request,'File Uploaded')
        if form.is_valid():
            for f in files:
                ...  
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
def after_login(request):
    if not request.user.is_authenticated():
        redirect('some-non-existence-page-or-404',...)
    #Your code
    return
	
	
def pdffiledata(request):
 
 data = Param_values.objects.filter(Person_id = request.user.id)
 context = {
        'data': data,
            }
 return render(request, 'pdffiledata.html', context=context)
 
class PdffileUpdate(UpdateView):
    model = Param_values
	
    fields = ['Parameter_name','Case_NAME','Value']
    template_name_suffix = '_update_form'
	
    def get_success_url(self):
     messages.success(self.request, 'Data updated')
     return '/legaldoc/pdffiledata'

def pdffiledelete(request, pk):
 
  query = Param_values.objects.get(pk=pk)
  query.delete()
  messages.success(request,'Data Deleted') 
  return redirect('/legaldoc/pdffiledata')
