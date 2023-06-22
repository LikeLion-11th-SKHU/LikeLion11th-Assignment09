from django.shortcuts import render, redirect, get_object_or_404
from .models import Journal
from .forms import Journalform
from django.utils import timezone



# Create your views here.

def journal(request):
    journals = Journal.objects.all()
    return render(request, 'journal.html', {'journals':journals})

def journal_detail(request, id=id):
    journal = get_object_or_404(Journal, id=id)
    return render(request, 'journal_detail.html', {'journal':journal})

def journal_update(request, id):
    update_journal = get_object_or_404(Journal, id=id)
    if request.method == 'POST':
        form = Journal(request.POST, request.FILES, instance=update_journal)
        if form.is_valid():
            form = form.save(commit=False)
            form.pub_date = timezone.now()
            form.save()
            return redirect('journal')
    else:
        form = Journal(instance=update_journal)
        return render(request, 'journal_update.html', {'form':form})
    
def journal_delete(request, id):
    delete_journal = Journal.objects.get(id=id)
    delete_journal.delete()
    return redirect('journal')

def write(request):
    if request.method == 'POST':
        form = Journalform(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.pub_date = timezone.now()
            form.save()
            return redirect('journal')
    else:
        form = Journalform()
        return render(request, 'write.html', {'form':form})