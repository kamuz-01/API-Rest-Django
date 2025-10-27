from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Filme, Avaliacao
from .serializers import FilmeSerializers, AvaliacaoSerializers
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins

"""
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
        if self.kwargs.get('filme_pk'):
            return self.queryset.filter(filme_id=self.kwargs.get('filme_pk'))
        return self.queryset.all()
    
class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializers
    
    def get_object(self):
        if self.kwargs.get('filme_pk'):
            return get_object_or_404(self.get_queryset(), filme_id=self.kwargs.get('filme_pk'), pk=self.kwargs.get('avaliacao_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))
    


"""
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
    
class AvaliacaoViewSet(viewsets.ModelViewSet):
    serializer_class = AvaliacaoSerializers
    
    def get_queryset(self):
        # Filtra as avaliações pelo filme_pk se fornecido na URL
        filme_pk = self.kwargs.get('filme_pk')
        if filme_pk is not None:
            return Avaliacao.objects.filter(filme_id=filme_pk)
        return Avaliacao.objects.all()
    
    def get_object(self):
        # Obtém um objeto específico de avaliação
        filme_pk = self.kwargs.get('filme_pk')
        avaliacao_pk = self.kwargs.get('pk')
        
        if filme_pk is not None:
            # Valida se o filme existe
            get_object_or_404(Filme, pk=filme_pk)
            # Retorna a avaliação específica do filme
            return get_object_or_404(Avaliacao, pk=avaliacao_pk, filme_id=filme_pk)
        
        return get_object_or_404(Avaliacao, pk=avaliacao_pk)