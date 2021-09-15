from rest_framework import generics
from .serializers import AlbumSerializer
from .models import Album
# from .permissions import IsOwnerOrReadOnly

class AlbumList(generics.ListCreateAPIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
