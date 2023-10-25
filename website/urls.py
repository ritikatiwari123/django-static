from website.views import *
from django.urls

urlpatterns = [
                path('about/', AboutPageView.as_view(), name="about-page"),]