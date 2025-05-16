from django.db import models

class Reminder(models.Model):
    METHOD_CHOICES = [
        ('SMS', 'SMS'),
        ('Email', 'Email'),
    ]

    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()
    method = models.CharField(max_length=10, choices=METHOD_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.method} reminder on {self.date} at {self.time}"
