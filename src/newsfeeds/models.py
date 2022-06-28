from django.db import models

# Create your models here.

class Post(models.Model):
    # date_post = models.DateTimeField(auto_now_add=True)
    fname = models.CharField("First Name", max_length=200)
    lname = models.CharField("Last Name", max_length=200)
    oname = models.CharField("Other Name", max_length=200, blank=True)
    planguage = models.CharField("Language", max_length=50)
    university = models.CharField("university", max_length=100, blank=True)
    # edu_stat = models.ForeignKey()
    more = models.TextField('More About You', blank=True)
    resume = models.URLField("CV link", blank=True)
    mail = models.EmailField("Email Address", blank=True)



    def __str__(self):
        return self.fname + ' ' + self.lname
