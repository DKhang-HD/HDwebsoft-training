from django.db import models

# Create your models here.

class Student(models.Model):
    # It is impossible to change a nullable field 'file_student' on student to non-nullable without providing a default. This is because the database needs something to populate existing rows
    # If don't set null = True for 2 column
    # auto_increment_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200,null = True)
    grade = models.IntegerField(null = True)
    file_student = models.FileField(null = True)
    def __str__(self):
        return self.name
