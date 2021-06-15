from django.conf.urls import url

from docs_management import views


urlpatterns = [
<<<<<<< HEAD
    url(r'admin_list/(\d+)/update-status',views.update_status_view,name='update_status'),
    url(r'list/digitized/(\d+)', views.digitized_doc_details, name='list_digitized_docs'),
    url(r'upload-doc', views.upload_doc, name='upload_doc'),
    url(r'user_list', views.list_uploaded_docs, name='user_list_docs'),
    url(r'admin_list', views.admin_docs, name='admin_list_docs'),
=======
    url(r'list/(\d+)/update-status',
        views.update_status_view,
        name='update_status'),
    url(r'list/digitized/(\d+)', views.digitized_doc_details, name='list_digitized_docs'),
    url(r'upload-doc', views.upload_doc, name='upload_doc'),
    url(r'list', views.list_uploaded_docs, name='list_docs'),
>>>>>>> b9324282d30826def492d35ce0aacc869987190a

    # API Views
    url(r'api/v1/list',
        views.UploadedDocListGenerics.as_view(),
        name='api_list_docs')
]
