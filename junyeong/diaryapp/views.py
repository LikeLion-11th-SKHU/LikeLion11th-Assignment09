from django.shortcuts import render, redirect, get_object_or_404
from .models import Diarynotform
from django.utils import timezone



# Create your views here.

def new(request):
    return render(request, 'new.html')

def create(request):
    diary = Diarynotform()
    diary.diary = request.POST['diary']
    diary.title = request.POST['title']
    diary.pub_date = timezone.datetime.now()
    diary.weather = request.POST['weather']
    diary.body = request.POST['body']
    diary.image = request.FILES['image']
    diary.save()
    return redirect('diary')

def diary(request):
    diary = Diarynotform.objects
    return render(request, 'diary.html', {'diary':diary})

def detail(request, diary_id):
    diary = get_object_or_404(Diarynotform, id=id)
    return render(request, 'detail.html', {'diary':diary})

def edit(request, diary_id):
    diary_edit = Diarynotform.objects.get(id=diary_id)
    return render(request, 'edit.html', {'diary_edit':diary_edit})

def update(request, diary_id):
    update_diary = Diarynotform.objects.get(id=diary_id)
    update_diary.title = request.POST['title']
    update_diary.weather = request.POST['weather']
    update_diary.body = request.POST['body']
    update_diary.image = request.FILES.get('image')
    update_diary.save()
    return redirect('detail', update_diary.id)

def delete(request, diary_id):
    delete_diary = get_object_or_404(Diarynotform,id=diary_id)
    delete_diary.delete()
    return redirect('diary')