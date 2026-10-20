import time
import os

'''
Curso: Fundamentos de Programación con Python
Módulo 5
Proyecto final
'''


estudiantes_registrados = {2026001: {'nombre': 'Carlos Valdez', 'calificaciones': (96, 95, 94)}
                         , 2026002: {'nombre': 'Juan Gomez', 'calificaciones': (85, 82, 83)}
                         , 2026003: {'nombre': 'Rosalinda Ramirez', 'calificaciones': (78, 74, 73)}
                         , 2026004: {'nombre': 'Jairo Matos', 'calificaciones': (96, 85, 76)}
                         , 2026005: {'nombre': 'Rosa Maríñez', 'calificaciones': (82, 91, 94)}
                         , 2026006: {'nombre': 'Ruth Valdez', 'calificaciones': (26, 35, 77)}
                         , 2026007: {'nombre': 'Lizbeth Alcantara', 'calificaciones': (69, 56, 45)}}



'''
---------------------------------------------------
###################################################
---------------------------------------------------
'''

#Diccionario para guardar temporalmente la información 
#del diccionario anidado de determinada matrícula.
estudiante = {}


#Diccionario que guarda la información de todos los estudiantes.
estudiantes = {}
estudiantes = estudiantes_registrados

'''
---------------------------------------------------
###################################################
---------------------------------------------------
'''


def calcular_promedio(calificaciones: list) -> float:
    promedio = round((sum(calificaciones)/len(calificaciones)),2)
    return promedio

'''
---------------------------------------------------
###################################################
---------------------------------------------------
'''

def estado_estudiante(promedio) -> str:  
    if promedio >= 70:
        estado = "Aprobado"
    elif promedio < 70:
        estado = "Reprobado"
    return estado


'''
---------------------------------------------------
###################################################
---------------------------------------------------
'''

def consultar_matricula(matricula):
    existe = False
    for key in estudiantes.keys():
        if matricula == key:
            existe = True
    return existe
    

'''
---------------------------------------------------
###################################################
---------------------------------------------------
'''

def registrar_estudiante():
    
    registrado = False
    cantidad_calificaciones_por_estudiantes = 3 
    
    while registrado == False:
        
        calificaciones = []
        matricula = 0
        nombre = ""
        estudiante = {}
        
        #Obteniendo la matrícula del estudiante.
        try:
            print("\nFavor digitar la matrícula del estudiante")
            matricula = int(input("> "))
        except:
            print("\nLa matrícula digitada solamente debe contener números. Favor verificar.")
            continue
        else:
            #Verificando si la matrícula ya existe.
            if consultar_matricula(matricula):
                print("\nLa matricula digitada ya estaba registrada. Favor verificar.")
                continue
            
            #Obteniendo el nombre del estudiante.
            print("Favor digitar el nombre del estudiante:")
            nombre = input("> ")
            caracteres_incorrectos_en_nombre = ("0","1","2","3","4","5","6","7","8","9",".","?","%")
            hay_caracteres_incorrectos_en_nombre = any([caracter in nombre  for caracter in caracteres_incorrectos_en_nombre])
            if hay_caracteres_incorrectos_en_nombre:
                print(f"\nEl nombre digitado '{nombre}' contiene algún carácter no válido para un nombre. Favor verificar.")
                continue
            else:
                nombre = nombre.title()
                
            #Obteniendo las calificaciones del estudiante.
            iteracion = 1
            while iteracion <= cantidad_calificaciones_por_estudiantes:
                try:
                    print(f"Favor digitar la Calificación {iteracion}:")
                    calificacion = int(input("> "))
                    if calificacion <= 0 or calificacion > 100:
                        print("La calificación debe ser mayor a cero (0) y menor a 101.")
                        continue
                    else:
                        calificaciones.append(calificacion)
                except:
                    print("Error. Favor verificar la calificación digitada. ")
                    print()
                    continue
                iteracion += 1
                
            promedio = calcular_promedio(calificaciones)
            
            estado = estado_estudiante(promedio)
            
            #Cargando información en diccionario anidado.
            estudiante["nombre"] = nombre
            estudiante["calificaciones"] = tuple(calificaciones)
            
            #Cargando información en diccionario principal.
            estudiantes[matricula] = estudiante
            
            #Mostrar estudiante ingresado.
            print("\n\nEstudiante ingresado:")
            buscar_estudiante(matricula)
            print()
            print("Estudiante registrado correctamente.")
            print()
            
            #Confirmando si se seguirá ingresando estudiantes.
            consultar_continuar_registrando = True
            while consultar_continuar_registrando == True:
                print("\n¿Desea registrar otro estudiante? (si/no)")
                respuesta_continuar_registrando = input("> ")
                if respuesta_continuar_registrando.lower() == "si":
                    consultar_continuar_registrando = False
                    registrado = False 
                elif respuesta_continuar_registrando.lower() == "no":
                    consultar_continuar_registrando = False
                    registrado = True
                else:
                    print("\nRespuesta no válida. Favor verificar.")
                    consultar_continuar_registrando = True
                    registrado = False 

