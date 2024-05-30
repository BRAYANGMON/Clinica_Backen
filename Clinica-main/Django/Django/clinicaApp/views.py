from django.views import View
import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from clinicaApp.AplicativoHistoriaClinica.models.models import Employees,Patient,NurseVisit,PatientInformation
from clinicaApp.AplicativoHistoriaClinica.service import adminService
import clinicaApp.AplicativoHistoriaClinica.validators.inputTypeValidators as inputTypeValidators 
import clinicaApp.AplicativoHistoriaClinica.validators.PatientInputValidator as PatientInputValidator
 
class employees (View):
    @method_decorator(csrf_exempt, name='dispatch')
    def create_employee_view(request):
        if request.method == 'POST':
            data = json.loads(request.body)
            try:
                employee = adminService.create_employee(data)
                return JsonResponse({'status': 'success', 'data': employee.id})
            except ValueError as e:
                return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

@method_decorator(csrf_exempt, name='dispatch')
def delete_employee_view(request, id_number):
    if request.method == 'DELETE':
        try:
            adminService.delete_employee(id_number)
            return JsonResponse({'status': 'success'})
        except Employee.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Employee not found'}, status=404)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

    @method_decorator(csrf_exempt, name='dispatch')
def update_employees_employee_view(request, id_number):
    if request.method == 'UPDATE':
        try:
            adminService.update_employees(id_number)
            return JsonResponse({'status': 'success'})
        except Employee.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Employee not found'}, status=404)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)



"""@method_decorator(csrf_exempt, name='dispatch')
def create_patient_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            patient = adminService.create_patient(data)
            return JsonResponse({'status': 'success', 'data': patient.id})
        except ValueError as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

@method_decorator(csrf_exempt, name='dispatch')
def create_visit_view(request):
    if request.method == 'POST':
        try:
            visit = adminService.create_visit(request.POST)
            return JsonResponse({'message': 'Visit created successfully', 'visit_id': visit.id})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
        
@method_decorator(csrf_exempt, name='dispatch')
def create_medical_record_view(request):
    if request.method == 'POST':
        try:
            medical_record = adminService.create_medical_record(request.POST)
            return JsonResponse({'message': 'Medical record created successfully', 'medical_record_id': medical_record.id})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
              
@method_decorator(csrf_exempt, name='dispatch')
def get_employee_view(request, id_number):
    if request.method == 'GET':
        try:
            employee = adminService.get_employee(id_number)
            return JsonResponse({'status': 'success', 'data': employee.get()})
        except Employee.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Employee not found'}, status=404)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

@method_decorator(csrf_exempt, name='dispatch')
def list_employees_view(request):
    if request.method == 'GET':
        employees = adminService.list_employees()
        return JsonResponse({'status': 'success', 'data': [employee.get() for employee in employees]})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

@method_decorator(csrf_exempt, name='dispatch')
def get_patient_view(request, id_number):
    if request.method == 'GET':
        try:
            patient = adminService.get_patient(id_number)
            return JsonResponse({'status': 'success', 'data': patient.to_dict()})
        except Patient.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Patient not found'}, status=404)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

@method_decorator(csrf_exempt, name='dispatch')
def list_patients_view(request):
    if request.method == 'GET':
        patients = adminService.list_patients()
        return JsonResponse({'status': 'success', 'data': [patient.to_dict() for patient in patients]})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

@method_decorator(csrf_exempt, name='dispatch')
def get_visit_view(request, id_number):
    if request.method == 'GET':
        try:
            visit = adminService.get_visit(id_number)
            return JsonResponse({'status': 'success', 'data': visit.get()})
        except Visit.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Visit not found'}, status=404)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

@method_decorator(csrf_exempt, name='dispatch')
def list_visits_view(request):
    if request.method == 'GET':
        visits = adminService.list_visits()
        return JsonResponse({'status': 'success', 'data': [visit.get() for visit in visits]})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

@method_decorator(csrf_exempt, name='dispatch')
def get_medical_record_view(request, id_number):
    if request.method == 'GET':
        try:
            medical_record = adminService.get_medical_record(id_number)
            return JsonResponse({'status': 'success', 'data': medical_record.get()})
        except MedicalRecord.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Medical record not found'}, status=404)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

@method_decorator(csrf_exempt, name='dispatch')
def list_medical_records_view(request):
    if request.method == 'GET':
        medical_records = adminService.list_medical_records()
        return JsonResponse({'status': 'success', 'data': [medical_record.get() for medical_record in medical_records]})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)"""




      



#