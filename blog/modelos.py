import json as JSON
class autor:
   def  __init__(self, nombre, bio, especialidad):
        self.nombre = nombre
        self.bio = bio
        self.especialidad = especialidad
   def to_diccionario(self):
       return{
           "nombre": self.nombre,
           "bio": self.bio,
           "especialidad": self.especialidad
       }
   @classmethod
   def from_diccionario(cls, diccionario):
       return cls(diccionario["nombre"],diccionario["bio"],diccionario["especialidad"])
class post:
    def __init__(self, id, contenido, tags, estado, titulo,  autor):
        self.id = id
        self.contenido = contenido
        self.tags = tags
        self.estado = estado
        self.titulo = titulo
        self.autor = autor
    def to_diccionario(self):
         return{
             "id": self.id,
             "contenido": self.contenido,
             "tags": self.tags,
             "estado": self.estado,
             "titulo": self.titulo,
             "autor": self.autor.to_diccionario()
         }
    def from_diccionario(cls, diccionario):
        autor_obj = autor.from_diccionario(diccionario["autor"])
        return cls(diccionario["id"], diccionario["contenido"], diccionario["tags"], diccionario["estado"], diccionario["titulo"], autor_obj)
        

class blog:
    def __init__(self):
        self.posts = []
    def listar_posts(self):
        print(post.id)
        print(post.autor)
        print(post.estado)
    def buscar_por_titulo(self, titulo):
        for post in self.posts:
            if post.titulo == titulo:
                return post
    def filtrar_tag(self, tags):
        post_filtrados = []
        for post in self.posts:
            if tags in post.tags:
                post_filtrados.append(post)
            return post_filtrados
    def crear_post(self,post):
        self.posts.append(post)
    def validar_post(self,post):
        if post.estado == "publicado":
            return True
        else:
            return False
    def obtener_los_posts(self):
        return self.posts
    def to_diccionario(self):
        return {
            "lista_posts": [post.to_diccionario() for post in self.posts]
        }
    def from_diccionario(self, diccionario):
        self.posts = [post.from_diccionario(post_dict) for post_dict in diccionario["lista_posts"]]