# pasos

python3 -m venv venv

source venv/bin/activate

Asegurarnos que tengamos el interprete del entorno virtual definido 
ctrl + p --> >python interpreter --> seleccionar interprete --> venv (entorno virtual )

pip install pymongo fastapi uvicorn

## crear carpetas
MODELS va a ser el que interactue con la base de datos
models --> sirve para modelar datos o definir que es lo que se estará guardando en nuestra base de datos
schemas --> permite definir que es lo que vamos a recibir en la app y que es lo que vamos a responder (las peticiones)
config --> Configuraciones del proyecto
routes --> definir rutas 

# comienzo

empezamos con app.py acá es donde van a estar todas las funciones moduladas
routes/user.py se encuentran los end-points http