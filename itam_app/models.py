from django.urls import reverse
from django.db import models
from django.utils.crypto import get_random_string
from simple_history.models import HistoricalRecords
from auditlog.registry import auditlog



class Employee(models.Model):
	name = models.CharField(max_length=250)
	email = models.EmailField()
	employee_number = models.CharField(max_length=100)
	history = HistoricalRecords()


	def __str__(self):
		return self.name


class Asset_Type(models.Model):
	name = models.CharField(max_length=250)
	description = models.CharField(max_length=300)
	history = HistoricalRecords()


	def __str__(self):
		return self.name


class Os_Type(models.Model):	
	name = models.CharField(max_length=250)
	description = models.CharField(max_length=300)	
	history = HistoricalRecords()


	def __str__(self):
		return self.name


class Product_Type(models.Model):
	name = models.CharField(max_length=250)
	description = models.CharField(max_length=300)
	history = HistoricalRecords()


	def __str__(self):
		return self.name

class State_Type(models.Model):
	name = models.CharField(max_length=250)
	description = models.CharField(max_length=300)
	history = HistoricalRecords()


	def __str__(self):
		return self.name

class Department(models.Model):
	name = models.CharField(max_length=250)
	description = models.CharField(max_length=300)
	history = HistoricalRecords()


	def __str__(self):
		return self.name

class Asset(models.Model):
	display_name = models.CharField(max_length=250)
	mac_address = models.CharField(max_length=250)
	serial_number = models.CharField(max_length=250, null=True, blank=True)
	date_assigned = models.DateField()

	employee = models.ForeignKey(Employee, related_name='employee', on_delete=models.CASCADE)
	asset_type = models.ForeignKey(Asset_Type, related_name='asset_type', on_delete=models.CASCADE)
	
	os_type = models.ForeignKey(Os_Type, related_name='asset_type', on_delete=models.CASCADE)
	product_type = models.ForeignKey(Product_Type, related_name='asset_type', on_delete=models.CASCADE)
	state_type = models.ForeignKey(State_Type, related_name='asset_type', on_delete=models.CASCADE)
	department = models.ForeignKey(Department, related_name='asset_type', on_delete=models.CASCADE)
	history = HistoricalRecords()


	def __str__(self):
		return self.display_name

	def get_absolute_url(self):
		return reverse('itam_app:detail', args=[str(self.id)])

	def save(self, *args, **kwargs):
		if self.serial_number is None:
			self.serial_number = 'GWXPH-' + get_random_string(length=15)	


		super().save(*args, **kwargs)



auditlog.register(Asset)