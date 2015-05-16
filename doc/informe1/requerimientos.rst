**************
Requerimientos
**************

A continuación se presentan las historias de ususarios identificadas para los procesos del FOMDES en lo relativo a la asignación, acompañamiento y recuperación de los créditos, basadas en la información recolectada en las entrevistas con los trabajadores.

Historias de usario
===================

**Usuario**
-----------

	.. list-table::
		:widths: 40 40 40
		:header-rows: 1

		* - Como
		  - Quiero
		  - Para
		* - Usuario
		  - Crear mi cuenta de usuario en linea
		  - Registrarme en el sistema
		* - Usuario
		  - Editar mis datos personales, direcciones y teléfonos en linea
		  - Actualizar mi informacion en el sistema
		* - Usuario
		  - Consultar el estado de mis solicitudes en linea
		  - Conocer el progreso de mis solicitudes
		* - Usuario
		  - Consultar el estados de cuenta de mis creditos en linea
		  - Conocer mi solvencia en la institucion
		* - Usuario
		  - Efectuar pagos en línea (con TDC) en linea
		  - Cancelar mas facilmente mis deudas con la institucion  

* Las cuentas de usuario invitado pueden tener uno o mas expedientes asociados y una fecha de vencimiento inicial de dos meses que en ultima instancia coincida con la fecha de liberación del crédito, pudiendo reactivarse en caso de nuevas solicitudes.


**Atencion al Ciudadano**
-------------------------

	.. list-table::
		:widths: 40 40 40
		:header-rows: 1

		* - Como
		  - Quiero
		  - Para
		* - Recepcionista
		  - Registrar los datos del vistante, fecha, hora y destino
		  - Utilizar la informacion en el futuro y en otras dependencias
		* - Recepcionista
		  - Consultar la informacion del estatus de la solcitud del usuario
		  - Suministrarla al solicitante
		* - Recepcionista
		  - Consultar la informacion del estado de cuenta del beneficiario
		  - Suministrarla al solicitante
		* - Recepcionista
		  - Generar reportes de los visitantes por rango de fecha
		  - Conocer el numero de visiantes en ese rango o los datos de los visitantes
		* - Recepcionista
		  - Generar reportes de los visitantes por su cedula
		  - Conocer su historial de visitas
		* - Recepcionista
		  - Generar colas por orden de atención y por dependencia
		  - Controlar el orden de atencion de los visitantes dentro de la institucion

**Gerencia de Crédito**
-----------------------

    .. list-table::
       :widths: 40 40 40
       :header-rows: 1

       * - Como
         - Quiero
         - Para
       * - gerente de credito
         - modificar las tasas de interés y los montos asignados por sector, rubro o garantía
         - atender los cambios en las politicas de financiamiento
	   * - Gerente de credito
		 - Seleccionar los proyectos que van al consejo directivo 
		 - Su posterior aprobación o negación.
	   * - Gerente de credito
		 - Generar una cola de rezagados en caso de que se termine el presupuesto pautado 
		 - Que estos rezagados pasan a ser los primeros en la cola del año siguiente
	   * - Gerente de credito
		 - Realizar reportes por municipio, por rubro, por estatus y por rango de fechas 
		 - Generar información estadística		


	

**Ciencia y Tecnologia**
------------------------

    .. list-table::
       :widths: 40 40 40
       :header-rows: 1

       * - Como
         - Quiero
         - Para
       * - a
         - b
         - c

**Informacion de Crédito**
---------------------------

    .. list-table::
       :widths: 40 40 40
       :header-rows: 1

       * - Como
         - Quiero
         - Para
       * - a
         - b
         - c

**Estadiatica y analisis de riesgo**
------------------------------------

    .. list-table::
       :widths: 40 40 40
       :header-rows: 1

       * - Como
         - Quiero
         - Para
       * - a
         - b
         - c

**Analisis Juridico**
---------------------

    .. list-table::
       :widths: 40 40 40
       :header-rows: 1

       * - Como
         - Quiero
         - Para
       * - a
         - b
         - c

**Analisis Economico**
----------------------

    .. list-table::
       :widths: 40 40 40
       :header-rows: 1

       * - Como
         - Quiero
         - Para
       * - a
         - b
         - c

**Gerencia de Acompanamiento**
------------------------------

    .. list-table::
       :widths: 40 40 40
       :header-rows: 1

       * - Como
         - Quiero
         - Para
       * - a
         - b
         - c


**Gerencia de Recuperaciones**
------------------------------

    .. list-table::
       :widths: 40 40 40
       :header-rows: 1

       * - Como
         - Quiero
         - Para
       * - a
         - b
         - c

**Secretaria Ejecutiva**
------------------------

    .. list-table::
       :widths: 40 40 40
       :header-rows: 1

       * - Como
         - Quiero
         - Para
       * - a
         - b
         - c

**Gerencia de Administracion**
------------------------------

    .. list-table::
       :widths: 40 40 40
       :header-rows: 1

       * - Como
         - Quiero
         - Para
       * - a
         - b
         - c

**Gerencia de Caja**
--------------------

    .. list-table::
       :widths: 40 40 40
       :header-rows: 1

       * - Como
         - Quiero
         - Para
       * - a
         - b
         - c

**Gerencia de Presupuesto**
---------------------------

    .. list-table::
       :widths: 40 40 40
       :header-rows: 1

       * - Como
         - Quiero
         - Para
       * - a
         - b
         - c

**Gerencia de Sistemas**
------------------------

    .. list-table::
       :widths: 40 40 40
       :header-rows: 1

       * - Como
         - Quiero
         - Para
       * - a
         - b
         - c


Requerimientos
==============

#. TINJACÁ debe contemplar tres tipos de usuarios:

	* Los funcionarios administradores según sus jerarquías (tipo súper usuario).
    * Los funcionarios operadores según sus cargos y ubicación administrativa (tipo usuario).
    * El público en general (tipo invitado).


#. Los beneficiarios deben poder utilizar la interfaz web del sistema para:

	* Efectuar pagos en línea (con TDC)
	* Registrar los pagos efectuados mediante transferencia o depósito y recibir físicamente del comprobante.

#. Las cuentas de usuario pueden tener uno o mas expedientes asociados y una fecha de vencimiento inicial de dos meses que en ultima instancia coincida con la fecha de liberación del crédito, pudiendo reactivarse en caso de nuevas solicitudes.

#. La inserción de información estará distribuida entre las herramientas web y las disponibles en la institución; igualmente debe ser utilizada de forma eficiente.

#. Se sugiere que el sistema adapte la solicitud de requisitos de acuerdo al sector, a los montos y a los rubros.




