import random
import string

LETRAS_MINUSCULAS = string.ascii_lowercase
LETRAS_MAYUSCULAS = string.ascii_uppercase
DIGITOS = string.digits
SIMBOLOS = string.punctuation

def solicitar_opciones():
    while True: 
        try:
            longitud = int(input("Ingrese la longitud deseada para la contraseña (minimo 8, maximo 64): "))
            if 8 <= longitud <= 64:
                break 
            else:
                print("Error: La longitud debe estar entre 8 y 64 caracteres.")
        except ValueError:
            print("Error: Por favor, ingrese solo un número entero.")
    
    usar_mayusculas = input("¿Incluir letras mayúsculas? (s/n): ").strip().lower() == 's'
    usar_numeros = input("¿Incluir números? (s/n): ").strip().lower() == 's'
    usar_simbolos = input("¿Incluir símbolos? (s/n): ").strip().lower() == 's'

    return longitud, usar_mayusculas, usar_numeros, usar_simbolos

def generar_contrasena(longitud, usar_mayusculas, usar_numeros, usar_simbolos):
    caracteres_permitidos = list(LETRAS_MINUSCULAS)
    contrasena_temporal = []

    if usar_mayusculas:
        caracteres_permitidos.extend(LETRAS_MAYUSCULAS)
        contrasena_temporal.append(random.choice(LETRAS_MAYUSCULAS))
    if usar_numeros:
        caracteres_permitidos.extend(DIGITOS)
        contrasena_temporal.append(random.choice(DIGITOS))
    if usar_simbolos:
        caracteres_permitidos.extend(SIMBOLOS)
        contrasena_temporal.append(random.choice(SIMBOLOS))
    
    longitud_restante = longitud - len(contrasena_temporal)

    for _ in range(longitud_restante):
        contrasena_temporal.append(random.choice(caracteres_permitidos))
    
    random.shuffle(contrasena_temporal)
    return "".join(contrasena_temporal)

if __name__ == "__main__":
    print("--- ¡Bienvenido al Generador de Contraseñas Seguras! ---")
    longitud, mayusculas, numeros, simbolos = solicitar_opciones()
    mi_contrasena = generar_contrasena(longitud, mayusculas, numeros, simbolos)
    
    print("\n" + "="*30)
    print("¡Contraseña generada con éxito!")
    print(f"Tu nueva contraseña segura es: {mi_contrasena}")
    print("="*30)