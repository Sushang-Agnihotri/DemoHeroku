from django.conf.urls import url
from .views import DemoAPIView

urlpatterns = [
    url(r'^demo',DemoAPIView.as_view())
]
