import json
from pathlib import Path
ruta_posts = Path(__file__).resolve().parent.parent / "posts.json"

perfil_autor = {
    "nombre": "Ana López",
    "bio": "Desarrolladora web y creadora de contenido sobre programación.",
    "especialidad": "Python y Django",
    "redes_sociales": ["@ana_dev", "@ana_python"]
}

estados_post = ("borrador", "publicado", "archivado")

etiquetas_blog = {"Python", "Django", "Web", "Backend"}

posts = [
    {
        "id": 1,
        "titulo": "Primeros pasos con Python",
        "contenido": "En este post veremos cómo empezar a programar con Python.",
        "autor": perfil_autor,
        "tags": ["Python", "Principiantes"],
        "estado": "publicado"
    },
    {
        "id": 2,
        "titulo": "Que es Django",
        "contenido": "Django es un framework web creado con Python.",
        "autor": perfil_autor,
        "tags": ["Python", "Django", "Web"],
        "estado": "borrador"
    },
    {
        "id": 3,
        "titulo": "Organizando datos con listas",
        "contenido": "Las listas permiten guardar varios elementos en una sola variable.",
        "autor": perfil_autor,
        "tags": ["Python", "Listas"],
        "estado": "archivado"
    },
    {
        "id": 4,
        "titulo": "Post incompleto",
        "autor": perfil_autor,
        "tags": ["Test"],
        "estado": "borrador"
        # sin "contenido" a propósito
    }
]

def cargar_posts():
    try:
        with open(ruta_posts, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        if not isinstance(datos,list) or not all(isinstance(post, dict)for post in datos):
            print("formato invalido")
            return []
        return datos
    except FileNotFoundError:
        print("archivo  no encontrado")
        return []
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON.")
        return []
def guardar_posts(posts):
    with open(ruta_posts, "w", encoding= "utf-8")as archivo:
        json.dump(posts, archivo, indent=4, ensure_ascii=False)

posts= cargar_posts()

