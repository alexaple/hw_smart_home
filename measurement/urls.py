from django.urls import path
from measurement.views import ListCreateSensorView, CreateMeasurementView, RetrieveUpdateSensorView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', ListCreateSensorView.as_view()),
    path('measurements/', CreateMeasurementView.as_view()),
    path('sensors/<pk>/', RetrieveUpdateSensorView.as_view())
]
