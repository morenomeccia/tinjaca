****************************
Procedimiento de Instalación
****************************

# 1 Clonar el repositorio dentro de la carpeta "projects"
git clone https://github.com/odoo/odoo.git

# 2 Instalar dependencias
sudo apt-get install postgresql-server-dev-9.3 postgresql-9.3 python-psycopg2 libxml2-dev libxslt1-dev python-dev libsasl2-dev libjpeg-dev libpng12-dev zlib1g-dev libldap2-dev


$ sudo su - postgres -c "createuser -s $USER"

# Instalar dependencias con pip
## Instalar pip
$ sudo apt-get install python-pip
$ sudo pip install --upgrade pip
$ sudo pip install virtualenvwrapper

## Configurar virtualenvwrapper, copiar las siguientes lineas en .bashrc
## en el raíz de la carpeta
export WORKON_HOME=~/.virtualenvs
export PROJECT_HOME=~/projects
source /usr/local/bin/virtualenvwrapper.sh

## desde la carpeta ~/projects
mkproject -f odoo
## Si ya está creado
workon odoo

$ pip install -r requirements.txt (tuve problemas en descargar un modulo)

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