from django.db import models


class Home(models.Model):
    """
    Home model
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Return a string representation of the model
        """
        return self.title
