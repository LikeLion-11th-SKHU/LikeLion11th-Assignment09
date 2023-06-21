from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from .models import ReviewNotForm

# Create your views here.
def new(request):
    return render(request, 'new.html')

def create(request):
    review = ReviewNotForm()
    review.title = request.POST['title']
    review.pub_date = timezone.now()
    review.weather = request.POST['weather']
    review.content = request.POST['content']
    review.phto = request.FILES['phto']
    review.save()
    return redirect('notform')

def notform(request):
    reviews = ReviewNotForm.objects
    return render(request, 'notform.html',{'reviews':reviews})

def detail(request,id):
    review = get_object_or_404(ReviewNotForm, id=id)
    return render(request,'detail.html',{'review': review})