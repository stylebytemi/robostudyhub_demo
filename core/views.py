from django.shortcuts import render, redirect
from .forms import RegisterForm
from .forms import DocumentUploadForm
from django.contrib.auth.decorators import login_required
from .models import Document

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('upload_document')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


@login_required
def upload_document(request):
    if request.method == 'POST':
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            if not form.cleaned_data['anonymous']:
                document.uploaded_by = request.user
            document.save()
            return redirect('document_list')  # Redirect after upload
    else:
        form = DocumentUploadForm()
    return render(request, 'upload_document.html', {'form': form})


def document_list(request):
    documents = Document.objects.all().order_by('-upload_date')
    return render(request, 'document_list.html', {'documents': documents})