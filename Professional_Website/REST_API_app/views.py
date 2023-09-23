from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from .serializers import PaymentSerializer,ScheduleSerializer,BloggerSerializer,BlogsSerializer


@api_view(['GET','POST','DELETE','PUT'])
def defaultRoutes(request):
    routes = [
        {
        'Endpoint':'/notes/',
        'method':'GET',
        'body':None,
        'description':'Returns an array of notes'
    },
    {
        'Endpoint':'/notes/id',
        'method':'GET',
        'body':None,
        'description':'Returns a single note'
    },
    ]
    return Response(routes)





# @api_view(['GET'])
# def getPayment(request,pk):
#     payment = Payments.objects.get(id=pk)
#     serializer = PaymentSerializer(payment,many=False)
#     return Response(serializer.data)

# @api_view(['PUT'])
# def putPayment(request,pk):
#     # data=request.data
#     payment = Payments.objects.get(id=pk)
#     serializer = PaymentSerializer(payment,data=request.data )
#     if serializer.is_valid():
#         serializer.save()
#     return Response(request.data)


# @api_view(['POST'])
# def createPayment(request):
#     data = request.data
#     payment = Payments.objects.create(body=data['body'])
#     serializer = PaymentSerializer(payment,many=False)
#     return Response(serializer.data)
    