import uuid

from io import BytesIO
import sys
from PIL import Image, ImageOps
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models

from website.templatetags.filters import board_title_filter


class BoardMember(models.Model):
    TITLE_CHOICES = [
        ("Prezident", "Prezident"),
        ("Víceprezident", "Víceprezident"),
        ("Tajemník", "Tajemník"),
        ("Pokladník", "Pokladník"),
        ("Řadový člen", "Řadový člen"),
        ("Člen revizní komise", "Člen revizní komise")
    ]

    PRONOUNS = [
        ("Mužské", "Mužské"),
        ("Ženské", "Ženské")
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=225, blank=False, null=False, verbose_name="Jméno a příjmení")
    title = models.CharField(max_length=225, choices=TITLE_CHOICES, blank=False, null=False, verbose_name="Pozice")
    pronouns = models.CharField(max_length=225, choices=PRONOUNS, blank=False, null=False, verbose_name="Oslovení")
    medallion = models.TextField(blank=True, null=True, verbose_name="Medailon")
    photo = models.ImageField(blank=True, null=True, upload_to="charlie/static", verbose_name="Fotka")
    email = models.EmailField(blank=True, null=True, verbose_name="Email")
    email2 = models.EmailField(blank=True, null=True, verbose_name="Druhý email")

    def __str__(self):
        title = board_title_filter(self)
        return f"{self.name} | {title.lower()}"


class File(models.Model):
    FILE_TYPES = [
        ("pdf", "pdf"),
        ("doc", "doc"),
        ("docx", "docx"),
        ("jpg", "jpg"),
        ("jpeg", "jpeg"),
        ("png", "png"),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=225, blank=False, null=False, verbose_name="Název")
    description = models.TextField(blank=True, null=True, verbose_name="Popis")
    slug = models.CharField(max_length=255, default=str(uuid.uuid4()), unique=True)
    file_type = models.CharField(max_length=225, choices=FILE_TYPES, blank=False, null=False, verbose_name="Typ souboru")
    file = models.FileField(blank=False, null=False, upload_to="charlie/static", verbose_name="Soubor")

    def __str__(self):
        return self.name


class Photo(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=225, blank=True, null=True, verbose_name="Popisek")
    photo = models.ImageField(blank=True, null=True, upload_to="charlie/static", verbose_name="Fotka")

    def __str__(self):
        return self.description

    def save(self):
        im = Image.open(self.photo)
        im = ImageOps.exif_transpose(im)
        output = BytesIO()
        im.save(output, format='JPEG', optimize=True, quality=30)
        output.seek(0)
        self.photo = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.photo.name.split('.')[0], 'image/jpeg',
                                          sys.getsizeof(output), None)
        super(Photo, self).save()


class University(models.Model):
    class Meta:
        verbose_name_plural = "universities"

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=225, blank=True, null=True, verbose_name="Název")

    def __str__(self):
        return self.name


class Faculty(models.Model):
    class Meta:
        verbose_name_plural = "faculties"

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=225, blank=True, null=True, verbose_name="Název")

    def __str__(self):
        return self.name


class Member(models.Model):
    MEMBERSHIP_TYPE = [
        ("Roční", "Roční"),
        ("Doživotní", "Doživotní"),
        # ("Ukončené", "Ukončené"),
    ]

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=225, verbose_name="Jméno")
    last_name = models.CharField(max_length=225, verbose_name="Příjmení")
    email = models.EmailField(blank=True, null=True, verbose_name="Email")
    phone = models.CharField(max_length=225, blank=True, null=True, verbose_name="Telefon")
    university = models.ManyToManyField(University, blank=True, verbose_name="Univerzita")
    faculty = models.ManyToManyField(Faculty, blank=True, verbose_name="Fakulta")
    photos_allowed = models.BooleanField(verbose_name="Souhlas s focením")
    membership_type = models.CharField(max_length=225, choices=MEMBERSHIP_TYPE, verbose_name="Typ členství")
    paid_membership = models.BooleanField(verbose_name="Poplatek zaplacen")
    member_since = models.DateField(blank=True, null=True, verbose_name="Členem od")
    member_until = models.DateField(blank=True, null=True, verbose_name="Členem do")
    membership_last_prolonged = models.DateField(blank=True, null=True,
                                                 verbose_name="Členství naposledy prodlouženo dne")
    lifetime_since = models.DateField(blank=True, null=True, verbose_name="Doživotní členství od")
    approved = models.BooleanField(verbose_name="Schváleno")
    found_application = models.BooleanField(verbose_name="Papírová přihláška existuje")
    ending_membership = models.BooleanField(verbose_name="Končící členství")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
