from django.db import models

# Create your models here.



class Service(models.Model):
    service_id=models.AutoField(primary_key=True,unique=True,null=False)
    name=models.CharField(max_length=50)
    Type=models.CharField(max_length=50)
    ip=models.GenericIPAddressField()

    def __str__(self):
        return str(self.service_id)
    
    
    

class SoftSwitch(models.Model):
    soft_id=models.AutoField(primary_key=True,unique=True,null=False)
    service_id=models.OneToOneField(Service,unique=True,null=False,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.service_id.service_id)


class SBC(models.Model):
    sbc_id=models.AutoField(primary_key=True,unique=True,null=False)
    service_id=models.OneToOneField(Service,unique=True,null=False,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.service_id.service_id)
