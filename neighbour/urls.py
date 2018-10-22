from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^signup/',views.signup,name='signup'),
    url(r'^profile/',views.profile,name='profile'),
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
