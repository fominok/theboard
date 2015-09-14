from django.db import models

# Create your models here.


class Thread(models.Model):
    name = models.TextField(max_length=30)

    def __str__(self):
        return "Thread: " + self.name


class Post(models.Model):
    post_text = models.TextField(max_length=10000)
    thread = models.ForeignKey(Thread)
    pub_date = models.DateTimeField('Date post')
    pic = models.ImageField(upload_to='pics', blank=True)

    def __str__(self):
        return "Post in " + self.thread.name + ": " + self.post_text[:10]
