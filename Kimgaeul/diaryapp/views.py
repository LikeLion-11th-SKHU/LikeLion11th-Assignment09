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
    review.photo = request.FILES['photo']
    review.save()
    return redirect('notform')

def notform(request):
    reviews = ReviewNotForm.objects
    return render(request, 'notform.html',{'reviews': reviews})

def detail(request,id):
    review = get_object_or_404(ReviewNotForm, id=id)
    return render(request,'detail.html',{'review': review})

def edit(request,id):
    edit_review = ReviewNotForm.objects.get(id = id)
    return render(request, 'edit.html', {'edit_review': edit_review})

def update(request,id):
    update_review = ReviewNotForm.objects.get(id=id)
    update_review.title = request.POST['title']
    update_review.pub_date = timezone.now()
    update_review.weather = request.POST['weather']
    update_review.content = request.POST['content']
    update_review.photo = request.FILES.get('photo')
    update_review.save()
    return redirect('notform')

def delete(request,id):
    delete_review = get_object_or_404(ReviewNotForm,id=id)
    delete_review.delete()
    return redirect('notform')