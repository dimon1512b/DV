from django.db import models


class Cars(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    version = models.CharField(default='', max_length=100)
    year = models.IntegerField()
    price_usd = models.IntegerField()
    price_uah = models.IntegerField()
    race = models.CharField(max_length=50)
    transmission = models.CharField(max_length=20)
    region = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    engine_type = models.CharField(max_length=20)
    engine_capacity = models.FloatField()
    plate_number = models.CharField(max_length=20)
    vin_code = models.CharField(max_length=50)
    type_of_transport = models.CharField(max_length=20)
    body_type = models.CharField(max_length=20)
    drive_type = models.CharField(max_length=20)
    description = models.TextField()
    date_created = models.DateTimeField()
    date_added_to_DB = models.DateTimeField(auto_now_add=True)
    photo_card = models.ImageField(null=True, blank=True)
    photo_view = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Cars"

    def __str__(self):
        return f'{self.brand} {self.model} {self.version} / {self.price_usd}$ / {self.date_created} / {self.id}'

    def serialize(self):
        return {
            'id': self.id,
            'brand': self.brand,
            'model': self.model,
            'version': self.version,
            'year': self.year,
            'price_usd': self.price_usd,
            'price_uah': self.price_uah,
            'race': self.race,
            'transmission': self.transmission,
            'region': self.region,
            'city': self.city,
            'engine_type': self.engine_type,
            'engine_capacity': self.engine_capacity,
            'plate_number': self.plate_number,
            'vin_code': self.vin_code,
            'type_of_transport': self.type_of_transport,
            'body_type': self.body_type,
            'description': self.description,
            # 'date_created': self.date_created,
            # 'date_added_to_DB': self.date_added_to_DB,
            'drive_type': self.drive_type,
            'photo_card': self.photo_card.url.replace('/https%3A/', 'https://'),
            'photo_view': self.photo_view.url.replace('/https%3A/', 'https://')
        }
