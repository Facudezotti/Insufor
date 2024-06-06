import interfaz_grafica
import archivos_json
import validacion

def ingresar_atributo():
    atributo = input("Ingrese el atributo: ")
    valido, mensaje = validacion.validar_entrada(atributo)
    if not valido:
        return mensaje
    datos = archivos_json.acceder_archivo()
    datos.append(atributo)
    archivos_json.guardar_archivo(datos)
    return "Atributo ingresado correctamente."

def modificar_atributo():
    datos = archivos_json.acceder_archivo()
    if not datos:
        return "No hay atributos para modificar."
    
    listar_atributos()
    try:
        indice = int(input("Ingrese el índice del atributo a modificar: "))
        if 0 <= indice < len(datos):
            nuevo_valor = input("Ingrese el nuevo valor: ")
            valido, mensaje = validacion.validar_entrada(nuevo_valor)
            if not valido:
                return mensaje
            datos[indice] = nuevo_valor
            archivos_json.guardar_archivo(datos)
            return "Atributo modificado correctamente."
        else:
            return "Índice no válido."
    except ValueError:
        return "Índice debe ser un número entero."

def eliminar_atributo():
    datos = archivos_json.acceder_archivo()
    if not datos:
        return "No hay atributos para eliminar."
    
    listar_atributos()
    try:
        indice = int(input("Ingrese el índice del atributo a eliminar: "))
        if 0 <= indice < len(datos):
            datos.pop(indice)
            archivos_json.guardar_archivo(datos)
            return "Atributo eliminado correctamente."
        else:
            return "Índice no válido."
    except ValueError:
        return "Índice debe ser un número entero."

def listar_atributos():
    datos = archivos_json.acceder_archivo()
    if not datos:
        return "No hay atributos para listar."
    
    for i, atributo in enumerate(datos):
        print(f"{i}. {atributo}")
    return "Listado de atributos completado."

def main():
    while True:
        accion = interfaz_grafica.solicitar_accion()
        if accion == "1":
            resultado = ingresar_atributo()
        elif accion == "2":
            resultado = modificar_atributo()
        elif accion == "3":
            resultado = eliminar_atributo()
        elif accion == "4":
            resultado = listar_atributos()
        elif accion == "5":
            interfaz_grafica.mostrar_mensaje("Saliendo del programa.")
            break
        else:
            resultado = "Acción no válida."
        interfaz_grafica.mostrar_resultado(resultado)

if __name__ == "__main__":
    main()
