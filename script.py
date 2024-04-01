import json
from usuario import Usuario

def leer_archivo_usuarios(archivo):
    usuarios = []
    try:
        with open(archivo, 'r') as f:
            for linea in f:
                datos_usuario = json.loads(linea)
                usuario = Usuario(**datos_usuario)
                usuarios.append(usuario)
    except Exception as e:
        print(f"Error al leer linea del archivo: {linea}")
        print(f"Excepcion: {e}")
        with open('error.log', 'a') as f:
            f.write(f"Error al leer linea del archivo: {linea}\n")
            f.write(f"Excepcion: {e}\n")
    return usuarios

def main():
    archivo_usuarios = "usuarios.txt"
    usuarios = leer_archivo_usuarios(archivo_usuarios)
    for usuario in usuarios:
        print(f"Usuario: {usuario.nombre} {usuario.apellido}")
        print(f"Email: {usuario.email}")
        print(f"Género: {usuario.genero}")
        print("---")

if __name__ == "__main__":
    main()