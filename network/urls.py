"""network URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from allauth.account import views as allauth_views
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path(
        'accounts/password/change/',
        login_required(
            allauth_views.PasswordChangeView.as_view(
                success_url=reverse_lazy('post-list')
            )
        ),
        name='account_change_password'
    ),
    path('accounts/', include('allauth.urls')),
    path('titbit/', include('titbit.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'network.views.handler404'
handler500 = 'network.views.handler500'
handler403 = 'network.views.handler403'
handler405 = 'network.views.handler405'
