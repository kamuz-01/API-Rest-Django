from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Filme, Avaliacao
from .serializers import FilmeSerializers, AvaliacaoSerializers
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins

""""
API v1
"""

class FilmesAPIView(generics.ListCreateAPIView):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializers
    

class FilmeAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializers
    
    
class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializers
    
    def get_queryset(self):
        if self.kwargs.get('fime_pk'):
            return self.get_queryset.filter(filme_id=self.kwargs.get('filme_pk'))
        return self.queryset.all()
    
class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializers
    
    def get_object(self):
        if self.kwargs.get('filme_pk'):
            return get_object_or_404(self.get_queryset(), filme_id=self.kwargs.get('filme_pk'), pk=self.kwargs.get('avaliacao_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))
    


""""
API v2
"""

class FilmeViewSet(viewsets.ModelViewSet):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializers
    
    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        filme = self.get_object()
        serializer = AvaliacaoSerializers(filme.avaliacoes.all(), many=True)
        return Response(serializer.data)
    
class AvaliacaoViewSet(mixins.ListModelMixin, 
                       mixins.CreateModelMixin, 
                       mixins.RetrieveModelMixin, 
                       mixins.UpdateModelMixin, 
                       mixins.DestroyModelMixin, 
                       viewsets.GenericViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializers