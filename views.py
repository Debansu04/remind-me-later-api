from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ReminderSerializer
from .models import Reminder

@api_view(['POST'])
def create_reminder(request):
    serializer = ReminderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_reminders(request):
    reminders = Reminder.objects.all().order_by('-created_at')
    serializer = ReminderSerializer(reminders, many=True)
    return Response(serializer.data)
