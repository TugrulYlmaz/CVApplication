from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.


class AbstractModel(models.Model):
    updated_date = models.DateTimeField(
        blank=True,
        auto_now=True,
        verbose_name='Updated Date',
        help_text='',
    )
    created_date = models.DateTimeField(
        blank=True,
        auto_now_add=True,
        verbose_name='Created Date',
        help_text='',
    )

    class Meta:
        abstract = True


class GeneralSettings(AbstractModel):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',
        help_text='This is variable of the setting.',
    )
    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Description',
        help_text='',
    )
    parameter = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Parameter',
        help_text='',
    )

    def __str__(self):
        return f'General Setting: {self.name}'

    class Meta:
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Settings'
        ordering = ('name',)


class ImageSettings(AbstractModel):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',
        help_text='This is variable of the setting.',
    )
    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Description',
        help_text='',
    )
    file = models.FileField(
        default='',
        verbose_name='Image',
        help_text='',
        blank=True,
        upload_to='Images/',
    )

    def __str__(self):
        return f'Image Setting : {self.name}'

    class Meta:
        verbose_name = 'Image Setting'
        verbose_name_plural = 'Image Settings'
        ordering = ('name',)


class Skill(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Order',
    )
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',
        help_text='This is variable of the setting.',
    )
    percentage = models.IntegerField(
        default=50,
        verbose_name='Percentage',
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )

    def __str__(self):
        return f'Skill : {self.name}'

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        ordering = ('id',)


class SecondSkill(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Order',
    )
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',
        help_text='This is variable of the setting.',
    )
    percentage = models.IntegerField(
        default=50,
        verbose_name='Percentage',
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )

    def __str__(self):
        return f'SecondSkill : {self.name}'

    class Meta:
        verbose_name = 'SecondSkill'
        verbose_name_plural = 'SecondSkills'
        ordering = ('id',)


class Experience(AbstractModel):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',
        help_text='This is variable of the setting.',
    )

    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Description',
        help_text='',
    )

    parameter = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Parameter',
        help_text='',
    )

    def __str__(self):
        return f'Experiences : {self.name}'

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'
        ordering = ('id',)


class Education(AbstractModel):
    department = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Department',
    )
    start_year = models.IntegerField(
        verbose_name='Start Year',
    )
    end_year = models.IntegerField(
        default=None,
        null=True,
        blank=True,
        verbose_name='End Year',
    )
    faculty = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Faculty',
    )
    school_location = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='School Location',
    )
    education_description = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Education Description',
    )

    def __str__(self):
        return f'Education : {self.department}'

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Education'
        ordering = ('id',)


class SocialMedia(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Order',
    )
    link = models.URLField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Link',
    )
    icon = models.CharField(
        name='',
        max_length=254,
        blank=True,
        verbose_name='Icon',
    )

    def __str__(self):
        return f'Social Media : {self.link}'

    class Meta:
        verbose_name = 'Social Media'
        verbose_name_plural = 'Social Media'
        ordering = ('order',)

class Document(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Order',
    )
    slug = models.SlugField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Slug',
        help_text='',
    )
    button_text = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Button Text',
        help_text='',
    )
    file = models.FileField(
        default='',
        verbose_name='File',
        help_text='',
        blank=True,
        upload_to='documents/',
    )
    def __str__(self):
        return f'Document : {self.slug}'

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'
        ordering = ('order',)
