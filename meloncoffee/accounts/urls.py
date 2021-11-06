# accounts/urls.py
from django.urls import path
from . import views
#from .views import Sample, SignUpView


urlpatterns = [
    #path('signup/', SignUpView.as_view(), name='signup'),
    #path('sample/', Sample.as_view(), name='sample'),
    path("signup/", views.signup, name="signup"),
]