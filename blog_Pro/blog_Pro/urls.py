"""blog_Pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog_app.views import (home_view,
							about_view,
							contact_view, 
							blog_list_view, 
							detail_view,)

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	url(r'^$', home_view, name='home'),
	url(r'^about/$', about_view, name='about'),
	url(r'^post/(?P<id>\d+)$', detail_view, name='detail'),
	url(r'^contact/$', contact_view, name='contact'),
	url(r'^blogs/$', blog_list_view, name='blogs'),
    url(r'^admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

