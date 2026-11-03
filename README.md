#proyecto de blog
Este proyecto muestra un blog creado como entrega final de un trabajo de python
Permite:
1) ver todos los posts
2) buscar por un determinado titulo
3) filtrar por el tag deseado
4) validar un determinado post o un post recien creado por el lector
5) crear nuevo post
6) guardar post en JSON
7) salir
#en cuanto a la ejecucion, se ejecuta desde la carpeta main.py, mediante el mando en la terminal:
python main.py
respecto a la actividad anterior se agrego un nuevo archivo llamado modelos orientado a objetos y cuestiones relacionadas a la persistencia en JSON para que los nuevos posts se puedan guardar en posts json

Proyecto base de un blog web desarrollado con Django.
Este repositorio contiene la estructura inicial de un proyecto Django para construir un blog.  
Incluye la configuración base del proyecto y una aplicación llamada `posts`.
Clonar el repositorio:

```bash
git clone URL_DEL_REPOSITORIO
```

Entrar a la carpeta del proyecto:
```
cd NOMBRE_DEL_REPOSITORIO
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
