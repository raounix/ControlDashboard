from django.db import models

# Create your models here.

Type = ( 
    ("ssw", "SSW"), 
    ("sbc","SBC"),
   
) 

class Server(models.Model):
    server_id=models.AutoField(primary_key=True,unique=True,null=False)
    name=models.CharField(unique = True ,max_length=50)
    ip=models.GenericIPAddressField()
    Type=models.CharField(max_length=20,choices=Type,default='ssw')
    def __str__(self):
        return str(self.server_id)
    class Meta:
        ordering = ['ip',]

 
    
class SBCConfig(models.Model):
    config_id=models.AutoField(primary_key=True,unique=True,null=False)
    config=models.FileField(upload_to='Dashboard/static/config_files/SBC',null=True)
    def __str__(self):
        return str("config id " + str(self.config_id))
    
    
class SSWConfig(models.Model):
    config_id=models.AutoField(primary_key=True,unique=True,null=False)
    config=models.FileField(upload_to='Dashboard/static/config_files/SSW',null=True)
    def __str__(self):
        return str("config id " + str(self.config_id))
    
class RTPConfig(models.Model):
    config_id=models.AutoField(primary_key=True,unique=True,null=False)
    config=models.FileField(upload_to='Dashboard/static/config_files/RTP',null=True)
    def __str__(self):
        return str("config id " + str(self.config_id))
    



class SSW(models.Model):
    ssw_id = models.AutoField(primary_key=True,unique=True,null=False)
    server_id=models.OneToOneField(Server,on_delete=models.CASCADE)
    # config=models.OneToOneField(SSWConfig,on_delete=models.CASCADE)
    
    def __str__(self):
        return str( "server id :"+ (str(self.server_id.server_id)))


class SBC(models.Model):
    sbc_id = models.AutoField(primary_key=True,unique=True,null=False)
    server_id=models.OneToOneField(Server,on_delete=models.CASCADE)
    # config=models.OneToOneField(SBCConfig,on_delete=models.CASCADE)
    
    def __str__(self):
        return str( "server id :"+ (str(self.server_id.server_id)))

class RTP(models.Model):
    rtp_id = models.AutoField(primary_key=True,unique=True,null=False)
    server_id=models.OneToOneField(Server,on_delete=models.CASCADE)
    # config=models.OneToOneField(SBCConfig,on_delete=models.CASCADE)
    
    def __str__(self):
        return str( "server id :"+ (str(self.server_id.server_id)))





# class SBC(models.Model):
#     sbc_id=models.AutoField(primary_key=True,unique=True,null=False)
#     service_id=models.OneToOneField(Service,unique=True,null=False,on_delete=models.CASCADE)
#     def __str__(self):
#         return str(self.service_id.service_id)


