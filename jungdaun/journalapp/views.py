from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import JournalUseForm

# Create your views here.
def write(request):
    if request.method == 'POST':
        form = JournalUseForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit = False)
            form.pub_date = timezone.now()
            form.save()
            return redirect('useform')
    else:
        form = JournalUseForm
        return render(request, 'write.html', {'form' : form})

def useform(request):
    journals = JournalUseForm.objects.all()
    return render(request, 'useform.html', {'journals' : journals})

def update(request, id):
    journal = get_object_or_404(JournalUseForm, id = id)
    if request.method == 'POST':
        form = JournalUseForm(request.POST, request.FILES, instance = journal)
        if form.is_valid():
            form = form.save(commit = False)
            form.pub_date = timezone.now()
            form.save()
            return redirect('useform')
    else:
        form = JournalUseForm(instance = journal)
        return render(request, 'update.html', {'form': form})

def delete(request, id):
    journal = get_object_or_404(JournalUseForm, id = id)
    journal.delete()
    return redirect('useform')


def detail1(request, id):
    journals = get_object_or_404(JournalUseForm, id = id)
    return render(request, 'detail1.html', {'journals' : journals})