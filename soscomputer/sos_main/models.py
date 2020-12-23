from django.db import models

# Create your models here.

class Order(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    description = models.CharField(max_length=250)
    online = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заявки'
        verbose_name_plural = 'Заявки'