from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
class Tree(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True)

    def __str__(self):
        return str(self.name) + " -> " + str(self.user.username)

    def adminName(self):
        return str(self.name) + " -> " + str(self.user.username)

# class Skill(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.CharField(max_length=500)
#     parent = models.ForeignKey('self', on_delete=models.CASCADE, default=None, blank=True, null=True)
#     checked = models.BooleanField(default=False)
#     bronzeCost = models.IntegerField(default=None, blank=True, null=True)
#     silverCost = models.IntegerField(default=None, blank=True, null=True)
#     goldCost = models.IntegerField(default=None, blank=True, null=True)
#     platinumCost = models.IntegerField(default=None, blank=True, null=True)
#     tree = models.ForeignKey(Tree, on_delete=models.CASCADE, default=None, blank=True)

#     def __str__(self):
#         return str(self.name)

class mSkill(MPTTModel):
    tree_field = models.ForeignKey(Tree, on_delete=models.CASCADE, default="", null=True)
    name = models.CharField(max_length=50)
    description = models.CharField(default="", max_length=500)
    checked = models.BooleanField(default=False)
    bronzeCost = models.IntegerField(default=None, blank=True, null=True)
    silverCost = models.IntegerField(default=None, blank=True, null=True)
    goldCost = models.IntegerField(default=None, blank=True, null=True)
    platinumCost = models.IntegerField(default=None, blank=True, null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return str(self.name)

    class MPTTMeta:
        order_by_insertion = ['name']