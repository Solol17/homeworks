from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView, ListAPIView
from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


class CreateSensor(CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class ChangesSensor(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class AddMeasurements(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

class ListSensor(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer