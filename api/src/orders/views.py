from rest_framework import status, generics
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models.models import Orders
from .serializer import OrdersSerializer


class OrdersListAPiView(generics.GenericAPIView):
    serializer_class = OrdersSerializer
    permission_classes = [AllowAny]
    queryset = Orders.objects.all()
    
    def get(self, request):
        serilizer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serilizer.data, status=status.HTTP_200_OK)


class OrdersretriveAPiView(generics.GenericAPIView):
    serializer_class = OrdersSerializer
    permission_classes = [AllowAny]
    queryset = Orders.objects.all()
    
    def get(self, request, pk=None):
        queryset = self.get_queryset().filter(id=pk)
        serilizer = self.serializer_class(queryset, many=True)
        return Response(serilizer.data, status=status.HTTP_200_OK)


class OrdersCreateApiView(generics.GenericAPIView):
    serializer_class = OrdersSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        order = request.data

        if request.user.customer.id == order['customer']:
            serilizer = self.serializer_class(data=order)
            serilizer.is_valid(raise_exception=True)
            serilizer.save()
            return Response(data=serilizer.data, status=status.HTTP_201_CREATED)
        else:
            return Response("you are not allowed to create orders for other customers",
            status=status.HTTP_401_UNAUTHORIZED)
