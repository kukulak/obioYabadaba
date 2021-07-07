import random
import os
from django.db import models
from django.db.models import Q
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.db.models.signals import pre_save, post_save
from django.urls import reverse

from ecom.utils import unique_slug_generator

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name,ext

def upload_image_path(instance, filename):
    #print(instance)
    # print(filename)
    new_filename = random.randint(1,3954605869)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(
            new_filename=new_filename,
            final_filename=final_filename
            )

# Create your models here.
class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True, active=True)

    def search(self, query):

        lookups = (Q(title__icontains=query) |
                  Q(description__icontains=query) |
                  Q(price__icontains=query) |
                  Q(tag__title__icontains=query)
                  )
        # Q(tag__name__iconatains=query)
        return self.filter(lookups).distinct()

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def featured(self):         #Products.objects.featured()
        return self.get_queryset().featured()


    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)    #Product.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):
        lookups = Q(title__icontains=query) | Q(description__icontains=query)
        return self.get_queryset().active().search(query)






class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    def __str__(self):
        return self.nombre 

class SubCategoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre         

class Caracteristica(models.Model):
    caracteristica = models.CharField(max_length=100)   

    def __str__(self):
        return self.caracteristica  

class Presentacion(models.Model):
    presentacion = models.CharField(max_length=100)
    
    def __str__(self):
        return self.presentacion 


class Product(models.Model):
    title            = models.CharField(max_length=120)        #max length of the title
    slug             = models.SlugField(blank=True, unique=True)
    categoria        = ForeignKey(Categoria, on_delete=models.CASCADE)
    subcategoria     = ForeignKey(SubCategoria, on_delete=models.CASCADE)
    caracteristicas  = ForeignKey(Caracteristica, on_delete=models.CASCADE)
    smallDescription = models.TextField(max_length=200)
    description      = models.TextField(null=True)             #null=True means it can be empty
    presentaciones   = ForeignKey(Presentacion, on_delete=models.CASCADE)
    price            = models.DecimalField(decimal_places=2, max_digits=20, default=0.00)
    image            = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    featured         = models.BooleanField(default=False)
    active           = models.BooleanField(default=True)
    timestamp        = models.DateTimeField(auto_now_add=True)

    objects          = ProductManager()

    def get_absolute_url(self):
        # return "/products/{slug}/".format(slug=self.slug)
        return reverse("products:detail", kwargs={"slug": self.slug})

    def __str__(self):          #for python 3 it's just representation and just a method which overide
        return self.title
      # def __unicode__(self):    #for python 2
      #     return self.title

    @property
    def name(self):
        return self.title


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)

class CategoriaCultura(models.Model):
    title           = models.CharField(max_length=120)
    slug            = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.title

class EntradasCultura(models.Model):
    title           = models.CharField(max_length=120)
    slug            = models.SlugField(blank=True, unique=True)
    categoria       = ForeignKey(CategoriaCultura, on_delete=models.CASCADE)
    image           = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    video           = models.URLField(max_length=1500, null=True, blank=True)
    description     = models.TextField(null=True) 

    def __str__(self):
        return self.title
