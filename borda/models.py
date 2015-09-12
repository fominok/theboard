from django.db import models

# Create your models here.


class Thread(models.Model):
    name = models.TextField(max_length=30)

    def __str__(self):
        return "Thread: " + self.name


class Post(models.Model):
    post_text = models.TextField(max_length=255)
    thread = models.ForeignKey(Thread)

    def __str__(self):
        return "Post in " + self.thread.name + ": " + self.post_text[:10]
