from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from PIL import Image

class Blog(models.Model):
    titulo = models.CharField(max_length=25)
    subtitulo = models.CharField(max_length=25)
    cuerpo = models.CharField(max_length=1000)
    autor = models.CharField(max_length=20)
    img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)





