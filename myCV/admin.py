from django.contrib import admin
from myCV.models import *

# Register your models here.


@admin.register(GeneralSettings)
class GeneralSettingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'parameter', 'updated_date', 'created_date']
    list_filter = ['name', 'description', 'parameter']
    list_editable = ['description', 'parameter']

    class Meta:
        model = GeneralSettings

@admin.register(ImageSettings)
class ImageSettingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'file', 'updated_date', 'created_date']
    list_filter = ['name', 'description', 'file']
    list_editable = ['description', 'file']

    class Meta:
        model = ImageSettings

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'name', 'percentage', 'updated_date', 'created_date']
    list_filter = ['name']
    list_editable = ['order', 'name', 'percentage']

    class Meta:
        model = Skill

@admin.register(SecondSkill)
class SecondSkillAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'name', 'percentage', 'updated_date', 'created_date']
    list_filter = ['name']
    list_editable = ['order', 'name', 'percentage']

    class Meta:
        model = SecondSkill

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'parameter', 'updated_date', 'created_date']
    list_filter = ['name', 'description', 'parameter']
    list_editable = ['description', 'parameter']

    class Meta:
        model = Experience

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['id', 'department', 'start_year', 'end_year', 'faculty', 'school_location', 'education_description', 'updated_date', 'created_date']
    list_filter = ['department', 'start_year', 'end_year', 'faculty', 'school_location', 'education_description']
    list_editable = ['department', 'start_year', 'end_year', 'faculty', 'school_location', 'education_description']

    class Meta:
        model = Education

@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'link', 'icon', 'updated_date', 'created_date']
    list_filter = ['link', 'icon']
    list_editable = ['order', 'link', 'icon']

    class Meta:
        model = SocialMedia

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'slug', 'button_text', 'file', 'updated_date', 'created_date']
    list_filter = ['slug', 'button_text']
    list_editable = ['order', 'slug', 'button_text', 'file']

    class Meta:
        model = Document
