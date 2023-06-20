from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import JournalUseForm
from .forms import JournalForm

# Create your views here.
def write(request):
    if request.method == 'POST':
        form = JournalForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit = False)
            form.pub_date = timezone.now()
            form.save()
            return redirect('journal')
    else:
        form = JournalForm
        return render(request, 'write.html', {'form' : form})

def journal(request):
    journals = JournalUseForm.objects.all()
    return render(request, 'journal.html', {'journals' : journals})

def detail2(request, id):
    journal = get_object_or_404(JournalUseForm, id=id)
    return render(request, 'detail2.html', {'journal': journal})

def update2(request, id):
    journal = get_object_or_404(JournalUseForm, id = id)
    if request.method == 'POST':
        form = JournalForm(request.POST, request.FILES, instance= journal)
        if form.is_valid():
            form = form.save(commit = False)
            form.pub_date = timezone.now()
            form.save()
            return redirect('journal')
    else:
        form = JournalForm(instance=journal)
        return render(request, 'update2.html', {'form' : form})
    
def delete2(id):
    journal = get_object_or_404(JournalUseForm, id = id)
    journal.delete()
    return redirect('journal')