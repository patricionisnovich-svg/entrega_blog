from blog.menu import menu
from blog.modelos import blog

if __name__ =="__main__":
    mi_blog = blog()
    mi_blog.cargar_posts()
    menu(mi_blog)
    



