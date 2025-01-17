from django.shortcuts import render, get_object_or_404, redirect
from .models import Subject


def subject_list(request):
    subject = Subject.objects.all()
    ctx = {'subject': subject}
    return render(request, 'subjects/subject_list.html', ctx)


def subject_detail(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    ctx = {'subject': subject}
    return render(request, 'subjects/subject_detail.html', ctx)


def subject_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Subject.objects.create(
                name=name
            )
            return redirect('subjects:subjects_list')
    return render(request, 'subjects/subject_form.html')


def subject_update(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            subject.name = name
            subject.save()
            return redirect(subject.get_detail_url())
    return render(request, 'subjects/subject-add.html')


def subject_delete(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        subject.delete()
    return redirect('subjects:subject_list')
