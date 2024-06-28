"""aqui se encuentran las clases para los aprendices y instructores"""
from random import randint
import datetime 

class Persona:
    #define el metodo constructor
    def __init__(self, documento='', nombreCompleto=''):
        self.__documento = documento
        self.__nombreCompleto = nombreCompleto
        
    #getter y setters
    def get_documento(self):
        return self.__documento
    
    
    def get_nombreCompleto(self):
        return self.__nombreCompleto
    
    
    def set_documento(self, value):
        self.__documento = value
     
        
    def set_nombreCompleto(self, value):
        self.__nombreCompleto = value
      
      #metodo que retorna la informacion de la clase  
    def informacion(self):
        print("nombre completo:{1}, documento:{2}".format(self.__nombreCompleto, self.__documento))
        
    
class Aprendiz(Persona):
    #define el metodo construtor
    def __init__(self, documento='', nombreCompleto='', ficha='' ,programa=''):
        super().__init__(documento, nombreCompleto)#traemos los atributos de la super clase
        self.__ficha = ficha
        self.__programa = programa
       
    #getter y setters    
    def get_ficha(self):
        return self.__ficha
    
    
    def get_programa(self):
        return self.__programa
    
    
    def set_ficha(self, value):
        self.__ficha = value
     
        
    def set_programa(self,value):
        self.__programa = value
       
        
    #asigna una matricula aleatoria
    def matricula(self):
        matricula=["Matriculado","No matriculado"]
        n=randint(0,len(matricula)-1)
        #print(n) 
        print("el Aprendiz se encutra: "+ matricula[n])
       
    

class EtapaLectiva(Aprendiz):

    
    #metodo constructor
    def __init__(self, documento='', nombreCompleto='', ficha='' ,programa='',
                 numeroTrimestre='',fechaInicio='',fechaTerminacion=''):
        super().__init__(documento, nombreCompleto, ficha, programa)
        self.__numeroTrimestre= numeroTrimestre
        self.__fechaInicio=fechaInicio
        self.__fechaTerminacion=fechaTerminacion
    
        
    #Getters y setters
    def get_numeroTrimestre(self):
        return self.__numeroTrimestre
    
    
    def set_numeroTrimeste(self, value):
        self.__numeroTrimestre=value
       
        
    def get_fechaInicio(self):
        return self.__fechaInicio
    
    
    def set_fechaInicio(self, value):
        self.__fechaInicio=value
      
        
    def get_fechaTerminacion(self):
        return self.__fechaTerminacion
   
    
    def set_fechaTerminacion(self, value):
        self.__fechaTerminacion=value
        
    
    #imprime la informacion basica
    def informacion(self):
        print("Nombre completo:{0}, Documento:{1}, Ficha:{2}, Programa:{3}, Numero de trimestre:{4}, Fecha de Inicio: {5}, Fecha de Terminacion: {6}".format(self.get_nombreCompleto(), self.get_documento(), self.get_ficha(),self.get_programa(),self.get_numeroTrimestre(),self.get_fechaInicio(), self.get_fechaTerminacion()))
        

    #le asigna un estado aleatorio 
    def estado(self):
        estados=["activo","suspendido","retirado"]
        n=randint(0,2)
        print(n) 
        print("el estado de estudiantes es: "+ estados[n])
       
    
    
class EtapaProductiva(Aprendiz):
    
    #metodo constructor
    def __init__(self, documento='', nombreCompleto='', ficha='' ,programa='',
                modalidad='',fechaInicio='',fechaTerminacion=''):
        super().__init__(documento, nombreCompleto, ficha, programa)
        self.__modalidad= modalidad
        self.__fechaInicio=fechaInicio
        self.__fechaTerminacion=fechaTerminacion
     
        
    #getters y setters
    def get_modalidad(self):
        return self.__modalidad
    
    
    def set_modalidad(self ,value):
        self.__modalidad=value

    
    def get_fechaInicio(self):
        return self.__fechaInicio
    
    
    def set_fechaInicio(self, value):
        self.__fechaInicio=value
      
        
    def get_fechaTerminacion(self):
        return self.__fechaTerminacion
   
    
    def set_fechaTerminacion(self, value):
        self.__fechaTerminacion=value
        

    #asigna un estado aleatorio
    def estado(self):
        estados=["activo","suspendido","retirado"]
        n=randint(0,2)
        print(n) 
        print("el estado de estudiantes es: "+ estados[n])


    #imprime los datos basicos en pantalla
    def informacion(self):
        print("Nombre completo: {0}, Documento: {1}, Ficha: {2}, Programa: {3}, modalidad: {4}, Fecha de Inicio: {5}, Fecha de Terminacion: {6}".format(self.get_nombreCompleto(), self.get_documento(), self.get_ficha(),self.get_programa(),self.get_modalidad(),self.get_fechaInicio(), self.get_fechaTerminacion()))
     
    
   
