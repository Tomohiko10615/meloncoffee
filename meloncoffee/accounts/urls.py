# accounts/urls.py
from django.urls import path
from .views import Sample, SignUpView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('sample/', Sample.as_view(), name='sample'),
]