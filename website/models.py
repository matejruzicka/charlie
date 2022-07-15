import uuid

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

