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