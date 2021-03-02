from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status
from .serializers import CustomerSerializer
from .models import Customer
from api.src.authentication.models import User
from rest_framework.permissions import IsAuthenticated

class ProfileViewSet(ViewSet):
    
    permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
   

    def update(self, request, pk=None):

        if request.user.customer.id == pk:
            instance = request.user.customer
            instance.phone_no = request.data.get('phone_no',instance.phone_no)
            instance.country_code = request.data.get('country_code',instance.country_code)
            instance.save()
            return Response(CustomerSerializer(instance).data, status=status.HTTP_200_OK)
        else:
            return Response({"error":"You are not the owner or Does not exist"},
            status=status.HTTP_403_FORBIDDEN)


    def retrieve(self, request, pk=None):
        serializer = CustomerSerializer(self.queryset.filter(id=pk), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def list(self, request):
        serializer = CustomerSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
