import datetime

def createUser(name,id,email,username,password,birthdate,adress):
    print("validar datos \n")
    inputTypeValidators.stringValidator(name,"nombre del usuario \n")
    id=inputTypeValidators.integerValidator(id,"cedula del usuario \n")
    inputTypeValidators.stringValidator(email,"correo del usuario \n")
    inputTypeValidators.stringValidator(userName, "Nombre del usuario \n")
    inputTypeValidators.stringValidator(password, "contraseña \n")
    inputTypeValidators.stringValidator(birthdate,"fecha de nacimiento \n")
    inputTypeValidators.stringValidator(adress,"direccion del usuario \n")
    adminService.createUser(name,id,email,role,userName,password,adress,birthdate)

def createPatient(id,name,birthdate,gender,adress,numberPhone,):
    id=inputTypeValidators.integerValidator(id,"cedula del Paciente \n")
    inputTypeValidators.stringValidator(name,"nombre del Paciente \n")
    inputTypeValidators.stringValidator(birthdate,"fecha de nacimiento del Paciente \n")
    inputTypeValidators.stringValidator(gender,"genero del Paciente \n")
    inputTypeValidators.stringValidator(adress,"direccion del Paciente \n")
    numberPhone=inputTypeValidators.integerValidator(numberPhone,("Ingrese el numero de contacto del Paciente \n"),"movil del Paciente \n")
    inputTypeValidators.stringValidator(email,"correo del Paciente \n")
    adminService.createPatient(id,name,birthdate,gender,adress,numberPhone,email)

def createClinicHistory(date,id,reasonConsultation,symptoms,diagnosis):
    date=datetime.datetime.today()
    print(date)
    id=inputTypeValidators.integerValidator(id,"cedula del usuario \n")
    inputTypeValidators.stringValidator(reasonConsultation,"Consulta realizada \n")
    inputTypeValidators.stringValidator(symptoms,"sinmatologia \n")
    inputTypeValidators.stringValidator(diagnosis,"Diagnostico realizado \n")
    adminService.createClinicHistory(Clinic,user,id,reasonConsultation,symptoms,diagnosis)
    
def createNurseVisit(id,bloodPressure,temperatura,pulse,oxygenLevel,procedure,procedureDetail,medicine,medicineDose,tests,observation,date):
    id=inputTypeValidators.integerValidator(id,"cedula del usuario \n")
    inputTypeValidators.stringValidator(bloodPressure,"presion realizada \n")
    inputTypeValidators.stringValidator(temperature,"temperatura registrada \n")
    inputTypeValidators.stringValidator(pulse,"Pulso realizado \n")
    inputTypeValidators.stringValidator(oxygenLevel,"Oxigeno agregados \n")
    inputTypeValidators.stringValidator(procedure,"Procedimiento agregado \n")
    inputTypeValidators.stringValidator(procedureDetail,"Detalle guardado \n")
    inputTypeValidators.stringValidator(medicine,"Medicina registrada \n")
    inputTypeValidators.stringValidator(medicineDose,"Diagnostico de medicina realizado \n")
    inputTypeValidators.stringValidator(tests,"prueba registrada\n")
    inputTypeValidators.stringValidator(observation,"observacion realizado \n")
    inputTypeValidators.stringValidator(date,"dato realizado \n")
    adminService.createNurseVisit(Clinic, user, id, bloodPressure,temperature,pulse,oxygenLevel,medicine,procedure, procedureDetail, tests, observation,date)