'''
---------------------------------------------------
###################################################
---------------------------------------------------
'''

def mostrar_estudiantes():
    cantidad_estudiantes = 0
    
    if len(estudiantes) == 0:
        print("\nNo hay estudiantes registrados.")
        print()
        
    for matricula in estudiantes.keys():
        if cantidad_estudiantes > 0:
            print("\n---------------\n")
        else:
            print("\n------------------------------\n")
            print("\nESTUDIANTES REGISTRADOS:\n")
                
        buscar_estudiante(matricula)
        cantidad_estudiantes += 1
        print()
        
    print(f"\nEstudiantes registrados: {cantidad_estudiantes}.")    
    print("\n------------------------------\n")

'''
---------------------------------------------------
###################################################
---------------------------------------------------
'''

def buscar_estudiante(matricula):
    estudiante_buscado = estudiantes.get(matricula)
    print()
    print(f"Matrícula: {matricula}")
    #Presentando el nombre y las calificaciones.
    for key, value in estudiante_buscado.items():
        if key == "nombre":
            print(f"Nombre: {value}")
            print()
        elif key == "calificaciones":
            for iteracion in range(3):
                print(f"Calificación {iteracion + 1}: {estudiante_buscado["calificaciones"][iteracion]}")
            print()  
    #Presentando el promedio.        
    calificaciones = list(estudiante_buscado["calificaciones"])        
    promedio = calcular_promedio(calificaciones)        
    print(f"Promedio: {promedio}") 
    #Presentando el estado.
    estado = estado_estudiante(promedio)
    print(f"Estado: {estado}")
    print()

'''
---------------------------------------------------
###################################################
---------------------------------------------------
'''

def mostrar_estudiantes_aprobados():
    cantidad_aprobados = 0
    
    if len(estudiantes) == 0:
        print("\nNo hay estudiantes registrados.")
        print()
        
    for matricula in estudiantes.keys():
        calificaciones = estudiantes[matricula]["calificaciones"]
        promedio = calcular_promedio(calificaciones)
        estado = estado_estudiante(promedio)
        
        if estado == "Aprobado":  
            if cantidad_aprobados > 0:
                print("\n---------------\n")
            else:
                print("\n------------------------------\n")
                print("ESTUDIANTES APROBADOS:\n")
            buscar_estudiante(matricula)
            cantidad_aprobados += 1
        print()
        
    if cantidad_aprobados > 0:
        print(f"\nCantidad de estudiantes aprobados: {cantidad_aprobados}.")
        print("\n------------------------------\n")

'''
---------------------------------------------------
###################################################
---------------------------------------------------
'''

def mostrar_estudiantes_reprobados():
    cantidad_reprobados = 0
    
    if len(estudiantes) == 0:
        print("\nNo hay estudiantes registrados.")
        print()
        
    for matricula in estudiantes.keys():
        calificaciones = estudiantes[matricula]["calificaciones"]
        promedio = calcular_promedio(calificaciones)
        estado = estado_estudiante(promedio)
        
        if estado == "Reprobado": 
            if cantidad_reprobados > 0:
                print("\n---------------\n")
            else:
                print("\n------------------------------\n")
                print("ESTUDIANTES REPROBADOS:\n")
            buscar_estudiante(matricula)
            cantidad_reprobados += 1
        print()
        
    if cantidad_reprobados > 0:
        print(f"\nCantidad de estudiantes reprobados: {cantidad_reprobados}.")
        print("\n------------------------------\n")

'''
---------------------------------------------------
###################################################
---------------------------------------------------
'''

def cantidad_estudiantes_aprobados():
    cantidad_aprobados = 0
    
    for matricula in estudiantes.keys():
        calificaciones = estudiantes[matricula]["calificaciones"]
        promedio = calcular_promedio(calificaciones)
        estado = estado_estudiante(promedio)
        
        if estado == "Aprobado": 
            cantidad_aprobados += 1
            
    return cantidad_aprobados
    
'''
---------------------------------------------------
###################################################
---------------------------------------------------
'''

def cantidad_estudiantes_reprobados():
    cantidad_reprobados = 0
    
    for matricula in estudiantes.keys():
        calificaciones = estudiantes[matricula]["calificaciones"]
        promedio = calcular_promedio(calificaciones)
        estado = estado_estudiante(promedio)
        
        if estado == "Reprobado": 
            cantidad_reprobados += 1
        
    return cantidad_reprobados
    
