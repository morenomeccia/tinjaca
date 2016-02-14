============================
Procedimiento de Instalación
============================

La instalación de TINJACA requiere, por una parte, instalar Odoo v8 y por la otra los módulos de
TINJACA diseñados para las necesidades del FOMDES.

Es muy recomendable tener dos instancias de Odoo v8 independientes para manejar actividades de
mantenimiento, llamado desarrollo, por una parte, y actividades de manejo del sistema por parte de
sus usuarios, llamado  producción.

A continuación se detalla el proceso de instalación en ambos casos.

--------------------------------------------------------------
Instalación de Odoo para labores de mantenimiento (Desarrollo)
--------------------------------------------------------------

1. Crear una carpeta para el destino de la instalación de Odoo, por ejemplo "proyecto"

2. Clonar el repositorio dentro de la carpeta "proyecto"

.. code-block:: shell

   $ git clone https://github.com/odoo/odoo.git

3. Instalar dependencias

La instalación de Odoo requiere la instalación de dependencias de python de forma manual:

.. code-block:: shell

   $ sudo apt-get install python-psycopg2 libxml2-dev libxslt1-dev python-dev libsasl2-dev
   libjpeg-dev libpng12-dev zlib1g-dev libldap2-dev

4. Instalar PostgreSQL

.. code-block:: shell

   $ sudo apt-get install postgresql-server-dev-9.3 postgresql-9.3 postgresql-client-9.3

5. Creación del usuario de PostgreSQL

.. code-block:: shell

   $ sudo su - postgres -c "createuser -s $USER"

6. Instalar dependencias con pip

Instalar pip

.. code-block:: shell

   $ sudo apt-get install python-pip
   $ sudo pip install --upgrade pip
   $ sudo pip install virtualenvwrapper


Configurar virtualenvwrapper, copiar las siguientes lineas en .bashrc

En el raíz de la carpeta

.. code-block:: shell

   export WORKON_HOME=~/.virtualenvs
   export PROJECT_HOME=~/proyecto
   source /usr/local/bin/virtualenvwrapper.sh

desde la carpeta ~/proyecto

.. code-block:: shell

   mkproject -f odoo

Si ya está creado

.. code-block:: shell

   workon odoo

   $ pip install -r requirements.txt

7. Instalar less

.. code-block:: shell

   $ sudo apt-get install -y npm
   $ sudo ln -s /usr/bin/nodejs /usr/bin/node
   $ sudo npm install -g less less-plugin-clean-css

8. Ejecutar odoo

.. code-block:: shell

   $ chmod u+x odoo.py
   $ ./odoo.py

    8.1 El comando general de inicio del Odoo sería

.. code-block:: shell

   $ ./odoo.py --addons-path=addons,../mymodules --db-filter=mydb$

9. Crear la base de datos

   9.1 Entrar con el navegador web a la dirección

.. code-block:: shell

   http://localhost:8069

    9.2 Si no hay bases de datos creadas va al manejador de bases de datos donde se creará la
    base de datos

.. code-block:: shell

   http://localhost:8069/web/database/manager

---------------------------------
Instalación de módulos de TINJACÁ
---------------------------------

HASTA AQUI

#

------------------------------------------------------------------
Instalación de Odoo para labores rutinarias de FOMDES (Producción)
------------------------------------------------------------------
