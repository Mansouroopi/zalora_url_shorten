from django.db import models
from django.urls import reverse

# Import the helper used to create random codes
from .utils import create_shortened_url




class Shortener(models.Model):
    '''
    Url shortener model
    ''' 
    uuid = models.PositiveIntegerField(default=0)    
    long_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def get_absolute_url(self):
        return reverse('shortener-detail', args=[str(self.id)])


    class Meta:

        ordering = ["-created_at"]


    def __str__(self):
        return '%s, %s' % (self.short_url, self.created_at)

    def __repr__(self):
        return '<Shortener(long_url={}, short_url={}>'.format(self.long_url, self.short_url)

    def save(self, *args, **kwargs):

        # If the short url wasn't specified
        if not self.short_url:
            # We pass the model instance that is being saved
            self.short_url = create_shortened_url(self)

        super().save(*args, **kwargs)