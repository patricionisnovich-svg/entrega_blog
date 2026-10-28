from blog.operaciones import listar_posts, mostrar_resultados, buscar_por_titulo, filtrar_por_tag
from blog.validaciones import validar_post
def menu(blog):
    while True:
        print("----MENU DEL BLOG----")
        print("1-ver todos los posts")
        print("2-buscar por titulo")
        print("3-filtrar por tag")
        print("4-validar posts")
        print("5- crear nuevo post")
        print("6-guardar post en JSON")
        print("7-salir")

        try:
            opcion = int(input("Ingresar opcion: "))
        except ValueError:
            print("Opción inválida: ingresá un número.")
            continue

        if opcion == 1:
            listar_posts(blog.posts)
        elif opcion == 2:
            termino = input("Inserte un título: ")
            mostrar_resultados(buscar_por_titulo(blog.posts, termino))
        elif opcion == 3:
            tag = input("Insertar tag: ")
            mostrar_resultados(filtrar_por_tag(blog.posts, tag))
        elif opcion == 4:
            for post in blog.posts:
                estado = "válido" if validar_post(post.to_diccionario()) else "inválido"
                print(f"Post {post.id}: {estado}")
        elif opcion == 5:
            blog.crear_post()
        elif opcion == 6:
            blog.guardar_posts()
            print("Guardando posts en JSON")    
        elif opcion == 7:
            print("Saliendo")
            break
        else:
            print("Opción fuera de rango.")