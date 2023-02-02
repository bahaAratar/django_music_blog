from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name

class Music(models.Model):
    title = models.CharField(max_length=50)
    duration = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='misics'
    )

    def __str__(self) -> str:
        return f'{self.title}  {self.duration}'

    