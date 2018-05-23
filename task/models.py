from django.db import models

# Create your models here.
class teacher(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=80,default="")
    notify_id=models.TextField(blank=True)
    def __str__(self):
        return self.name
    class Meta:
        db_table="teacher"

class schedule(models.Model):
    teacher=models.ForeignKey('teacher',on_delete='CASCADE',default=1)
    subject=models.CharField(default="",max_length=150)
    classFrom=models.TimeField()
    classTo=models.TimeField()
    def __str__(self):
        return str(str(self.teacher)+" : "+str(self.subject))
    class Meta:
        db_table="schedule"