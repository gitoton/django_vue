from django.db import models

class Categorys(models.Model):
    category = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.category

class Titles(models.Model):
    title = models.TextField(blank=False)
    category = models.ForeignKey(Categorys, on_delete=models.CASCADE, null=True,)
    showing = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
class Emotions(models.Model):
    emotion = models.TextField(blank=False)
    title = models.ForeignKey(Titles, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
 
    def __str__(self) -> str:
        return self.emotion

class Thinkings(models.Model):
    thinking = models.TextField(blank=False)
    title = models.ForeignKey(Titles, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.thinking
    
class Behaviors(models.Model):
    behavior = models.TextField(blank=False)
    title = models.ForeignKey(Titles, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.behavior
    
class Feelings(models.Model):
    feeling = models.TextField(blank=False)
    title = models.ForeignKey(Titles, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.feeling