'''
---------------------------------------------------
###################################################
---------------------------------------------------
'''

def cantidad_estudiantes():
    cantidad = 0
    
    for matricula in estudiantes.keys():
        cantidad += 1
        
    return cantidad
    
    
'''
---------------------------------------------------
###################################################
---------------------------------------------------
'''

def promedio_general_estudiantes_registrados():
    suma_promedios = 0 
    promedio_general = 0
    
    for matricula in estudiantes.keys():
        calificaciones = estudiantes[matricula]["calificaciones"]
        promedio = calcular_promedio(calificaciones)
        suma_promedios += promedio
        
    promedio_general = round( (suma_promedios / len(estudiantes)) ,2)
    
    return promedio_general
    
'''
---------------------------------------------------
###################################################
---------------------------------------------------
'''

def buscar_estudiante_promedio_mas_alto(matricula):
    
    estudiante_buscado = estudiantes.get(matricula)

    for key, value in estudiante_buscado.items():
        if key == "nombre":
            nombre = value
            
    calificaciones = list(estudiante_buscado["calificaciones"])        
    promedio = calcular_promedio(calificaciones)   
    
    print(f"{nombre} - {promedio}") 


'''
---------------------------------------------------
###################################################
---------------------------------------------------
'''

def estudiante_con_promedio_mas_alto():
    suma_promedios = 0 
    promedio_mas_alto = 0
    matricula_promedio_mas_alto = 0
    
    for matricula in estudiantes.keys():
        calificaciones = estudiantes[matricula]["calificaciones"]
        promedio = calcular_promedio(calificaciones)
        
        if promedio > promedio_mas_alto:
            promedio_mas_alto = promedio
            matricula_promedio_mas_alto = matricula
    
    buscar_estudiante_promedio_mas_alto(matricula_promedio_mas_alto)
    
'''
---------------------------------------------------
###################################################
---------------------------------------------------
'''

def mostrar_estadisticas():
        
        if len(estudiantes) == 0:
            
            print("\nNo hay estudiantes registrados.")
            print()
            
        else:
            
            total_estudiantes = cantidad_estudiantes()
            aprobados = cantidad_estudiantes_aprobados()
            reprobados = cantidad_estudiantes_reprobados()
            promedio_general = promedio_general_estudiantes_registrados()
            
            
            print("\n------------------------------")
            
            print(f"\nESTADÍSTICAS DEL GRUPO\n")
            print(f"Total de estudiantes: {total_estudiantes} ")
            print(f"Aprobados: {aprobados}")
            print(f"Reprobados: {reprobados}")
            print(f"Promedio general: {promedio_general}")
            print()
            print("\nMejor promedio:")
            estudiante_con_promedio_mas_alto()
            
            print("------------------------------\n")
            
'''
---------------------------------------------------
###################################################
---------------------------------------------------
'''

def limpiar_pantalla():
    os.system("cls" if os.system == "nt" else "clear")
    

def salir_del_sistema():
        print("\nGracias por utilizar el sistema.")
        time.sleep(4)
        limpiar_pantalla()
        
        
'''
---------------------------------------------------
###################################################
---------------------------------------------------
'''
  
        
while True:
    
    print("\nSISTEMA DE GESTIÓN DE ESTUDIANTES")
    
    print("\n1. Registrar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Buscar estudiante")
    print("4. Mostrar estudiantes aprobados")
    print("5. Mostrar estudiantes reprobados")
    print("6. Mostrar estadísticas")
    print("7. Salir")
    
    print("\nSeleccione una opción:")
    
    try:
        opcion_elegida = int(input("> "))
    except ValueError:
        print("Favor digitar un dígito del 1 al 7.")
        print()
        continue
    except:
        print("Opción no válida.")
        continue

    if opcion_elegida == 1:
        registrar_estudiante()
    elif opcion_elegida == 2:
        print()
        mostrar_estudiantes()
        print()
    elif opcion_elegida == 3:
        while True:
            try:
                print("\nFavor digitar la matrícula: ")
                matricula = int(input())
                break
            except ValueError:
                print("\nSolamente use números, por favor.")
            except:
                print("\nMatrícula incorrecta")
                continue
        if consultar_matricula(matricula):
            buscar_estudiante(matricula)
        else:
            print("\nMatrícula no registrada.")
    elif opcion_elegida == 4:
        mostrar_estudiantes_aprobados()
    elif opcion_elegida == 5:
        mostrar_estudiantes_reprobados()
    elif opcion_elegida == 6:
        mostrar_estadisticas()
    elif opcion_elegida == 7:
        salir_del_sistema()
        break
    else:
        print("Opción no válida.")
        print()

    





'''
---------------------------------------------------
###################################################
---------------------------------------------------
'''







    
    
    
    
    














