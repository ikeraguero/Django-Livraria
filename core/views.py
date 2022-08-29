from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet
## from rest_framework.permissions import isAuthenticated

from core.models import Categoria, Editora, Autor, Livro
from core.serializer import CategoriaSerializer, EditoraSerializer, AutorSerializer, LivroDetailSerializer, LivroSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
##    permission_classes = [isAuthenticated]

class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer

class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return LivroDetailSerializer
        return LivroSerializer