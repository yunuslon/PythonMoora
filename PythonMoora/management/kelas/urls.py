
from django.conf.urls import url
from management.kelas import views

urlpatterns = [
    url (r'^$', views.ListKelasView.as_view(), name='view'),
    url (r'^matrix$', views.ListMatrixkelasView.as_view(), name='matrix'),
    url (r'^pembobotan$', views.ListPembobotankelasView.as_view(), name='pembobotan'),

]