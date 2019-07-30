from django.db import models

# Create your models here.

class Data(models.Model):
    korean = '한식'
    chinese = '중식'
    japanese = '일식'
    american = '양식'
    dessert = '디저트'
    rest = '기타'
    category_choices = ((korean, '한식'), (chinese, '중식'), (japanese, '일식'), (american, '양식'), (dessert, '디저트'), (rest, '기타'))

    photo = models.ImageField(upload_to = 'images/')
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    specialaddress = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    menu = models.CharField(max_length=200)
    price = models.IntegerField()
    priceChar = models.CharField(max_length=200)
    comment = models.CharField(max_length=200)
    hashtag = models.CharField(max_length=200)
    category = models.CharField(max_length = 20, choices = category_choices)

    def __str__(self):
        return self.title