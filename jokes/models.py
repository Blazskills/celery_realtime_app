from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    
    
    

class TacState(BaseModel):
    church_state = models.CharField(max_length=64)
    superintendent_name = models.CharField(max_length=64, null=True)
    phone =  models.CharField(max_length=64)

    def __str__(self):
        return f"{self.church_state} ({self.superintendent_name})"
    
    class Meta:
        verbose_name = "Tac State List"
        
        
class District(BaseModel):
    church_assembly_location = models.CharField(max_length=64)
    pastor_incharge = models.CharField(max_length=64, null=True)
    phone =  models.CharField(max_length=64)
    tacstatename = models.ForeignKey(TacState, on_delete=models.CASCADE,  related_name='tacstatelist', db_index=True, null=True, blank=True)
    
    def __str__(self):
        return f"{self.church_assembly_location} ({self.pastor_incharge})"
    
    class Meta:
        verbose_name = "Tac district List"