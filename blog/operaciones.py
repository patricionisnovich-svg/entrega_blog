
from blog.modelos import post, autor
from blog.datos import estados_post

def listar_posts(lista):
    print("Lista de posts")
    for post in lista:
        titulo = post.get("titulo", "(sin título)")
        nombre = post.get("autor", {}).get("nombre", "(sin autor)")
        print(f"{titulo}: {nombre}")


def buscar_por_titulo(lista, termino):
    termino = termino.lower().strip()
    resultados = []
    for post in lista:
        if termino in post.get("titulo", "").lower():
            resultados.append(post)
    return resultados


def filtrar_por_tag(lista, tag):
    tag = tag.lower().strip()
    resultados = []
    for post in lista:
        tags_post = [t.lower() for t in post.get("tags", [])]
        if tag in tags_post:
            resultados.append(post)
    return resultados

def mostrar_resultados(resultados):
    if not resultados:
        print("Sin resultados.")
        return
    for post in resultados:
        print(f"- {post.get('titulo', '(sin título)')} {post.get('tags', [])}")


def crear_post(blog):
    titulo = input("ingrese titulo del post: ").strip()
    contenido = input("ingrese contenido del post: ").strip()
    estado = input("ingrese estado del post: ").strip().lower()
    tags = input("ingrese tags del post separados por coma: ").strip().split(",")

    if estado not in estados_post:
        print("estado invalido")
        return
    if not titulo or not contenido:
        print("titulo y contenido son obligatorios")
        return

    nombre = input("ingrese nombre del autor: ").strip()
    bio = input("ingrese bio del autor: ").strip()
    especialidad = input("ingrese especialidad del autor: ").strip()

    autor_nuevo = autor(nombre, bio, especialidad)
    nuevo_id = max((p.id for p in blog.posts), default=0) + 1
    nuevo_post = post(nuevo_id, contenido, tags, estado, titulo, autor_nuevo)

    blog.agregar_post(nuevo_post)
    print("Post creado exitosamente")

