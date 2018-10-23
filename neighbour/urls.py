from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^signup/',views.signup,name='signup'),
    url(r'^biz/',views.create_business,name='biz'),
    url(r'^profile/',views.profile,name='profile'),
    url(r'^profiles/(\d+)',views.profiles,name='profiles'),
    url(r'^search',views.search_results,name='search_results'),
    url(r'^comment/(\d+)',views.comment,name='comment'),

]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
