
class Employees():
    def __init__(self,name,id,birthdate,role,userName,password,email,adress):
        self.name=name
        self.id=id
        self.email=email
        self.adress=adress
        self.birthdate=birthdate
        self.role=role
        self.userName=userName
        self.password=password

class Patient():
    def __init__(self,id,name,birthdate,gender,adress,numberPhone,email,emergencyContact,patientSecure):
        self.id=id
        self.name=name
        self.birthdate=birthdate
        self.gender=gender
        self.adress=adress
        self.numberPhone=numberPhone
        self.emergencyContact=emergencyContact
        self.patientSecure=patientSecure
        self.email=email
        
#class ClinicHistory():
    #def __init__(self, date,doctorId, reasonConsultation, symptoms,  diagnosis, procedure, procedureDetail, medicine, medicineDose):
        #self.date=date
        #self.doctorId=doctorId
        #self.reasonConsultation=reasonConsultation
        #self.symptoms=symptoms
        #self.diagnosis=diagnosis
        #self.procedure=procedure
        #self.procedureDetail=procedureDetail
        #self.medicine=medicine
        #self.medicineDose=medicineDose

class MedicalOrder():
    def __init__(self, OrderNumber, IdPatient, IdDoctor, CreationDate):
        self.OrderNumber=OrderNumber
        self.IdPatient=IdPatient
        self.IdDoctor=IdDoctor
        self.CreationDate=CreationDate

class StatusOrder():
    def __init__(self, companyName, policyNumber, statusPolicy, policyVigency):
        self.companyName=companyName
        self.policyNumber=policyNumber
        self.statusPolicy=statusPolicy
        self.policyVigency=policyVigency

class ProcedureOrder():
    def __init__(self, orderNumber,IdProcedure,amount,frecuency,attendance,IdSpecialist,item):
        self.orderNumber=orderNumber
        self.IdProcedure=IdProcedure
        self.amount=amount
        self.frecuency=frecuency
        self.attendance=attendance
        self.IdSpecialist=IdSpecialist
        self.item=item

class DiagnosticHelp():
    def __init__(self, orderDiagnostic,IdHelp,amountHelp,frecuencyHelp,attendanceHelp,IdSpecialistHelp,itemHelp):
        self.orderDiagnostic=orderDiagnostic
        self.IdHelp=IdHelp
        self.amountHelp=amountHelp
        self.frecuencyHelp=frecuencyHelp
        self.attendanceHelp=attendanceHelp
        self.IdSpecialistHelp=IdSpecialistHelp
        self.itemHelp=itemHelp

class NurseVisit():
    def __init__(self, bloodPresure,temperature,pulse,bloodOxygen):
        self.bloodPresure=bloodPresure
        self.temperature=temperature
        self.pulse=pulse
        self.bloodOxygen=bloodOxygen

class Clinic():
    def __init__(self):
        self.Employees=[]
        self.Patient=[]
        #self.ClinicHistory={}
        self.MedicalOrder=[]
        self.StatusOrder=[]
        self.ProcedureOrder=[]
        self.DiagnosticHelp=[]
        self.NurseVisit=[]

class PatientInformation():
    def __init__(self,id,name,birthdate,gender,adress,numberPhone,email,emergencyContact,patientSecure):
        self.id=id
        self.name=name
        self.birthdate=birthdate
        self.gender=gender
        self.adress=adress
        self.numberPhone=numberPhone
        self.emergencyContact=emergencyContact
        self.patientSecure=patientSecure
        self.email=email


