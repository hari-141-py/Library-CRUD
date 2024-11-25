from django.shortcuts import render
from books.models import Book
from django.contrib.auth.decorators import login_required


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

# Create your views here.

@login_required
def book_view(request):
    u=request.user
    k=Book.objects.filter(user=u)
    return render(request,'book_view.html', {'book':k})

@login_required
def add_book(request):
    if(request.method == 'POST'):
        tit=request.POST['tit']                             #tit=request.POST.get('tit')
        auth=request.POST['auth']                           #auth=request.POST.get('auth')
        lang=request.POST['lang']       #ALTERNATIVE WAY    #lang=request.POST.get('lang')
        prc=request.POST['prc']                             #prc=request.POST.get('prc')
        pge=request.POST['pge']                             #pge=request.POST.get('pge')

        cvr=request.FILES['cvr']
        pdf1=request.FILES['pdf1']

        det = request.POST['det']

        b=Book.objects.create(title=tit,author=auth,language=lang,price=prc,pages=pge,cover=cvr,pdf=pdf1,details=det)
        b.save()
        return book_view(request)
    return render(request,'add_book.html',{})

@login_required
def edit_book(request,i):
    k=Book.objects.get(id=i)
    if(request.method == 'POST'):
        k.title = request.POST['tit']
        k.author = request.POST['auth']
        k.language = request.POST['lang']
        k.price = request.POST['prc']
        k.pages = request.POST['pge']
        k.details = request.POST['det']
        if(request.FILES.get('cvr')== None):
            k.save()
        else:
            k.cover = request.FILES['cvr']
        if (request.FILES.get('pdf1') == None):
            k.save()
        else:
            k.pdf = request.FILES['pdf1']
        return book_view(request)
    return render(request,'edit_book.html',{'book':k})

@login_required
def delete_book(request,d):
    k=Book.objects.get(id=d)
    k.delete()
    return book_view(request)

from django.db.models import Q       # Q object in quesrry used when we include AND OR in a query
def search_book(request):
    k=None   # Initialize k as None
    if(request.method == 'POST'):
        srch_item = request.POST.get('srch_item')
        if srch_item:
            k = Book.objects.filter(Q(title__icontains=srch_item) | Q(author__icontains=srch_item))
    return render(request,'search_book.html',{'srch':k})

















