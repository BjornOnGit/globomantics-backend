from django.urls import path

from .views import InquiryList, InquiryDetail

urlpatterns = [
    path('', InquiryList.as_view(), name='inquiry_list'),
    path('<int:pk>/', InquiryDetail.as_view(), name='inquiry_detail'),
]