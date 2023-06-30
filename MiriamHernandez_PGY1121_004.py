import random


def valir_opciones(opcion):
    if opcion > 0 and opcion < 5:
        return True
    else:
        return False


def mensaje_selecionar_opcion(mensaje="Debe seleccionar un número entre 1 al 4"):
    print("")
    print("****************************************")
    print("")
    print(mensaje)
    print("")
    print("****************************************")
    print("")


def mensaje_selecionar_opcion_2(mensaje="Debe seleccionar un número entre 1 al 4"):
    print("")
    print("-----------------------------------------")
    print("")
    print(mensaje)
    print("")
    print("-----------------------------------------")
    print("")


def guardar_informacion_alumno():

    validar_rut = bool(True)
    while validar_rut:
        rut = input("Indique rut:\n")
        if len(rut) < 2 and len(rut) > 12:
            mensaje_selecionar_opcion(
                "El rango del rut debe ser entre 2 a 12 caracteres")
            continue

        if rut[-1].upper() != "K" and not rut[-1].isdigit():
            mensaje_selecionar_opcion(
                "El numero digitador debe ser K o un número entre 0 al 9")
            continue

        if rut[-2] != "-":
            mensaje_selecionar_opcion(
                "Debe seguir el siguiente formato xxxxxxx-k")
            continue

        validar_rut = False

    nombre = input("Indique nombre:\n")
    apellido = input("Indique apellido:\n")
    fecha_nacimiento = input("Indique fecha de nacimiento:\n")
    carrera = input("Indique carrera:\n")
    asignatura = input("Indique asignatura:\n")
    validar_promedio = bool(True)
    while validar_promedio:
        try:
            promedio = float(input("Indique promedio:\n"))
            if promedio >= 1.0 and promedio <= 7.0:
                validar_promedio = False
            else:
                mensaje_selecionar_opcion(
                    "El rango del promedio debe ser entre 1.0 al 7.0")

        except Exception as e:
            mensaje_selecionar_opcion(
                "El rango del promedio debe ser entre 1.0 al 7.0")

    alumno = {
        "rut": rut,
        "nombre": nombre,
        "apellido": apellido,
        "fecha_nacimiento": fecha_nacimiento,
        "carrera": carrera,
        "asignatura": asignatura,
        "promedio": promedio,
    }
    alumnos.append(alumno)
    mensaje_selecionar_opcion_2("Alumno registrado con exito")


def buscar_alumno():
    busqueda = str(input('Ingrese el RUT \n'))
    for alumno in alumnos:
        if alumno['rut'] == busqueda:
            return alumno
    return ""


alumnos = []
certificados = {
    "1": {"valor": random.randint(1000, 5000), "nombre": "Alumno regular"},
    "2": {"valor": random.randint(1000, 5000), "nombre": "Notas"},
    "3": {"valor": random.randint(1000, 5000), "nombre": "Matrícula"},
}

menu = """

Opciones:

1) Grabar Información Alumno
2) Buscar Alumno
3) Imprimir certificado
4) Salir

"""

menu_2 = f"""
Seleccione alguna de las opciones de certificado
1) Alumno regular   valor: {certificados["1"]['valor']}
2) Notas            valor: {certificados["2"]['valor']}   
3) Matrícula        valor: {certificados["3"]['valor']}
"""

continuar = bool(True)

while continuar:
    try:
        opcion = int(input(menu))
        if valir_opciones(opcion) == False:
            mensaje_selecionar_opcion()
            continue

        if opcion == 1:
            guardar_informacion_alumno()
        if opcion == 2:
            alumno = buscar_alumno()
            if len(alumno) > 0:
                mensaje_selecionar_opcion_2(alumno)
            else:
                mensaje_selecionar_opcion("No se encontro alumno")

        if opcion == 3:
            alumno = buscar_alumno()
            if len(alumno) > 0:

                validar_opcion = bool(True)
                while validar_opcion:
                    try:
                        opcion_certificado = int(input(menu_2))

                        if opcion_certificado > 0 and opcion_certificado < 4:
                            validar_opcion = False
                        else:
                            mensaje_selecionar_opcion("Opcion invalida")

                    except Exception as e:
                        mensaje_selecionar_opcion("Opcion invalida")

                mensaje = f"""
                Certificado  {certificados[str(opcion_certificado)]['nombre']}.

                Rut     : {alumno['rut']}
                Nombre  : {alumno['nombre']}
                Carrera : {alumno['carrera']}
                """

                if opcion_certificado == 2:
                    mensaje += f"""
                Asignatura  : {alumno['asignatura']}
                Promedio : {alumno['promedio']}
                """

                mensaje_selecionar_opcion_2(mensaje)

            else:
                mensaje_selecionar_opcion("No se encontro alumno")

        if opcion == 4:
            continuar = False
            print("Muchas gracias, que tenga un buen día")

    except Exception as e:
        mensaje_selecionar_opcion()
        continue
