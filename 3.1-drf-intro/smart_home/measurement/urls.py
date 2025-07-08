from django.urls import path
from measurement.views import CreateSensor, ChangesSensor, AddMeasurements, ListSensor

urlpatterns = [
    path('create_sensor/', CreateSensor.as_view()),
    path('changes_sensor/<pk>/', ChangesSensor.as_view()),
    path('add_measurements/', AddMeasurements.as_view()),
    path('list_sensor/', ListSensor.as_view()),
]
