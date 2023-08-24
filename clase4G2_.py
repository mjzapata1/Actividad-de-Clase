ver = True
class Paciente:
    def __init__(self):
      self.__nombre = ""
      self.__cedula = 0
      self.__genero = ""
      self.__servicio = ""
      
    def verNombre(self):
        return self.__nombre
    def verServicio(self):
        return self.__servicio
    def verGenero(self):
        return self.__genero
    def verCedula(self):
        return self.__cedula
    
    def asignarNombre(self,n):
        self.__nombre = n
    def asignarServicio(self,s):
        self.__servicio = s
    def asignarGenero(self,g):
        self.__genero = g
    def asignarCedula(self,c):
        self.__cedula = c

class Sistema:
    def __init__(self):
      self.__lista_pacientes = []

    def ingresarPaciente(self,ced):
        ing = True
        for p in self.__lista_pacientes:
            if ced == p.verCedula():
                ing = False
        if ing == True:
            nombre = input("\nIngrese el nombre: ")
            genero = input("\nIngrese el género: ")
            servicio = input("\nIngrese el servicio: ")
            paciente = Paciente()
            paciente.asignarCedula(ced)
            paciente.asignarGenero(genero)
            paciente.asignarNombre(nombre)
            paciente.asignarServicio(servicio)
            self.__lista_pacientes.append(paciente)
            print("\nEl paciente ha sido alamcenado exitosamente...")
        elif ing == False:
            print("\nEl paciente ya se encuentra registrado...")

    def verNumeroPacientes(self):
        print(f"En el Sistema se encuentran {str(len(self.__lista_pacientes))} pacientes.")
    
    def verDatosPaciente(self,c):
        for paciente in self.__lista_pacientes:
          if c == paciente.verCedula():
            ver = True
            print("Nombre: " + paciente.verNombre())
            print("Cédula: " + str(paciente.verCedula()))
            print("Género: " + paciente.verGenero())
            print("Servicio: " + paciente.verServicio())
          else:
            ver = False

        if ver == False:
          print("\nLa cédula que ha ingresado no se encuentra registrada...")
                
def main():
    sis = Sistema()
    while True:
        menu = int(input("\nBienvenido. \nIngrese: \n1. Para ingresar un nuevo paciente.\n2. Para ver paciente.\n3. Para ver la cantidad de pacientes.\n4. Para salir.\nIngrese una opción: "))

        if menu == 1:
            print("\nHa seleccionado la opción de Ingresar un paciente.\nPor favor ingrese los datos solicitados a continuación...")
            cedula = int(input("\nIngrese la cédula: "))
            sis.ingresarPaciente(cedula)

        elif menu == 2:
            print("\nHa seleccionado la opción Ver Paciente...")
            ced = int(input("\nIngrese la cédula del paciente que desea ver: "))
            pbus = sis.verDatosPaciente(ced)

        elif menu == 3:
            print("\nHa seleccionado la opción Ver la Cantidad de pacientes...")
            sis.verNumeroPacientes()

        elif menu == 4:
            print("Hasta pronto")
            break

        else:
            print("\nIngrese una opción válida...")

if __name__ == "__main__" :
    main()