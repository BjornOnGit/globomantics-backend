from rest_framework import generics

from .models import Inquiry
from .serializers import InquirySerializer

class InquiryList(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer

class InquiryDetail(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer

# Create your views here.
