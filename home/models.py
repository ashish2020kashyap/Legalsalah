from django.db import models

# personal info
class Personal(models.Model):

    first_name=models.CharField(max_length=50,blank=True)
    mid=models.CharField(max_length=50,blank=True)
    last_name=models.CharField(max_length=50,blank=True)
    gender=models.CharField(max_length=50,blank=True)
    dob=models.DateField()
    pan_number=models.CharField(max_length=50,blank=True)
    father_name=models.CharField(max_length=50,blank=True)
    
    marital_status=models.CharField(max_length=50,blank=True)
    
class Address(models.Model):
    flat_num=models.CharField(max_length=50,blank=True)
    premise_name=models.CharField(max_length=50,blank=True)
    road_name=models.CharField(max_length=50,blank=True)
    pincode=models.CharField(max_length=50,blank=True)
    area =models.CharField(max_length=50,blank=True)
    town_name=models.CharField(max_length=50,blank=True)
    state_name=models.CharField(max_length=50,blank=True)
    country_name=models.CharField(max_length=50,blank=True)
    contact_number=models.CharField(max_length=50,blank=True)
    email=models.EmailField(max_length=50,blank=True)
    email2=models.EmailField(max_length=50,blank=True)
#income/salary
class Salary(models.Model):
    employer_name=models.CharField(max_length=50,blank=True)
    employer_type=models.CharField(max_length=50,blank=True)
    salary=models.CharField(max_length=50,blank=True)
    perquisites=models.CharField(max_length=50,blank=True)
    profit=models.CharField(max_length=50,blank=True)
    allowances=models.CharField(max_length=50,blank=True)
    balance=models.CharField(max_length=50,blank=True)
    deduction=models.CharField(max_length=50,blank=True)
    std_deduciton=models.CharField(max_length=50,blank=True)
    professional_tax=models.CharField(max_length=50,blank=True)
    income_chargeable=models.CharField(max_length=50,blank=True)
    tds=models.CharField(max_length=50,blank=True)
    tan=models.CharField(max_length=50,blank=True)

class Otherincomee(models.Model):
    saving_bank=models.CharField(max_length=50,blank=True)
    deposit=models.CharField(max_length=50,blank=True)
    other=models.CharField(max_length=50,blank=True)

  
class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
  
    class Meta:  
        db_table = "myapp_document"


class DocumentUpload(models.Model):
    name = models.CharField(max_length=255, blank=True)
    upload_file = models.FileField(upload_to='doc/', null=True, blank=True)
    upload_date = models.DateTimeField(auto_now_add =True)

    def __str__(self):
        return self.name







