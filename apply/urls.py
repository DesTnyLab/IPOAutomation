
#apply/urls.py

from django.urls import path
from . import views
urlpatterns = [
    
    path('home/', views.home, name='home'),
    path('applicable-shares/', views.view_applicable_shares, name='applicable-shares'),
    path('fetch-shares/', views.auto_applicable_shares, name='fetch-shares'),
    path('<int:share_id>/', views.apply_share, name='apply-share'),
    path('check-status/<int:user_id>/<int:share_id>/', views.check_status, name="check_status"),


]


