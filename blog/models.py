from django.db import models

# Create your models here.
class BlogPost(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=500)
    head0=models.CharField(max_length=500,default="")
    chead01=models.CharField(max_length=10000000,default="")
    chead02=models.CharField(max_length=10000000,default="")
    head1=models.CharField(max_length=500,default="")
    chead11=models.CharField(max_length=10000000,default="")
    chead12=models.CharField(max_length=10000000,default="")
    head2=models.CharField(max_length=500,default="")
    chead21=models.CharField(max_length=10000000,default="")
    chead22=models.CharField(max_length=10000000,default="")
    pub_date=models.DateField()
    thumbnail=models.ImageField(upload_to='shop/images',default="")

    def __str__(self):
        return self.title