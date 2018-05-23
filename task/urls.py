from django.conf.urls import url
from task.views import index,registerNotification,success
urlpatterns=[
    url("^$",index,name='index'),
    url("^register$",registerNotification,name='registerNotification'),
    url("^success$",success,name='success'),
]
import task.jobs