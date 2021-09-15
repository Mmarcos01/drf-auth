from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import AlbumSerializer
from .models import Album
from .permissions import IsOwnerOrReadOnly

class AlbumList(ListCreateAPIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class AlbumDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
