""""
CBA
Ficha: 2877795
Aprendiz: Kevin Donato Jimenez Rocha
version: 0.5
fecha: 06/06/2024

"""
from modules import clases as cl
from modules import excepcion as ex
from modules import clasesLibros as cll

#instanciamos las clases
etapaLectiva1= cl.EtapaLectiva("1000580625","kevin","28487","ADSO","2","2024-01-22","2025-10-22")
etapaPratica1=cl.EtapaProductiva("1000580625","kevin","28487","ADSO","presencial","2025-10-22","2026-3-22")
instructorPlanta1= cl.InstructorPlanta("5584421","Juan","Ingeniero",1500,3,"2022-05-15")
instructorContrato=cl.InstructorContrato("5584421","Juan","Ingeniero",1500,6,2022,5,15)
revista= cll.Revista("25","Como Dormir sin llorar","Donato","salvador","2005",15000,"05")
libro=cll.libro("30","el banquete","platon","DC","2015",5000,"español")
productoGrabado=cll.ProductoGrabado("50","nosequeponer","alejandro fernadez",60,"spotify")
productoSotfware=cll.ProductoSoftware("40","Bases de Datos","jimenez","5.0",5)
#probamos los metodos y atributos de las clases
if __name__=="__main__":
    #etapa Lectiva
    """"
    print("Etapa Lectiva")
    etapaLectiva1.set_documento(value= ex.verificacionNumerosSTR("ingrese el nuevo documento: "))
    print(etapaLectiva1.get_documento())
    etapaLectiva1.set_nombreCompleto(value=ex.verificacionTexto("ingrese el Nombre de la Persona: "))
    print(etapaLectiva1.get_nombreCompleto())
    etapaLectiva1.set_ficha(value=ex.verificacionNumerosSTR("ingrese la ficha del Aprendiz: "))
    print(etapaLectiva1.get_ficha())
    etapaLectiva1.set_programa(value=ex.verificacionTexto("ingrese el Programa al que pertenece el aprendiz: "))
    print(etapaLectiva1.get_programa())
    etapaLectiva1.matricula()
    etapaLectiva1.set_numeroTrimeste(value=ex.verificacionNumerosSTR("ingrese el numero del trimestre que pertenece: "))
    print(etapaLectiva1.get_numeroTrimestre())
    etapaLectiva1.set_fechaInicio(value=input("ingrese la fecha que ingreso(2000-04-31): "))
    print(etapaLectiva1.get_fechaInicio())
    etapaLectiva1.set_fechaTerminacion(value=input("ingrese la fecha que termina la etapa lectiva: "))
    print(etapaLectiva1.get_fechaTerminacion())
    etapaLectiva1.estado()
    etapaLectiva1.informacion()
    
    #etapa Practica
    print("\n","-"*40)
    print("Etapa Practica")
    etapaPratica1.set_documento(value= ex.verificacionNumerosSTR("ingrese el nuevo documento: "))
    print(etapaPratica1.get_documento())
    etapaPratica1.set_nombreCompleto(value=ex.verificacionTexto("ingrese el Nombre de la Persona: "))
    print(etapaPratica1.get_nombreCompleto())
    etapaPratica1.set_ficha(value=ex.verificacionNumerosSTR("ingrese la ficha del Aprendiz: "))
    print(etapaPratica1.get_ficha())
    etapaPratica1.set_programa(value=ex.verificacionTexto("ingrese el Programa al que pertenece el aprendiz: "))
    print(etapaPratica1.get_programa())
    etapaPratica1.matricula()
    etapaPratica1.set_modalidad(value=ex.verificacionTexto("ingrese su modalidad: "))
    print(etapaPratica1.get_modalidad())
    etapaPratica1.set_fechaInicio(value=input("ingrese la fecha que ingreso(2000-04-31): "))
    print(etapaPratica1.get_fechaInicio())
    etapaPratica1.set_fechaTerminacion(value=input("ingrese la fecha que termina la etapa lectiva(2000-04-31): "))
    print(etapaPratica1.get_fechaTerminacion())
    etapaPratica1.estado()
    etapaPratica1.informacion()
    
    #Instructor Planta
    print("\n","-"*40)
    print("Instructor planta")
    instructorPlanta1.set_documento(value= ex.verificacionNumerosSTR("ingrese el nuevo documento: "))
    print(instructorPlanta1.get_documento())
    instructorPlanta1.set_nombreCompleto(value=ex.verificacionTexto("ingrese el Nombre de la Persona: "))
    print(instructorPlanta1.get_nombreCompleto())
    instructorPlanta1.set_profesion(value=ex.verificacionTexto("Ingrese su profesion: "))
    print(instructorPlanta1.get_profesion())
    instructorPlanta1.set_salarioBasico(value=ex.solicitar_dato_int("Ingrese el salario del instructor: "))
    print(instructorPlanta1.get_salarioBasico())
    instructorPlanta1.contrato(2025,1,15)
    instructorPlanta1.set_grado(value=ex.solicitar_dato_int("ingrese su grado(1-20): "))
    print(instructorPlanta1.get_grado())
    instructorPlanta1.set_fechaVinculacion(value=input("ingrese la fecha de vinculacion(2000-04-31): "))
    print(instructorPlanta1.get_fechaVinculacion())
    instructorPlanta1.informacion()
    instructorPlanta1.estado()
    instructorPlanta1.sueldo()
    
    #instructor Contrato
    print("\n","-"*40)
    print("Instructor contrato")
    instructorContrato.set_documento(value= ex.verificacionNumerosSTR("ingrese el nuevo documento: "))
    print(instructorContrato.get_documento())
    instructorContrato.set_nombreCompleto(value=ex.verificacionTexto("ingrese el Nombre de la Persona: "))
    print(instructorContrato.get_nombreCompleto())
    instructorContrato.set_profesion(value=ex.verificacionTexto("Ingrese su profesion: "))
    print(instructorContrato.get_profesion())
    instructorContrato.set_salarioBasico(value=ex.solicitar_dato_int("Ingrese el salario del instructor: "))
    print(instructorContrato.get_salarioBasico())
    instructorContrato.contrato(2025,1,15)
    instructorContrato.set_duracionContrato(value= ex.solicitar_dato_int("ingrese cuanto le queda para terminar el  contrato en años(ejemplo: 5 = 5 años)"))
    print(instructorContrato.get_duracionContrato())
    instructorContrato.set_fechaVinculacion(ano=ex.solicitar_dato_int("ingrese el año(0000) cuando se vinculo: "),mes=ex.solicitar_dato_int("ingrese el mes(04): "), dia=ex.solicitar_dato_int("ingrese el dia(00): "))
    print(instructorContrato.get_fechaVinculacion())
    instructorContrato.informacion()
    instructorContrato.estado(2025,5,29)
    instructorContrato.sueldo()
    
    #Revista
    print("\n","-"*40)
    print("Revista")
    revista.set_codigo(value=ex.verificacionNumerosSTR("ingrese el codigo de la revista: "))
    print(revista.get_codigo())
    revista.set_titulo(value=ex.verificacionTexto("ingrese el titulo(solo alfabetico): "))
    print(revista.get_titulo())
    revista.set_autor(value=ex.verificacionTexto("ingrese el nombre del autor: "))
    print(revista.get_autor())
    revista.set_editorial(value=ex.verificacionTexto("ingrese la editorial: "))
    print(revista.get_editorial())
    revista.set_ano(value=ex.verificacionNumerosSTR("ingrese el año de publicación de la revista: "))
    print(revista.get_ano())
    revista.set_precio(value=ex.verificacionNumerosSTR("ingrese el precio de la revista: "))
    print(revista.get_precio())
    revista.set_volumen(value=ex.verificacionNumerosSTR("ingrese el volumen de la revista: "))
    print(revista.get_volumen())
    revista.informacion()
    revista.estado()
    
    #libro
    print("\n","-"*40)
    print("libro")
    libro.set_codigo(value=ex.verificacionNumerosSTR("ingrese el codigo de la libro: "))
    print(libro.get_codigo())
    libro.set_titulo(value=ex.verificacionTexto("ingrese el titulo(solo alfabetico): "))
    print(libro.get_titulo())
    libro.set_autor(value=ex.verificacionTexto("ingrese el nombre del autor: "))
    print(libro.get_autor())
    libro.set_editorial(value=ex.verificacionTexto("ingrese la editorial: "))
    print(libro.get_editorial())
    libro.set_ano(value=ex.verificacionNumerosSTR("ingrese el año de publicación de la libro: "))
    print(libro.get_ano())
    libro.set_precio(value=ex.verificacionNumerosSTR("ingrese el precio del libro: "))
    print(libro.get_precio())
    libro.set_idioma(value=ex.verificacionTexto("ingrese el idioma del libro: "))
    print(libro.get_idioma())
    libro.informacion()
    libro.estado()
    

    #producto Grabado
    print("\n","-"*40)
    print("producto Grabado")
    productoGrabado.set_codigo(value=ex.verificacionNumerosSTR("ingrese el codigo del producto Grabado: "))
    print(productoGrabado.get_codigo())
    productoGrabado.set_titulo(value=ex.verificacionTexto("ingrese el titulo(solo alfabetico): "))
    print(productoGrabado.get_titulo())
    productoGrabado.set_autor(value=ex.verificacionTexto("ingrese el nombre del autor: "))
    print(productoGrabado.get_autor())
    productoGrabado.set_tiempoDuracion(value=ex.solicitar_dato_int("ingrese la duracion en minutos: "))
    print(productoGrabado.get_tiempoDuracion())
    productoGrabado.set_medioTecnologico(value=ex.verificacionTexto("escriba el medio tecnologico: "))
    print(productoGrabado.get_medioTecnologico())
    productoGrabado.informacion()
    """

    #producto software
    print("\n","-"*40)
    print("producto software")
    productoSotfware.set_codigo(value=ex.verificacionNumerosSTR("ingrese el codigo del producto de software: "))
    print(productoSotfware.get_codigo())
    productoSotfware.set_titulo(value=ex.verificacionTexto("ingrese el titulo(solo alfabetico): "))
    print(productoSotfware.get_titulo())
    productoSotfware.set_autor(value=ex.verificacionTexto("ingrese el nombre del autor: "))
    print(productoSotfware.get_autor())
    productoSotfware.set_version(value=input("ingrese la version del producto: "))
    print(productoSotfware.get_version())
    productoSotfware.set_sistemaOperativo(value=ex.solicitar_dato_int("ingrese el sistema operativo: "))
    print(productoSotfware.get_sistemaOperativo())
    productoSotfware.informacion()


