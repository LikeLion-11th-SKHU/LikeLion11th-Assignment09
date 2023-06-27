from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import DiaryNotForm

# Create your views here.
def new(request):
    return render(request, 'new.html')

def create(request):
    diary = DiaryNotForm()
    diary.diary = request.POST['diary']
    diary.title = request.POST['title']
    diary.pub_date = timezone.now()
    diary.weather = request.POST['weather']
    diary.image = request.FILES['image']
    diary.save()
    return redirect('diary')

def diary(request):
    diaries = DiaryNotForm.objects
    return render(request, 'diary.html', {'diaries' : diaries})

def detail(request, id):
    diary = get_object_or_404(DiaryNotForm, id=id)
    return render(request, 'detail.html', {'diary':diary})

def edit(request, id):
    edit_diary = DiaryNotForm.objects.get(id = id)
    return render(request, 'edit.html', {'edit_diary':edit_diary})

def update(request, id):
    update_diary = DiaryNotForm.objects.get(id = id)
    update_diary.title = request.POST['title']
    update_diary.pub_date = timezone.now()
    update_diary.diary = request.POST['diary']
    update_diary.weather = request.POST['weather']
    if 'image' in request.FILES:
        update_diary.image = request.FILES['image']
    update_diary.save()
    return redirect('diary')

def delete(request, id):
    delete_diary = get_object_or_404(DiaryNotForm, id = id)
    delete_diary.delete()
    return redirect('diary')