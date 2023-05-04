from django.shortcuts import render
from . models import jadwalimsak
from . seriallizers import jadwalimsakSerializer

#rest_framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def readjadwalimsak(request):
    jadwal = jadwalimsak.objects.all()
    serializer = jadwalimsakSerializer(jadwal, many=True )
    return Response(serializer.data)
@api_view(['GET'])
def detailjadwalimsak(request, id):
    jadwal = jadwalimsak.objects.get(pk=id)
    serializer = jadwalimsakSerializer(jadwal, many=False )
    return Response(serializer.data)
@api_view(['POST'])
def createjadwalimsak(request):
    jadwal = jadwalimsak.objects.all()
    serializer = jadwalimsakSerializer(data=request.data )
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['PUT'])
def updatejadwalimsak(request, id):
    jadwal = jadwalimsak.objects.get(pk=id)
    serializer = jadwalimsakSerializer(instance=jadwal, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['DELETE'])
def deletejadwalimsak(request, id):
    jadwal = jadwalimsak.objects.get(pk=id)
    jadwal.delete()
    return Response('data di hapus', status=204)
# Create your views here.
