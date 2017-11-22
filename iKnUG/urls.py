"""iKnUG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
admin.autodiscover()
from iKnUG.views import home, icons, charts, forms, tables, login, panels, widgets

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$|^index', home),
    url(r'^icon', icons),
    url(r'^chart', charts),
    url(r'^table', tables),
    url(r'^log', login),
    url(r'^form', forms),
    url(r'^widget', widgets),
    url(r'^panel', panels),
]
