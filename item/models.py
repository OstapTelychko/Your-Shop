from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Categories(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=50, unique=True)


    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Categories"
    

    def __str__(self) -> str:
        return self.name



class Items(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    sold = models.BooleanField(default=False)
    image = models.ImageField(upload_to="items_images", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Categories, related_name="items", on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name="items", on_delete=models.CASCADE)
    views = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Items"
    

    def average_rating(self) -> float | int:
        return FeedBacks.objects.filter(item=self).aggregate(models.Avg("rating"))["rating__avg"]    

    def __str__(self) -> str:
        return f"{self.name}-{self.price}-{self.owner}"



class FeedBacks(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    content = models.TextField()
    item = models.ForeignKey(Items, related_name="feedbacks", on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name="feedbacks", on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "FeedBacks"
        ordering = ("rating",)

    def __str__(self) -> str:
        return f"{self.item}-{self.rating}-{self.owner}"


