from django.shortcuts import render, redirect, get_object_or_404
from myCV.models import GeneralSettings, ImageSettings, Skill, SecondSkill, Experience, Education, SocialMedia, Document


# Create your views here.
def index(request):
    site_title = GeneralSettings.objects.get(name='site_title').parameter
    site_keywords = GeneralSettings.objects.get(name='site_keywords').parameter
    site_description = GeneralSettings.objects.get(name='site_description').parameter
    hero_name = GeneralSettings.objects.get(name='hero_name').parameter
    about_title = GeneralSettings.objects.get(name='about_title').parameter
    about_description = GeneralSettings.objects.get(name='about_description').parameter
    about_upper_description = GeneralSettings.objects.get(name='about_upper_description').parameter
    about_footer_description = GeneralSettings.objects.get(name='about_footer_description').parameter
    about_skills_description = GeneralSettings.objects.get(name='about_skills_description').parameter
    resume_description = GeneralSettings.objects.get(name='resume_description').parameter
    portfolio_description = GeneralSettings.objects.get(name='portfolio_description').parameter
    portfolio_description2 = GeneralSettings.objects.get(name='portfolio_description2').parameter
    contact_description = GeneralSettings.objects.get(name='contact_description').parameter

    # Images
    navbar_profile = ImageSettings.objects.get(name='navbar_profile').file

    # Skills
    skills = Skill.objects.all().order_by('id')
    skill = SecondSkill.objects.all().order_by('id')

    # Experience
    job_title = Experience.objects.get(name='job_title').parameter
    job_title_2 = Experience.objects.get(name='job_title_2').parameter
    start_date = Experience.objects.get(name='start_date').parameter
    start_date_2 = Experience.objects.get(name='start_date_2').parameter
    end_date = Experience.objects.get(name='end_date').parameter
    end_date_2 = Experience.objects.get(name='end_date_2').parameter
    company_name = Experience.objects.get(name='company_name').parameter
    company_name_2 = Experience.objects.get(name='company_name_2').parameter
    job_location = Experience.objects.get(name='job_location').parameter

    # Education
    educations = Education.objects.all().order_by('id')

    # Social Media
    social_medias = SocialMedia.objects.all()
    #Document
    documents = Document.objects.all()

    context = {
        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_description': site_description,
        'hero_name': hero_name,
        'about_title': about_title,
        'about_description': about_description,
        'about_upper_description': about_upper_description,
        'about_footer_description': about_footer_description,
        'about_skills_description': about_skills_description,
        'resume_description': resume_description,
        'portfolio_description': portfolio_description,
        'portfolio_description2' : portfolio_description2,
        'contact_description': contact_description,
        # Image
        'navbar_profile': navbar_profile,
        # Skills
        'skills': skills,
        'skill': skill,

        # Experience
        'job_title': job_title,
        'job_title_2': job_title_2,
        'start_date': start_date,
        'start_date_2': start_date_2,
        'end_date': end_date,
        'end_date_2': end_date_2,
        'company_name': company_name,
        'company_name_2': company_name_2,
        'job_location': job_location,
        # Education
        'educations': educations,

        # Social Media
        'social_medias': social_medias,

        #Document
        'documents': documents,
    }

    return render(request, 'index.html', context=context)


def contact(request):
    return render(request, 'contact.html')

def redirect_urls(request, slug):
    doc = get_object_or_404(Document, slug=slug)
    return redirect(doc.file.url)
