

from django.conf.urls import url, include
from django.contrib import admin

from Invi_backend import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admins/', views.admin_home, name='admin_home'),
    url(r'^$', views.home, name='home'),
    url(r'^login/$', views.main_login, name='login'),
    url(r'^login_base/$', views.login_base, name='login_base'),
    url(r'^logout/$', views.main_logout, name='logout'),
    url(r'^docs/', include('docs_management.urls')),

    
]

from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
