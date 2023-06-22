from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from .models import ReviewUseForm
from .forms import ReviewForm

# Create your views here.
def write(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST,request.FILES)
        if form.is_valid():
            form = form.save(commit= False)
            form.pub_date = timezone.now()
            form.save()
            return redirect('useform')
    else:
        form = ReviewForm
        return render(request,'write.html',{'form':form})
    
def useform(request):
    reviews = ReviewUseForm.objects.all()
    return render(request, 'useform.html',{'reviews':reviews})

def detail02(request,id):
    review = get_object_or_404(ReviewUseForm, id=id)
    return render(request,'detail02.html',{'review':review})

def update02(request, id) :
    review = get_object_or_404(ReviewUseForm, id= id)
    if request.method == 'POST':
        form = ReviewForm(request.POST,request.FILES,instance= review)
        if form.is_valid():
            form = form.save(commit=False)
            form.pub_date = timezone.now()
            form.save()
            return redirect('useform')
    else:
        form = ReviewForm(instance=review)
        return render(request, 'update02.html',{'form':form})

def delete02(request, id):
    reviw = get_object_or_404(ReviewUseForm,id=id)
    reviw.delete()
    return redirect('useform')