from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model) :
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self) :
        return self.title + "\n" + self.description
    
class Reply(models.Model) :
    replyTo = models.ForeignKey(Post, related_name="replies", on_delete = models.CASCADE)
    commentAuthor = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self) :
        return self.content

class userFollowing(models.Model) :
    userId = models.ForeignKey(User, null=True, blank=True, related_name="following", on_delete = models.CASCADE)
    followUserId = models.ForeignKey(User, null=True, blank=True, related_name="followers", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta :
        constraints = [
            models.UniqueConstraint('userId', 'followUserId', name="followChecker"),
        ]

    def __str__(self) :
        return self.userId + " " + self.followUserId