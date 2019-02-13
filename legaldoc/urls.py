from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required, permission_required
urlpatterns = [
    
    path('', views.index, name='index'),
	path('books/', views.BookListView.as_view(), name='books'),
	path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
	path('authors/', views.AuthorListView.as_view(), name='authors'),
	path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
	#path('header-detaill', views.HeaderDetailView.as_view(), name='header-detaill'),
	path('headerfooterdata', login_required(views.headerfooterdata), name='headerfooterdata'),
	path('headerfooterdata/<int:pk>', login_required(views.HeaderfooterUpdate.as_view()), name='headerfooterupdate'),
	#path('headerfooterdata/<int:pk>', login_required(views.headerfooter_update_form), name='headerfooterupdate'),
	path('simple_upload', views.simple_upload, name='simple_upload'),
	path('signup', login_required(views.signup), name='signup'),
	
	#path('login', views.login, name='login'),
	path('userdata', login_required(views.userdata_view), name='userdata'),
	path('loginn', views.user_login, name='user_login'),
	path('uploadpdffile/', login_required(views.UploadPdffileView.as_view()), name='uploadpdffile'),
	path('pdffiledata', login_required(views.pdffiledata), name='pdffiledata'),
	path('pdffiledata/<int:pk>', login_required(views.PdffileUpdate.as_view()), name='pdffileupdate'),
	path('pdffiledelete/<int:pk>', login_required(views.pdffiledelete), name='pdffiledelete'), 
]

