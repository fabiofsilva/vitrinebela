from rest_framework.generics import (ListAPIView,
                                     RetrieveAPIView,
                                     DestroyAPIView,
                                     UpdateAPIView,
                                     CreateAPIView)

from vitrinebela.bookings.models import Booking
from .serializers import (BookingListSerializer,
                          BookingDetailSerializer,
                          BookingCreateUpdateSerializer)


class PostCreateAPIView(CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingCreateUpdateSerializer

class PostDetailAPIView(RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingDetailSerializer
    # lookup_field = 'user'


class PostUpdateAPIView(UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingCreateUpdateSerializer
    lookup_field = 'pk'


class PostDeleteAPIView(DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingDetailSerializer
    lookup_field = 'pk'


class PostListAPIView(ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingListSerializer


# def eliminaEventos(request):
#     output = {}
#     record_id = request.POST.get("id", "")
#     if(record_id is not None and record_id != ''):
#         event_id = Evento.objects.get(evento_id=record_id)
#         event_id.delete()
#         output['id'] = record_id
#     return HttpResponse(record_id)