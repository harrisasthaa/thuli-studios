from django.db import models

class UserRequest(models.Model):
    user_id = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='uploads/')
    preferences = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request {self.id} - {self.user_id}"

class Dress(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField(max_length=200)

    def __str__(self):
        return self.name

class Recommendation(models.Model):
    user_request = models.ForeignKey(UserRequest, on_delete=models.CASCADE)
    recommended_dress = models.ForeignKey(Dress, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Recommendation for {self.user_request.id}"
