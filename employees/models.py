from django.db import models

# Create your models here.

class ServiceType(models.Model):
    name=models.CharField(max_length=200,default="")

    def __str__(self):
        return self.name
        
class Department(models.Model):
    name = models.CharField(max_length=200,null=True)
    servicetypes=models.ManyToManyField(ServiceType)
    

    def __str__(self):
        return self.name
    


class CostCentre(models.Model):
    name = models.CharField(max_length=200) 
    department = models.ForeignKey(Department, on_delete=models.CASCADE,null=True, related_name="costcentres")
    


    def __str__(self):
        return self.name
    
class ContractType(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Contract(models.Model):


    started=models.DateTimeField('Startdate')
    ended=models.DateTimeField('Enddate')
    contracttype=models.ForeignKey(ContractType, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.contracttype}+___'




class Employee(models.Model):
    name = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    heads=models.IntegerField(default=1)
    pub_date = models.DateTimeField('date scraped')
    contracttime=models.DecimalField(default=0.000, decimal_places=3,max_digits=5)
    timequota=models.BooleanField(default=False)
    position=models.CharField(max_length=200, default="")
    pcontracttime=models.DecimalField(default=0.000, decimal_places=3,max_digits=5)
    bz=models.DecimalField( decimal_places=3,max_digits=5, default=0.0)
    comments=models.CharField(max_length=2000,default="")
    costcentres =models.ManyToManyField(CostCentre)
    departments=models.ManyToManyField(Department)



    contract = models.OneToOneField(
        Contract,
        on_delete=models.CASCADE,
        null=True,
    
    )









    

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return f'{self.name} , {self.firstname}'


class Customer(models.Model):
    name = models.CharField(max_length=200,default="")
    firstname = models.CharField(max_length=200,default="")
    heads=models.DecimalField(default=0.000, decimal_places=3,max_digits=5)
    pub_date = models.DateTimeField('date scraped',null=True)
    caretime=models.DecimalField(default=0.000, decimal_places=3,max_digits=5)
    bz=models.DecimalField( decimal_places=3,max_digits=5, default=0.0)
    
    handicap=models.CharField(max_length=200,default="")
    handicap_number=models.DecimalField( decimal_places=3,max_digits=5, default=0.0)
    comments=models.CharField(max_length=2000,default="")
    senior=models.BooleanField(default=False)
    costcentres =models.ManyToManyField(CostCentre)
    departments=models.ManyToManyField(Department)
    servicetypes=models.ManyToManyField(ServiceType)



    def __str__(self):
        return f'{self.name} , {self.firstname}'





