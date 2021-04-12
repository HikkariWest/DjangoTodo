from django.db import models
from django.utils import timezone
import uuid
from django.utils.text import slugify

# Create your models here.
class TodoItem(models.Model):
	uu_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
	title = models.CharField(max_length = 100)
	description = models.TextField(blank = True)
	completed = models.BooleanField(default = False)


	def __str__(self):
		return self.title

class TestModel(models.Model):
	slug = models.SlugField(null = False, unique = True, blank = True)	
	boolean = models.BooleanField(default = True, verbose_name = 'This is a field for completed')
	title = models.CharField(max_length= 50, default= False)
	datefield = models.DateField(default = timezone.now)
	decimal = models.DecimalField(decimal_places = 2, max_digits= 6)
	email = models.EmailField(max_length = 40)
	file = models.FileField(upload_to = 'uploads', blank = True)
	image = models.ImageField(upload_to='uploads', blank = True)
	integer = models.IntegerField()
	positive_integer = models.PositiveIntegerField()
	positive_small_integer = models.PositiveSmallIntegerField()
	text = models.TextField()
	url = models.URLField(max_length = 300)
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
	
	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		return super().save(*args, **kwargs)

class Student(models.Model):
	name = models.CharField(max_length = 100)
	MONTHS = [
	 (1, 'January'),
	 (2, 'February'),
	 (3, 'March'),
	 (4, 'April'),
	 (5, 'May'),
	 (6, 'June'),
	 (7, 'July'),
	 (8, 'August'),
	 (9, 'September'),
	 (10, 'October'),
	 (11, 'November'),
	 (12, 'December'),
	 ]
	WEEK_DAYS = [
	(None, 'Day is not selected'),
	('mo', 'Monday'),
	('tu', 'Tuesday'),
	('we', 'Wednesday'),
	('th', 'Thursday'),
	('fr', 'Friday'),
	('sa', 'Saturday'),
	('su', 'Sunday'),
	]
	month = models.PositiveSmallIntegerField(blank = False, choices = MONTHS, default = 1)
	week_day = models.CharField(max_length = 50, choices = WEEK_DAYS, blank  = True)
	registed_at = models.DateField(default = timezone.now)