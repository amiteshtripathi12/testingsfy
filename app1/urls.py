from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('',views.index,name='index'),
    path('about_us',views.about_us, name='about_us'),
    path('blog', views.blog,name='blog'),
    path('contact_us',views.contact_us, name='contact_us'),
    path('gallery', views.gallery,name='gallery'),
    path('service', views.service,name='service'),
    path('appointment', views.appointment,name='appointment'),
    path('login', views.login,name='login'),
    path('plans', views.plans,name='plans'),
    path('payment', views.payment,name='payment'),
    path('zoom', views.zoom,name='zoom'),
    path('registration', views.registration,name='registration'),
    path('login1', views.login1,name='login1'),
    path('gender', views.gender,name='gender'),
    path('doc_index', views.doc_index,name='doc_index'),
    path('doc_appointment', views.doc_appointment,name='doc_appointment'),
    path('doc_edit_appointment', views.doc_edit_appointment,name='doc_edit_appointment'),
    path('doc_patients', views.doc_patients,name='doc_patients'),
    path('doctor_payment', views.doctor_payment,name='doctor_payment'),
    path('doctor_login', views.doctor_login,name='doctor_login'),

##+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



