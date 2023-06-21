from django.shortcuts import render, redirect
from django.utils import timezone
from .models import JournalUseForm

# Create your views here.
def write(request):
    return render(request, 'write.html')

def create(request):
    diary = JournalUseForm()
    diary.title = request.POST['title']
    diary.date = timezone.now()
    diary.weather = request.POST['weather']
    diary.content = request.POST['content']
    diary.file = request.FILES['file']
    diary.image = request.FILES['image']
    diary.save()
    return redirect('useform')

def useform(request):
    journals = JournalUseForm.objects
    return render(request, 'useform.html', {'journal' : journals})

def update(request, id):
    update_diary = JournalUseForm.objects.get(id = id)
    update_diary.title = request.POST['title']
    update_diary.date = timezone.now()
    update_diary.weather = request.POST['weather']
    update_diary.content = request.POST['content']
    update_diary.file = request.FILES['file']
    update_diary.image = request.FILES['image']
    update_diary.save()
    return redirect('useform')

def delete(request, id):
    delete_diary = get_object_or_404(JournalUseForm, id = id)
    delete_diary.delete()
    return redirect('useform')