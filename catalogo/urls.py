from django.urls import path
from .views import (
    FilmeAPIView, 
    AvaliacaoAPIView, 
    FilmesAPIView, 
    AvaliacoesAPIView, 
    FilmeViewSet, 
    AvaliacaoViewSet
)
from rest_framework_nested import routers

# API V1 - usando views genéricas
urlpatterns_v1 = [
    path('filmes/', FilmesAPIView.as_view(), name='filmes'),
    path('filmes/<int:pk>/', FilmeAPIView.as_view(), name='filme'),
    path('filmes/<int:filme_pk>/avaliacoes/', AvaliacoesAPIView.as_view(), name='filmes_avaliacoes'),
    path('filmes/<int:filme_pk>/avaliacoes/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='filme_avaliacao'),
    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
    path('avaliacoes/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='avaliacao'),
]

# API V2 - usando routers e viewsets
router = routers.SimpleRouter()
router.register('filmes', FilmeViewSet, basename='filme')
router.register('avaliacoes', AvaliacaoViewSet, basename='avaliacao')

# Router aninhado para avaliacoes dentro de filmes
filmes_router = routers.NestedSimpleRouter(router, 'filmes', lookup='filme')
filmes_router.register('avaliacoes', AvaliacaoViewSet, basename='filme-avaliacao')

urlpatterns = urlpatterns_v1 + router.urls + filmes_router.urls