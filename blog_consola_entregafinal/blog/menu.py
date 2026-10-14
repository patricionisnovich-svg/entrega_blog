from blog.operaciones import listar_posts, mostrar_resultados, buscar_por_titulo, filtrar_por_tag
from blog.validaciones import validar_post
from blog.datos import posts
def menu():
    while True:
        print("----MENU DEL BLOG----")
        print("1-ver todos los posts")
        print("2-buscar por titulo")
        print("3-filtrar por tag")
        print("4-validar posts")
        print("5-salir")

        try:
            opcion = int(input("Ingresar opcion: "))
        except ValueError:
            print("Opción inválida: ingresá un número.")
            continue

        if opcion == 1:
            listar_posts(posts)
        elif opcion == 2:
            termino = input("Inserte un título: ")
            mostrar_resultados(buscar_por_titulo(posts, termino))
        elif opcion == 3:
            tag = input("Insertar tag: ")
            mostrar_resultados(filtrar_por_tag(posts, tag))
        elif opcion == 4:
            for post in posts:
                estado = "válido" if validar_post(post) else "inválido"
                print(f"Post {post.get('id', '?')}: {estado}")
        elif opcion == 5:
            print("Saliendo")
            break
        else:
            print("Opción fuera de rango.")