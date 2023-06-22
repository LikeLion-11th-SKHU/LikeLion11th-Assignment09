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

def create(request):
    if request.method == 'POST':
        form = JournalUseForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.pub_date = timezone.now()
            form.save()
            return redirect('useform')
    else:
        form = JournalUseForm
        return render(request, 'create.html', {'journals' : journals})

def useform(request):
    journals = JournalUseForm.objects
    return render(request, 'useform.html', {'journals' : journals})

def edit(request, id):
    edit_journal = JournalUseForm.objects.get(id = id)
    return render(request, 'edit.html', {'edit_journal': edit_journal})

def update(request, id):
    blog = get_object_or_404(JournalUseForm, id = id)
    if request.method == 'POST':
        form = JournalUseForm(request.POST, instance=blog)
        if form.is_valid():
            form = form.save(commit = False)
            form.pub_date = timezone.now()
            form.save()
            return redirect('useform')
    else:
        journals = JournalUseForm(instance=blog)
        return render(request, 'update.html', {'journals' : journals})

def delete(request, id):
    delete_journal = get_object_or_404(JournalUseForm, id = id)
    delete_journal.delete()
    return redirect('useform')

def detail(request, id):
    journals = get_object_or_404(JournalUseForm, id = id)
    return render(request, 'detail.html', {'journals' : journals})