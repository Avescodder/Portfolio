from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f'{self.id}.{self.name}'
    
class Watch(models.Model):
    title = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='images/watches/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}.{self.title}'



