from django.db import models

# Create your models here.


class Projects(models.Model):
    title=models.CharField(max_length=255)
    description=models.CharField(max_length=400)
    link=models.URLField()
    created_at=models.DateTimeField()

    def __str__(self):
        return self.title
    

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()
    create_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"


class Skills(models.Model):
    name=models.CharField(max_length=20)
    percentage=models.IntegerField()
    image=models.TextField()

    def __str__(self):
        return f"{self.name}"