class Instructor(Persona):

    
    #metodo constructor
    def __init__(self, documento='', nombreCompleto='',profesion='', salarioBasico=0):
        super().__init__(documento, nombreCompleto)
        self.__profesion=profesion
        self.__salarioBasico= salarioBasico
        
    
    #getters y setters
    def get_profesion(self):
        return self.__profesion
    
    def set_profesion(self, value):
        self.__profesion= value
        
    def get_salarioBasico(self):
        return self.__salarioBasico
    
    def set_salarioBasico(self, value):
        self.__salarioBasico= value
    

    #imprime en pantalla cuanto le queda al contrato, en los parametros se debe poner la fecha de finalizacion del contrato
    # en años, mes y dia 
    def contrato(self, ano, mes, dia):
        fechafinalizacion= datetime.datetime(ano,mes,dia)
        fechaHoy= datetime.datetime.now()
        contrato= (fechafinalizacion - fechaHoy)
        diasTotal= contrato.days  #sacamos los dias del contrato
        meses= diasTotal // 30 #aproximando 30 dias por mes
        dias= diasTotal %30 #dias restantes
        print("duracion del contrato:")
        print(f"{meses} meses, {dias} dias")
        return fechafinalizacion
        

class InstructorPlanta(Instructor):
    

    #metodo constructor
    def __init__(self, documento='', nombreCompleto='', profesion='', salarioBasico=0,grado=0 ,fechaVinculacion=''):
        super().__init__(documento, nombreCompleto, profesion, salarioBasico)
        self.__grado=grado
        self.__fechaVinculacion=fechaVinculacion
        
        
    #setters y getters
    def get_grado(self):
        return self.__grado
    

    def set_grado(self, value):
        self.__grado= value


    def get_fechaVinculacion(self):
        return self.__fechaVinculacion
    

    def set_fechaVinculacion(self, value):
        self.__fechaVinculacion= value

     
     # imprime los datos basicos en pantalla
    def informacion(self):
        print("Nombre completo:{0}, Documento:{1}, profesion:{2}, salario Basico:{3}, grado:{4}, Fecha de Vinculacion: {5}".format(self.get_nombreCompleto(), self.get_documento(), self.get_profesion(),self.get_salarioBasico(),self.get_grado(),self.get_fechaVinculacion()))
        
    
    #asigna un estado aleatorio
    def estado(self):
        estados=["activo","suspendido","retirado"]
        n=randint(0,len(estados)-1)
        #print(n) 
        print("el estado del instructor es"+ estados[n])


    #imprime en pantalla en sueldo asignado
    def sueldo(self):
        salario=self.get_salarioBasico()
        grado= self.get_grado()* 100000
        sueldo=salario+ grado
        print("el sueldo de {0} con la profesion{1} es de: ".format(self.get_nombreCompleto(), self.get_profesion()), sueldo)
        

class InstructorContrato(Instructor):
    
    
    #metodo constructor
    def __init__(self, documento='', nombreCompleto='', profesion='', salarioBasico=0,duracionContrato=0, ano=0, mes=0, dia=0):
        super().__init__(documento, nombreCompleto, profesion, salarioBasico)
        self.__duracionContrato=duracionContrato
        self.__fechaVinculacion=datetime.datetime(ano, mes, dia)
       
        
    #getters y setters
    def get_duracionContrato(self):
        return self.__duracionContrato
    
    
    def set_duracionContrato(self, value):
        self.__duracionContrato= value
        
        
    def get_fechaVinculacion(self):
        return self.__fechaVinculacion
    
    
    def set_fechaVinculacion(self, ano, mes, dia):
        self.__fechaVinculacion= datetime.datetime(ano, mes,dia)
        

    #imprime los datos basicos en pantalla   
    def informacion(self):
        print("Nombre completo:{0}, Documento:{1}, profesion:{2}, salario Basico:{3}, duracion del contrato:{4}, Fecha de Vinculacion: {5}".format(self.get_nombreCompleto(), self.get_documento(), self.get_profesion(),self.get_salarioBasico(),self.get_duracionContrato,self.get_fechaVinculacion))


    # en el parametros se debe poner la fecha de finalizacion del contrato en año,mes,dia
    def estado(self, ano, mes, dia):# imprimira cuanto le queda de contrato al instructor
        fechaIngreso= self.get_fechaVinculacion()
        fechaContrato= self.contrato(ano,mes,dia)
        anos = fechaContrato.year - fechaIngreso.year # Calcula la diferencia en años entre la fecha de contrato y la fecha de vinculación
        meses = fechaContrato.month - fechaIngreso.month # Calcula la diferencia en meses entre la fecha de contrato y la fecha de vinculación
        dias = fechaContrato.day - fechaIngreso.day # Calcula la diferencia en días entre la fecha de contrato y la fecha de vinculación

        if dias < 0:  #Si la diferencia en días es negativa, significa que no se ha completado un mes completo
            meses -= 1 # Resta un mes de la diferencia en meses
        # Calcula el número de días en el mes anterior a la fecha de ingreso
                    #se crea una nueva fecha -obtiene el mes de la fecha-asegura el siguiente mes,dia 
            dias += (fechaIngreso.replace(month=fechaIngreso.month % 12 + 1, day=1) - datetime.timedelta(days=1)).day

        if meses < 0:# Si la diferencia en meses es negativa, significa que no se ha completado un año completo
            anos -= 1# Resta un año de la diferencia en años
            meses += 12# Ajusta la diferencia en meses sumando 12 (para convertir el negativo a positivo)

        print("al contrato le queda:")
        print(f"{anos} años {meses} meses {dias} dias")
        return anos, meses, dias # Devolvemos la duración restante del contrato en años, meses y días
    

    #imprime el sueldo asignado
    def sueldo(self):
        print("el sueldo del instructor es de:", self.get_salarioBasico())
        

       
        


