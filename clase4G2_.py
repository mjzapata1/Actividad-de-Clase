
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

    def ingresarPaciente(self,pac):
        self.__lista_pacientes.append(pac)

    def verNumeroPacientes(self):
        print(f"En el Sistema se encuentran {str(len(self.__lista_pacientes))} pacientes.")
    
    def verDatosPaciente(self,c):
        for paciente in self.__lista_pacientes:
            if c == paciente.verCedula():
                return paciente
                
def main():
    sis = Sistema()
    while True:
        menu = int(input("\nBienvenido. \nIngrese: \n1. Para ingresar un nuevo paciente.\n2. Para ver paciente.\n3. Para ver la cantidad de pacientes.\n4. Para salir.\nIngrese una opción: "))

        if menu == 1:
            print("\nHa seleccionado la opción de Ingresar un paciente.\nPor favor ingrese los datos solicitados a continuación...")
            nombre = input("\nIngrese el nombre: ")
            cedula = int(input("\nIngrese la cédula: "))
            genero = input("\nIngrese el género: ")
            servicio = input("\nIngrese el servicio: ")
            paciente = Paciente()

            paciente.asignarCedula(cedula)
            paciente.asignarGenero(genero)
            paciente.asignarNombre(nombre)
            paciente.asignarServicio(servicio)
            sis.ingresarPaciente(paciente)
            print("\nEl paciente ha sido alamcenado exitosamente...")

        elif menu == 2:
            print("\nHa seleccionado la opción Ver Paciente...")
            ced = int(input("\nIngrese la cédula del paciente que desea ver: "))
            pbus = sis.verDatosPaciente(ced)
            print("Nombre: " + pbus.verNombre())
            print("Cédula: " + str(pbus.verCedula()))
            print("Género: " + pbus.verGenero())
            print("Servicio: " + pbus.verServicio())

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