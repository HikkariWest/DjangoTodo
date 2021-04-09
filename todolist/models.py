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