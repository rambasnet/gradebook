from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='default'),
    url(r'^index/$', views.index, name='index'),
    url(r'^home/$', views.index, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^grade/([0-9]*)', views.saveGrade, name='grade'),
    url(r'^grades/$', views.showGrades, name='grades'),
    url(r'delete/(?P<student_id>[0-9]+)/$', views.deleteGrade, name='delete'),
]