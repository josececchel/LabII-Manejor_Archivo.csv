import csv
nueva_ejecucion = True

while nueva_ejecucion :
    try:
        
        comando=input("SI USTED QUIERE OBTENER UN LISTADO DE LOS USUARIOS HABILITADOS ESCRIBA SI, PARA SALIR INGRESE NO -->   ")
        if comando.upper() == "NO":
            print("NOS VEMOS LUEGO :) ")
            break
        elif comando.upper() == "SI":
            with open("archivo.csv", "r") as archivo:
                datos = archivo.readlines()
                for i in datos:
                    datosusuarios = i.strip().split(",")
                    nombre,apellido,dni,correo,pasword,estado = datosusuarios
                    if estado == "1" :
                        
                        tiene_minuscula = 0
                        tiene_mayuscula = 0
                        tiene_numeros = 0
                        for p in pasword:
                            if p.isupper():
                                tiene_mayuscula += 1
                                
                            elif p.islower():
                                tiene_minuscula += 1
                                
                            elif p.isdigit():
                                tiene_numeros += 1
                                
                        if tiene_minuscula >= 1 and tiene_mayuscula > 1 and tiene_numeros > 4:
                            print(f"Usuario habilitado:{nombre}, su correo es:{correo}, su pasword es fuerte")
                        else: 
                            print(f"Usuario habilitado: {nombre}, su correo es: {correo}, su pasword es débil")
        else:
            opcion = input("CARACTER INGRESADO NO VALIDO, ¿QUIERE VOLVER A INTENTARLO?, PARA VOLVER A INTENTARLO INGRESE SI, PARA SALIR INGRESE NO:   ")
            if opcion.upper() == "SI":
                nueva_ejecucion = True
            elif opcion.upper() == "NO":
                print("NOS VEMOS LUEGO")
                nueva_ejecucion = False
    except FileNotFoundError:
        print("EL ARCHIVO NO SE HA ENCONTRADO")
    except ValueError:
        print("ERROR EN VALOR INGRESADO, INGRESE SOLAMENTE LOS CARACTERES SOLICITADOS")
    except Exception:
        print("ERROR ENCONTRADO, REINICIE EL SISTEMA")
