# ZappGroup
Repositorio dedicado a las prácticas de la asignatura Dirección y Gestión de Proyectos ( ETSIIT UGR)

# Instalación
Se puede usar windows o ubuntu. hay que tener instalado anaconda o miniconda. Si queréis ahorrar espacio, usad miniconda, al diferencia es
la cantidad de librerías que vienen ya descargadas. En la terminal de Ubuntu (en windows, abrir la terminal de conda), escribir el siguiente comando:

conda env create -f environment.yml

Poneros en la carpeta donde tengais el fichero environment.yml o cambias la ruta para environment.yml como /mi/carpeta/aqui/environment.yml, es irrelevante.

Si acabas de instalar conda, añade esto al .bashrc (solo ubuntu):
export PATH=~/anaconda3/bin:$PATH

#Ejecución
En el directorio app externo:
python manage.py runserver
