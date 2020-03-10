from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tree(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True)

    def __str__(self):
        return str(self.name) + " -> " + str(self.user.username)

    def adminName(self):
        return str(self.name) + " -> " + str(self.user.username)

class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    tree = models.ForeignKey(Tree, on_delete=models.CASCADE, default=None, blank=True)
    checked = models.BooleanField(default=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, default=None, blank=True, null=True)

    def __str__(self):
        return str(self.name)