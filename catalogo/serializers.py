from rest_framework import serializers
from .models import Filme, Avaliacao

class AvaliacaoSerializers(serializers.ModelSerializer):

    class  Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }

        model = Avaliacao

        fields = (
            'id',
            'filme',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        )

class FilmeSerializers(serializers.ModelSerializer):
    #Relacionamento Neste
    #avaliacoes = AvaliacaoSerializers(many=True, read_only=True)

    #HyperLinked related field
    #avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')
    
    #Prymary Key related field
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class  Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }

        model = Filme
        
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes'
        )