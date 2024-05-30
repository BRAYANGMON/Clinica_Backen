from django.db import models

class Employees(models.Model):
        name=models.CharField(max_length=30)
        id=models.AutoField(primary_key=True)
        email=models.CharField(max_length=30)
        adress=models.CharField(max_length=30)
        birthdate=models.CharField(max_length=30)
        role=models.CharField(max_length=30)
        userName=models.CharField(max_length=30)
        password=models.CharField(max_length=30)

class Patient(models.Model):
        id=models.AutoField(primary_key=True)
        name=models.CharField(max_length=30)
        birthdate=models.CharField(max_length=30)
        gender=models.CharField(max_length=30)
        adress=models.CharField(max_length=30)
        numberPhone=models.CharField(max_length=30)
        email=models.CharField(max_length=30)
        #contato de emergencia, seguro del paciente
        
#class ClinicHistory(models.Model):
       # date=models.CharField(max_length=30)
        #doctorId=models.ForeignKey(Employees,on_delete=models.CASCADE)
        #reasonConsultation=models.CharField(max_length=30)
        #symptoms=models.CharField(max_length=30)
        #diagnosis=models.CharField(max_length=30)
        #procedure=models.CharField(max_length=30)
        #procedureDetail=models.CharField(max_length=30)
        #medicine=models.CharField(max_length=30)
        #medicineDose=models.CharField(max_length=30)

class MedicalOrder(models.Model):
        OrderNumber=models.AutoField(primary_key=True)
        IdPatient=models.ForeignKey(Patient,on_delete=models.CASCADE)
        IdDoctor=models.ForeignKey(Employees,on_delete=models.CASCADE)
        CreationDate=models.CharField(max_length=30)

##orden de estado , orden procedimiento ,orden ayuda diacnostica, vicita enfermera
