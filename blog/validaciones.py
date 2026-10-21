from blog.datos import estados_post
def validar_post(post):
    if not isinstance(post, dict):
        return False
    claves_necesarias = ["titulo", "contenido", "autor", "tags", "estado"]
    for clave in claves_necesarias:
        if clave not in post:
            return False
    if post["titulo"] == "":
        return False
    if post["contenido"] == "":
        return False
    if not isinstance(post["autor"], dict):
        return False
    if "nombre" not in post["autor"]:
        return False
    if not isinstance(post["tags"], list):
        return False
    if post["estado"] not in estados_post:
        return False
    return True