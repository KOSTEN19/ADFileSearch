"""mindmap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from website import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),
    #path('login/',views.login_page, name = "login"),
    #path('logout/',views.logout_page, name = "logout"),
    #path('registration/',views.registraion_page, name = "registration"),
    path('', views.main_page, name = 'main'),
    path('add_document/',views.add_document),
    path('add_folder/',views.add_folder),
    path('search/',views.search),
    path('<int:year>', views.year_folder),
     path('<int:year>/<str:name_file>', views.one_file),
    path('catalogs/', views.catalogs),
    path('open_file/', views.open_file)
]+ static(settings.DOCUMENT_URL, document_root=settings.DOCUMENT_ROOT)
