from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({"cpf": "CPF inválido."})

        if not nome_valido(data['nome']):
            raise serializers.ValidationError({"nome": "O campo nome deve possuir apenas letras."})

        if not rg_valido(data['rg']):
            raise serializers.ValidationError({"rg": "O campo rg deve possuir 9 dígitos"})

        if not celular_valido(data['celular']):
            raise serializers.ValidationError({"celular": "O celular deve ter o seguinte modelo: 11 92345-6789"})

        return data
