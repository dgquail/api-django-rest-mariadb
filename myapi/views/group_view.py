from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import Group
from rest_framework import permissions, viewsets

from ..serializers import GroupSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]