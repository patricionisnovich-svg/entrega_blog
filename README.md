Proyecto base de un blog web desarrollado con Django.
Este repositorio contiene la estructura inicial de un proyecto Django para construir un blog.  
Incluye la configuración base del proyecto y una aplicación llamada `posts`.
Clonar el repositorio:

```bash
git clone https://github.com/patricionisnovich-svg/entrega_blog
```

Entrar a la carpeta del proyecto:
```
cd blog_consola_entregafinal
```

Crear entorno virtual:
python -m venv venv

Activar entorno virtual:
En Windows PowerShell:
```
.\venv\Scripts\Activate.ps1
```

En Linux o macOS:
```
source venv/bin/activate
```

Instalar dependencias:
```
pip install -r requirements.txt
```

Ejecutar el servidor:
```
python manage.py runserver
```

Abrir en el navegador:
http://127.0.0.1:8000/

Aplicaciones
- posts: aplicación inicial para manejar las publicaciones del blog.
