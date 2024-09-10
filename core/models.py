from django.db import models
from django.contrib.auth.models import User

class Document(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    uploaded_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    upload_date = models.DateTimeField(auto_now_add=True)
    anonymous = models.BooleanField(default=False)

    def __str__(self):
        return self.title
