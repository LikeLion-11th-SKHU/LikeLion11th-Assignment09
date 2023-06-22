from django.shortcuts import render, redirect, get_object_or_404
from .models import Journal
from django.utils import timezone



# Create your views here.

def journal(request):
    journals = Journal.objects.all()
    return render(request, 'journal.html', {'journals':journals})

def journal_detail(request, journal_id):
    journal_detail = Journal.objects.get(id=journal_id)
    return render(request, 'journal_detail.html', {'journal_detail':journal_detail})

def journal_update(request, journal_id):
    update_journal = Journal.objects.get(id=journal_id)
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
    
def journal_delete(request, journal_id):
    delete_journal = Journal.objects.get(id=journal_id)
    delete_journal.delete()
    return redirect('journal')

def write(request):
    if request.method == 'POST':
        form = Journal(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.pub_date = timezone.now()
            form.save()
            return redirect('journal')
    else:
        form = Journal()
        return render(request, 'write.html', {'form':form})