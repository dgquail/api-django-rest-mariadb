"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin # type: ignore
from django.urls import include, path # type: ignore
from rest_framework import routers

from myapi.views import (
    ConfigListCreateView, ConfigDetailView,
    LanguageListCreateView, LanguageDetailView,
    SourceListCreateView, SourceDetailView, SourceViewSet, 
    SpeakerListCreateView, SpeakerDetailView,
    SpeechListCreateView, SpeechDetailView, 
    UserViewSet,GroupViewSet
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'sources', SourceViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('config/', ConfigListCreateView.as_view(), name='config-list-create'),
    path('config/<int:pk>/', ConfigDetailView.as_view(), name='config-detail'),
    path('languages/', LanguageListCreateView.as_view(), name='language-list-create'),
    path('Languages/<int:pk>/', LanguageDetailView.as_view(), name='language-detail'),
    path('sources/', SourceListCreateView.as_view(), name='source-list-create'),
    path('sources/<int:pk>/', SourceDetailView.as_view(), name='source-detail'),
    path('speakers/', SpeakerListCreateView.as_view(), name='speaker-list-create'),
    path('speakers/<int:pk>/', SpeakerDetailView.as_view(), name='speaker-detail'),
    path('speeches/', SpeechListCreateView.as_view(), name='speech-list-create'),
    path('speeches/<int:pk>/', SpeechDetailView.as_view(), name='speech-detail'),
]
