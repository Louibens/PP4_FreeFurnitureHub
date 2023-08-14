from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from cloudinary.models import CloudinaryField

# Furniture model choices

FURNITURE_TYPES = (
    ("couch", "Couch"),
    ("armchair", "Armchair"),
    ("dining table", "Dining Table"),
    ("dining chair", "Dining Chair"),
    ("desk", "Desk"),
    ("bed", "Bed"),
    ("dresser", "Dresser"),
    ("locker", "Locker"),
    ("coffee table", "Coffee Table"),
    ("other", "Other"),
)

ROOMS = (
    ("kitchen", "Kitchen"),
    ("dining room", "Dining Room"),
    ("bedroom", "Bedroom"),
    ("study", "Study"),
    ("living room", "Living Room"),
    ("bathroom", "Bathroom"),
    ("baby", "Baby"),
    ("other", "Other"),
)

CONDITION = (
    ("as new", "As New"),
    ("damaged", "Damaged"),
    ("good condition, some damage", "Good Condition, Some Damage"),
)

COUNTIES = (
    ("antrim", "Antrim"),
    ("armagh", "Armagh"),
    ("carlow", "Carlow"),
    ("cavan", "Cavan"),
    ("clare", "Clare"),
    ("cork", "Cork"),
    ("derry", "Derry"),
    ("donegal", "Donegal"),
    ("down", "Down"),
    ("dublin", "Dublin"),
    ("fermanagh", "Fermanagh"),
    ("galway", "Galway"),
    ("kerry", "Kerry"),
    ("kildare", "Kildare"),
    ("kilkenny", "Kilkenny"),
    ("laois", "Laois"),
    ("leitrim", "Leitrim"),
    ("limerick", "Limerick"),
    ("longford", "Longford"),
    ("louth", "Louth"),
    ("mayo", "Mayo"),
    ("meath", "Meath"),
    ("monaghan", "Monaghan"),
    ("offaly", "Offaly"),
    ("roscommon", "Roscommon"),
    ("sligo", "Sligo"),
    ("tipperary", "Tipperary"),
    ("tyrone", "Tyrone"),
    ("waterford", "Waterford"),
    ("westmeath", "Westmeath"),
    ("wexford", "Wexford"),
    ("wicklow", "Wicklow"),
)


# Furniture model


class Furniture(models.Model):
    """
    A model to create and manage furniture posts
    """
    user = models.ForeignKey(User, related_name="furniture_owner",
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=15, null=False, blank=False)
    furniture_type = models.CharField(max_length=50, choices=FURNITURE_TYPES,
                                      default="armchair")
    room = models.CharField(max_length=50, choices=ROOMS, default="bathroom")
    description = models.TextField(max_length=10000, null=False, blank=False)
    county = models.CharField(max_length=50, choices=COUNTIES,
                              default="antrim")
    town = models.CharField(max_length=100, null=False, blank=False)
    image = ResizedImageField(
        size=[None, 400],
        quality=75,
        upload_to="furniture/",
        force_format="WEBP",
        blank=False,
        null=False,
    )
    image_alt = models.CharField(max_length=100, null=False, blank=False)
    condition = models.CharField(max_length=50, choices=CONDITION,
                                 default="as new")
    posted_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-posted_date"]

    def __str__(self):
        return str(self.title)


# Comment model


class Comment(models.Model):

    furniture_post = models.ForeignKey(Furniture, on_delete=models.CASCADE,
                                       related_name='comments', null=True)
    name = models.CharField(max_length=80)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'Comment {self.message} by {self.name}'
