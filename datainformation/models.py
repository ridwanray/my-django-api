from django.db import models

#from django.db import models

class DataInformation(models.Model):
	location = models.CharField(max_length=200, blank=True, null=True)
	customer_name = models.CharField(max_length=20, blank=True, null=True)
	amount_paid = models.CharField(max_length=20, blank=True, null=True)
	volume_dispensed = models.DecimalField(default=0,max_digits=20,decimal_places=2,blank=True, null=True)
	complete_status = models.BooleanField(default=False)

	def __str__(self):
		return (self.location)
