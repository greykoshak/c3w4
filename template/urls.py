from django.conf.urls import url

from template.views import echo, filters, extend
from db.views import db_view

urlpatterns = [
    url(r'^echo/$', echo),
    url(r'^filters/$', filters),
    url(r'^extend/$', extend),
    url(r'^db_view/$', db_view),
]
