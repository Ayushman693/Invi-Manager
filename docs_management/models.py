# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


from django.contrib.postgres.fields import ArrayField
# Create your models here.


class UploadedDoc(models.Model):
<<<<<<< HEAD
    UPLOADED = 1
    UNDER_REVIEW = 2
    DIGITIZED = 3
=======
    UPLOADED = 100
    UNDER_REVIEW = 200
    DIGITIZED = 300
>>>>>>> b9324282d30826def492d35ce0aacc869987190a

    CHOICES = (
        (UPLOADED, 'Uploaded'),
        (UNDER_REVIEW, 'UnderReview'),
        (DIGITIZED, 'Digitized')
    )

    uploaded_on = models.DateTimeField(default=timezone.now)
    storage_path = models.CharField(max_length=1000)
    status = models.IntegerField(
        choices=CHOICES,
        default=UPLOADED)

    @classmethod
    def create(cls, url):
        doc = UploadedDoc()
        doc.uploaded_on = timezone.now()
        doc.storage_path = url

        doc.save()

    def update_status(self, update_status):
        if update_status > self.status:
            self.status = update_status

    @property
    def next_status(self):
        if self.status < self.DIGITIZED:
<<<<<<< HEAD
            return self.status + 1
=======
            return self.status + 100
>>>>>>> b9324282d30826def492d35ce0aacc869987190a
        else:
            return self.DIGITIZED

    def __str__(self):
        return str(self.id) + " : " + str(self.status)


class InvoiceEntry(models.Model):
    item_name = models.CharField(max_length=400)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.item_name + " : qty " + str(self.quantity)


class ExtractedDoc(models.Model):
    uploaded_doc = models.OneToOneField(
        UploadedDoc,
        on_delete=models.CASCADE,
        primary_key=True)
    invoice_number = models.CharField(max_length=100, default="")
    summary = models.CharField(max_length=1000)

    def __str__(self):
        return "extraced doc : " + self.invoice_number
