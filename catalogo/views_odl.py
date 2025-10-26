from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Filme, Avaliacao
from .serializers import FilmeSerializers, AvaliacaoSerializers
from rest_framework import status

# Create your views here.
class FilmeAPIView(APIView):
    """
    API de avaliação de filmes
    """
    def get(self, request):
        filmes = Filme.objects.all()
        serializer = FilmeSerializers(filmes, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = FilmeSerializers(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    
class AvaliacaoAPIView(APIView):
    """
    API de avaliação de filmes
    """
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializers(avaliacoes, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = AvaliacaoSerializers(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)