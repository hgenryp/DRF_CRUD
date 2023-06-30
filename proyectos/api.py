from proyectos.models import Proyecto
from rest_framework import viewsets,permissions
from .serializers import ProyectoSerializer

class ProyectoViewset(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProyectoSerializer
