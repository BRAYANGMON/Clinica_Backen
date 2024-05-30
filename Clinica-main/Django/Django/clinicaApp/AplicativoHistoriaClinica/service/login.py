def passwordValidator(Employees,password):
    if Employees.password==password:
        return Employees
    raise Exception("la contraseña es incorrecta")

def login(Clinic,userName,password):
    for Employees in Clinic.Employees:
        if Employees.userName==userName:
            return passwordValidator(Employees,password)
    return None