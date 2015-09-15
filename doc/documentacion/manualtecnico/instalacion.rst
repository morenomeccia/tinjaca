****************************
Procedimiento de Instalación
****************************

La instalación de TINJACA requiere instalar Odoo v8 y los módulos de TINJACA diseñados para las
necesidades del FOMDES.

Es muy recomendable tener dos instancias de Odoo v8 independientes para manejar actividades de
mantenimiento, llamado desarrollo, por una parte, y actividades de manejo del sistema por parte de
sus usuarios, llamado  producción.

A continuación se detalla el proceso de instalación en ambos casos.

--------------------------------------------------------------
Instalación de Odoo para labores de mantenimiento (Desarrollo)
--------------------------------------------------------------

# 1 Crear una carpeta para el destino de la instalación de Odoo, por ejemplo "proyecto"

# 2 Clonar el repositorio dentro de la carpeta "proyecto"

    $ git clone https://github.com/odoo/odoo.git

# 3 Instalar dependencias

La instalación de Odoo requiere la instalación de dependencias de python de forma manual:


$ sudo apt-get install python-psycopg2 libxml2-dev libxslt1-dev python-dev libsasl2-dev libjpeg-dev libpng12-dev zlib1g-dev libldap2-dev

# 4 Instalar PostgreSQL

$ sudo apt-get install postgresql-server-dev-9.3 postgresql-9.3 postgresql-client-9.3

# 5 Creación del usuario de PostgreSQL

$ sudo su - postgres -c "createuser -s $USER"

# 6 Instalar dependencias con pip

## Instalar pip

$ sudo apt-get install python-pip
$ sudo pip install --upgrade pip
$ sudo pip install virtualenvwrapper

## Configurar virtualenvwrapper, copiar las siguientes lineas en .bashrc

## En el raíz de la carpeta

export WORKON_HOME=~/.virtualenvs
export PROJECT_HOME=~/proyecto
source /usr/local/bin/virtualenvwrapper.sh

## desde la carpeta ~/proyecto
mkproject -f odoo

## Si ya está creado
workon odoo

$ pip install -r requirements.txt

# Instalar less

$ sudo apt-get install -y npm
$ sudo ln -s /usr/bin/nodejs /usr/bin/node
$ sudo npm install -g less less-plugin-clean-css

# Ejecutar odoo

$ chmod u+x odoo.py
$ ./odoo.py

## El comando general de inicio del Odoo sería
$ ./odoo.py --addons-path=addons,../mymodules --db-filter=mydb$

# Crear la base de datos

## Entrar con el navegador web a la dirección
http://localhost:8069

## Si no hay bases de datos creadas va al manejador de bases de datos
## donde se creará la base de datos

http://localhost:8069/web/database/manager

---------------------------------
Instalación de módulos de TINJACÁ
---------------------------------

#

------------------------------------------------------------------
Instalación de Odoo para labores rutinarias de FOMDES (Producción)
------------------------------------------------------------------
