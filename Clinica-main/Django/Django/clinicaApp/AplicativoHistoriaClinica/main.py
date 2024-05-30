from models import models
from service import login
from validators import PatientInputValidator

Clinic=models.Clinic()
patient=models.Employees("admin",1234,"qwert@tdea.edu","admin","admin", "admin", "admin", "admin")
Clinic.Employees.append(patient)

def createDoctor():
    PatientInputValidator.createUser(Clinic,"Doctor")
def createNurses():
    PatientInputValidator.createUser(Clinic,"Enfermera")
def createPatient():
    PatientInputValidator.createPatient(Clinic)
def createMedicalOrder(user):
    PatientInputValidator.createMedicalOrder(Clinic,user)
def createNurseVisit(user):
    PatientInputValidator.createNurseVisit(Clinic,user)
def createAdminPersonal():
    PatientInputValidator.createUser(Clinic, "Personal Administrativo")

def adminMenu(user):
    while True:
        option= input("1. Crear ingreso doctor \n2. Crear ingreso enfermera \n3. Crear personal administrativo \n4. cerrar sesion\n")
        if option=="1":
            createDoctor()
        if option=="2":
            createNurses()
        if option=="3":
            createAdminPersonal()
        if option=="4":
            print("Cerrando sesion \n")
        return
    
def personalMenu(user):
    while(True):
        option=input("1.Crear paciente \n2. Cerrar")
        if option=="1":
            createPatient()
        if option=="2":
            print("Cerrando sesión")
            return
def clinicMenu(user):
    while(True):
        option=input("1.Crear historia clinica \n2. Cerrar")
        if option=="1":
            createMedicalOrder()
        if option=="2":
            print("Cerrando sesión")
            return
        
def nurseMenu(user):
    while True:
        option = input("1. Registrar visita de paciente \n2. Cerrar sesión \n")
        if option == "1":
            createNurseVisit(user)
        if option == "2":
            print("Cerrando sesión \n")
            return

def loginRole(user):
    if user.role=="admin":
        return adminMenu(user)
    if user.role=="Doctor":
        return clinicMenu(user)
    if user.role=="Nurse":
        return nurseMenu(user)
    if user.role=="Personal administrativo":
        return personalMenu(user)
    raise Exception("Rol invalido")

def loginMenu():
    userName = input("Ingrese su usuario \n")
    password = input("Ingrese su contraseña \n")   
    user = login.login(Clinic, userName,password)
    if user==None:
       raise Exception("El usuario no está registrado")
    return loginRole(user)  
while True:
    option=input("1. iniciar sesion \n0. cerrar \n ")
    if option =="1":
        try:
            loginMenu()
        except Exception as error:
            print(str(error))
    if option =="0":
        print("Cerrando el programa")
        break
    