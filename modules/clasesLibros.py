"""aqui estan todas las clases para los productos"""
from random import randint

class Producto:
    def __init__(self, codigo='',titulo='',autor='' ):
        self.__codigo= codigo
        self.__titulo=titulo
        self.__autor  =autor

    #getters y setters

    def get_codigo(self):
        return self.__codigo
    

    def set_codigo(self,value):
        self.__codigo=value
         

    def get_titulo(self):
        return self.__titulo
    
    
    def set_titulo(self,value):
        self.__titulo=value


    def get_autor(self):
        return self.__autor
    
    def set_autor(self,value):
        self.__autor=value
    

    #imprime los datos basicos
    def informacion(self):
        print("codigo:{0}, titulo:{1}, autor:{2}".format(self.get_codigo(), self.get_titulo(), self.get_autor()))


class ProductoImpreso(Producto):
    #metodo constructor
    
    def __init__(self, codigo='',titulo='',autor='',editorial='',ano='',precio=0):
        super().__init__(codigo,titulo,autor)
        self.__editorial=editorial
        self.__ano= ano
        self.__precio=precio
        
    
    #getters y setters
    def get_editorial(self):
        return self.__editorial
    

    def set_editorial(self, value):
        self.__editorial= value


    def get_ano(self):
        return self.__ano
    

    def set_ano(self, value):
        self.__ano= value


    def get_precio(self):
        return self.__precio
    

    def set_precio(self, value):
        self.__precio= value

    #imprime los datos basicos
    def informacion(self):
        print("codigo: {0}, titulo: {1}, autor: {2}, editorial: {3}, año: {4}, precio: {5}"
              .format(self.get_codigo(), self.get_titulo(), self.get_autor(), self.get_editorial(), self.get_ano(), self.get_precio()))



class ProductoGrabado(Producto):

    #metodo constructor
    def __init__(self, codigo='', titulo='', autor='', tiempoDuracion=0, medioTecnologico=''):
        super().__init__(codigo, titulo, autor)
        self.__tiempoDuracion=tiempoDuracion
        self.__medioTecnologico= medioTecnologico


    #Getters y setters
    def get_tiempoDuracion(self):
        return self.__tiempoDuracion
    

    def set_tiempoDuracion(self, value):
        self.__tiempoDuracion = value

    
    def get_medioTecnologico(self):
        return self.__medioTecnologico
    

    def set_medioTecnologico(self, value):
        self.__medioTecnologico = value

    #imprime los datos basicos
    def informacion(self):
        print("codigo: {0}, titulo: {1}, autor: {2}, tiempo de Duracion: {3} minutos, medio Tecnologico: {4}"
              .format(self.get_codigo(), self.get_titulo(), self.get_autor(), self.get_tiempoDuracion(), self.get_medioTecnologico()))


class ProductoSoftware(Producto):
   
   #metodo constructor
    def __init__(self, codigo='', titulo='', autor='', version='', sistemaOperativo=0):
        super().__init__(codigo, titulo, autor)
        self.__version=version
        self.__sistemaOperativo=sistemaOperativo


    #getters y setters
    def get_version(self):
        return self.__version
    

    def set_version(self,value):
        self.__version= value


    def get_sistemaOperativo(self):
        return self.__sistemaOperativo


    def set_sistemaOperativo(self,value):
        self.__sistemaOperativo= value

    
    #imprime los datos basicos
    def informacion(self):
        print("codigo: {0}, titulo: {1}, autor: {2}, version: {3}, sistema Operativo: {4}"
              .format(self.get_codigo(), self.get_titulo(), self.get_autor(), self.get_version(), self.get_sistemaOperativo()))
        

class Revista(ProductoImpreso):

    #metodo Constructor
    def __init__(self, codigo='', titulo='', autor='', editorial='', ano='', precio=0,volumen=''):
        super().__init__(codigo, titulo, autor, editorial, ano, precio)
        self.__volumen = volumen

       
        #getter y setters
    def get_volumen(self):
        return self.__volumen
    

    def set_volumen(self, value):
        self.__volumen = value

    #imprime los datos basicos 
    def informacion(self):
        print("codigo:{0}, titulo:{1}, autor:{2}, editorial:{3}, año:{4}, precio:{5}, volumen:{6}"
            .format(self.get_codigo(), self.get_titulo(), self.get_autor(), self.get_editorial(), self.get_ano(), self.get_precio(), self.get_volumen()))
            
    
    #le asigna un estado al producto
    def estado(self):
        estados=["produccion","revision","Proceso de publicacion","preventa", "lanzamiento"]
        n=randint(0,len(estados)-1)
        print(n) 
        print("el estado del libro es "+ estados[n])


class libro(ProductoImpreso):


    #metodo constructor
    def __init__(self, codigo='', titulo='', autor='', editorial='', ano='', precio=0, idioma=''):
        super().__init__(codigo, titulo, autor, editorial, ano, precio)
        self.__idioma= idioma


    #getters y setters
    def get_idioma(self):
        return self.__idioma
    

    def set_idioma(self, value):
        self.__idioma=value

    
    #imprime los datos basicos
    def informacion(self):
        print("codigo:{0}, titulo: {1}, autor: {2}, editorial: {3}, año: {4}, precio: {5}, idioma: {6}"
            .format(self.get_codigo(), self.get_titulo(), self.get_autor(), self.get_editorial(), self.get_ano(), self.get_precio(), self.get_idioma()))
        
    
    #le asigna un estado al producto
    def estado(self):
        estados=["produccion","revision","Proceso de publicacion","preventa", "lanzamiento"]
        n=randint(0,len(estados))
        print(n) 
        print("el estado del libro es "+ estados[n])
