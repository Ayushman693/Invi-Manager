# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from django.shortcuts import get_object_or_404

from .serializers import UploadedDocSerializer
from . import serializers


from docs_management import (models, forms)


def upload_doc(request):
    if request.method == 'POST' and request.FILES['doc']:
        doc_file = request.FILES['doc']
        fs = FileSystemStorage()
        filename = fs.save(doc_file.name, doc_file)
        uploaded_file_url = fs.url(filename)

        models.UploadedDoc.create(uploaded_file_url)
        return render(request, 'docs_management/upload_doc.html', {
            'uploaded_file_url': uploaded_file_url
        })

    return render(request, 'docs_management/upload_doc.html')

<<<<<<< HEAD
def admin_docs(request):
    docs = models.UploadedDoc.objects.all()

    kwargs = locals()
    return render(request, 'docs_management/admin_list_docs.html', kwargs)

=======
>>>>>>> b9324282d30826def492d35ce0aacc869987190a

def list_uploaded_docs(request):
    docs = models.UploadedDoc.objects.all()

    kwargs = locals()
<<<<<<< HEAD
    return render(request, 'docs_management/user_list_docs.html', kwargs)


=======
    return render(request, 'docs_management/list_docs.html', kwargs)
>>>>>>> b9324282d30826def492d35ce0aacc869987190a


def update_status_view(request, pk):
    if request.method == "POST":
        serializer = serializers.UpdateStatusSerializer(request.POST)
        doc = get_object_or_404(models.UploadedDoc, id=pk)
        doc.update_status(serializer.data["status"])
        doc.save()

<<<<<<< HEAD
        return redirect("admin_list_docs")
=======
        return redirect("list_docs")
>>>>>>> b9324282d30826def492d35ce0aacc869987190a


def digitized_doc_details(request, pk):

    doc = get_object_or_404(models.ExtractedDoc, uploaded_doc__id=pk)
    serializer = serializers.UpdateExtracedDocSerializer(doc)
    form = forms.ExtractedDocUpdateForm(serializer.data)

    if request.method == "POST":
        form = forms.ExtractedDocUpdateForm(request.POST)
        if form.is_valid():
            form.update_instance(doc)

    kwargs = locals()
    return render(request, 'docs_management/extracted_doc.html', kwargs)


class GenericCursorPagination(PageNumberPagination):
    page_size_query_param = 'per_page'

    def get_paginated_response(self, data):
        return JsonResponse({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'total': self.page.paginator.count,
            'count': self.get_page_size(self.request),
            'results': data,
        })


class UploadedDocListGenerics(generics.ListAPIView):
    """
    List all uploaded documents.
    """

    queryset = models.UploadedDoc.objects.all()
    serializer_class = UploadedDocSerializer
    pagination_class = GenericCursorPagination
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)

    def list(self, request):
        paginated_queryset = self.paginate_queryset(self.get_queryset())
        serializer = UploadedDocSerializer(paginated_queryset, many=True)

        return self.get_paginated_response(serializer.data)
