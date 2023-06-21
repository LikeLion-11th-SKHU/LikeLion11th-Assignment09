from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import DiaryNotForm

def new(request):
    return render(request, 'new.html')

def create(request):
    diary = DiaryNotForm()
    diary.title = request.POST['title']
    diary.pub_date = timezone.now()
    diary.weather = request.POST['weather']
    diary.content = request.POST['content']
    diary.file = request.FILES['file']
    diary.save()
    return redirect('notform')

def notform(request):
    diarys = DiaryNotForm.objects
    return render(request, 'notform.html', {'diarys': diarys})

def detail(request, id):
    diary = get_object_or_404(DiaryNotForm, id = id)
    return render(request, 'detail.html', {'diary': diary})

def edit(request, id):
    edit_diary = DiaryNotForm.objects.get(id = id)
    return render(request, 'edit.html', {'edit_diary': edit_diary})

def update(request, id):
    update_diary = DiaryNotForm.objects.get(id = id)
    update_diary.title = request.POST['title']
    update_diary.pub_date = timezone.now()
    update_diary.weather = request.POST['weather']
    update_diary.content = request.POST['content']
    update_diary.file = request.FILES['file']
    update_diary.save()
    return redirect('notform')

def delete(request, id):
    delete_diary = get_object_or_404(DiaryNotForm, id = id)
    delete_diary.delete()
    return redirect('notform')