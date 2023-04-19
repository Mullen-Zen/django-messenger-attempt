from django.utils import timezone
from tokenize import String
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.username
    def is_new_user(self):
        return self.created_at >= timezone.now() - timezone.timedelta(days=1)

class Message(models.Model):
    content = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="send_messages")
    conversation = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")
    created_at = models.DateTimeField(auto_now_add=True)

class Conversation(models.Model):
    name = models.CharField(max_length=100)
    participants = models.ManyToManyField(
      User,
      through="UserConversation",
      through_fields=("conversation", "user"),
      related_name="conversations",
    )

class UserConversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)