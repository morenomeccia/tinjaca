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
       * - Analista de credito
         - Ingresar los datos de la planilla de financiamiento al sistema
         - disponer de esta informacion en el sistema para su futuro uso
       * - Analista de credito
		 

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
       * - Analista Juridico
         - Generar el informe de control previo
         - Su uso en las siguientes fases del proceso de evaluacion de propuestas
       * - Analista Juridico
         - Asignar el valor de "CUMPLE" o "NO CUMPLE" para las garantias
         - Su uso en las siguientes fases del proceso de evaluacion de propuestas


**Analisis Economico**
----------------------

    .. list-table::
       :widths: 40 40 40
       :header-rows: 1

       * - Como
         - Quiero
         - Para
       * - Analista economico
         - Generar el informe de inspeccion (informe tecnico) con registro fotografico
         - Su uso en las siguientes fases del proceso de evaluacion de propuestas
       * - Analista economico
		 - Registrar las minutas que se levantan en campo
		 - Ser incluido en el informe tecnico

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
       * - Jefe del departamento de estadística y auditoría de cobranza
         - Realizar una factura con los datos del usuario, monto aprobado, tasas de interés y cuotas
         - Su posterior uso por Caja
       * - Jefe del departamento de estadística y auditoría de cobranza
		 - Generar un reporte desglosado por niveles de morosidad		
		 - recordar el vencimiento de las cuotas.
       * - Ejecutivo de cobranza
		 - Generar una lista con los beneficiarios que deben visitar por fecha, municipio y sectores cuando existen cuotas vencidas. 
		 - Efectuar el cobro de las cuotas.		
       * - Ejecutivo de cobranza
		 - Filtrar los estados de cuentas por cédula y expediente.
		 - facilitar la busqueda de beneficiarios morosos
       * - Jefe del departamento de estadística y auditoría de cobranza
		 - hacer una exoneracion en el cobro del credito
		 - situaciones especiales de los beneficiarios
       * - Ejecutivo de cobranza
		 - registrar la información de mi labor diaria  
		 - para llevar estadisticas del numero de beneficiarios procesados
       * - Ejecutivo de cobranza
		 - registrar la información sobre los beneficiarios atendidos  
		 - para llevar estadisticas del numero de beneficiarios procesados




**Secretaria Ejecutiva**
------------------------

    .. list-table::
       :widths: 40 40 40
       :header-rows: 1

       * - Como
         - Quiero
         - Para
       * - Secretaria(o) ejecutiva(o)
         - Asignar el estatus de la solicitud de crédito en base a lo discutido en el consejo directivo
         - Dar continuidad al proceso de aprobacion de credito
       * - Secretaria(o) ejecutiva(o)
		 - Realizar la agenda con los casos previamente filtrados 
		 - discutirlos en el consejo directivo. 
       * - Secretaria(o) ejecutiva(o)
		 - Imprimir la lista de asistentes del consejo directivo
		 - que se lleve a cabo el consejo directivo 
       * - Secretaria(o) ejecutiva(o)
		 - realizar el acta del consejo directivo
		 - que se lleve a cabo el consejo directivo 
       * - Secretaria(o) ejecutiva(o)
		 - crear el documento del crédito 
		 - su posterior autenticacion por el beneficiario
       * - Secretaria(o) ejecutiva(o)
		 - aprobar el documento del crédito 
		 - para su posterior autenticacion por el beneficiario 
       * - Secretaria(o) ejecutiva(o)
		 - revocar un credito en los casos en que los cheques no se retiren o los créditos se rechacen por los beneficiarios
		 - 
       * - Secretaria(o) ejecutiva(o)


#. Existe un listado de estaciones para hacer un seguimiento interno de los procesos por los cuales va pasando el expediente y una condición: 

Las letras de cambio de aval con garantía se llevan en el software de ofimática Libre Office Calc. Secretaria ejecutiva y la gerencia de administración no se conectan entre si, por lo que se debe permitir modificar los datos del expediente, ya que por ejemplo los datos del conyugue no son vaciados por información de crédito pero para secretaria ejecutiva son importantes.


**Gerencia de Administracion**
------------------------------

    .. list-table::
       :widths: 40 40 40
       :header-rows: 1

       * - Como
         - Quiero
         - Para
       * - Asesor Administrativo
         - Abrir las cuentas de los usuarios cuyos créditos fueron aprobados
         - Dar continuidad al proceso de aprobacion de credito 
       * - ??????????????????
         - Elaborar los cheques de los usuarios cuyos créditos fueron aprobados
         - Dar continuidad al proceso de aprobacion de credito 
       * - ??????????????????
         - Generar la tabla de amortización de los usuarios cuyos cheques fueron procesados
         - Dar continuidad al proceso de aprobacion de credito 
	   * - Cajero
		 - registrar los pagos de los beneficiarios para la cancelacion de cuotas de los credito
         - para actualizar el estado de cuenta del credito del beneficiario 
		

 se generan los recibos


**Gerencia de Caja**
--------------------

    .. list-table::
       :widths: 40 40 40
       :header-rows: 1

       * - Como
         - Quiero
         - Para
       * - ?????????????????
         - generar un reporte del ingreso diario de caja
         - poder ser visto por el presidente

**Gerencia de Presupuesto**
---------------------------

    .. list-table::
       :widths: 40 40 40
       :header-rows: 1

       * - Como
         - Quiero
         - Para
       * - Jefe de departamento de presupuesto
         - Verificar la disponibilidad presupuestaria para el pago del credito al beneficiario
         - Dar continuidad al proceso de aprobacion de credito 

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


**Presidencia**
---------------

    .. list-table::
       :widths: 40 40 40
       :header-rows: 1

       * - Como
         - Quiero
         - Para
       * - Presidente
         - conocer cuánto fue el ingreso diario de caja 
         - evaluar la recuperacion de fondos por la institucion




Establecieron metas diarias de recuperación, montos mayores a 120 mil se considera que van bien en caso contrario van mal. Este reporte se hace de manera manual y quieren que se vea el monto total en la interfaz del sistema.


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

#. El sistema adaptar la solicitud de requisitos de acuerdo al sector, a los montos y a los rubros.

#. El sistema debe distribuir a los analistas económicos de crédito por municipios y parroquias para realizar las inspecciones con el fin de optimizar los tiempos por los traslados.

#. Deben existir las siguientes categorías para los morosos:

	* A para los solventes
	* B, C, D de acuerdo al número de cuotas vencidas.

#. Deben existir las siguientes categorías para las garantías de los créditos de FOMDES:

	* Aval con letra de cambio (Fiador)
	* Hipoteca
	* Fianza financiera (sociedad de garantías reciprocas)
	* Prenda sin Desplazamiento

#. El informe de control previo debe reflejar datos básicos del expediente, la condición de cumple o no cumple, la observación del analista juridico y el texto de la hipoteca o detalle de la garantía.

#. Debe existir una opción intermedia para aquellos expedientes a los cuales les faltan requisitos del analisis jurídico, como "Cumple condicionado".

#. Para las visitas de inspección se dispone de distintos formatos segun el sector del credito.

#. El sistema debería poder cargar fotografías de inspección con cada expediente de modo que en cualquier instancia de decisión pueda ser visualizada esta información. 

#. El sistema debe aportar el formato de documento de crédito para su protocolización y asi evitar que ese proceso se haga de forma manual.

#. El sistema debe mostrar en cual de las siguientes condiciones se encuentra el expediente: exonerado (en caso de muerte del beneficiario con hijos menores de edad, vaguadas, etc), negado, aprobado, aprobado condicionado, aprobado especial, diferido y revocado. Ademas debe mostrar que documentos le faltan al expediente.

#. Se quiere que cada ejecutivo tenga asignado automáticamente una cierta cantidad de expedientes y filtrarlos por criterios para los reportes en el que se muestren las cuotas que están más próximas a vencerse (de mayor a menor, diferenciadas por colores).

#. Actualizar los pagos de las cuotas de la caja exprés en la base de datos cada 3 meses. 

#. El sistema debe ser capaz de diferenciar entre "deuda vigente" y "deuda vencida".
 
#. Los estados de cuenta deben tener dos campos: un campo denominado "recibo", que guarda la lista de los recibos del expediente que los beneficiarios entregan en físico, por fax o correo y un campo denominado "Seguimiento", el cual guarda un resumen histórico de FOMDES con el beneficiario, es decir si se contactó a través de una visita o una llamada y a qué acuerdo de fecha y pago se llegó.

#. Deben generarse alertas en las fechas próximas en que el beneficiario se compromete a pagar las cuotas vencidas para acompanamiento. 

#. Debe existir un módulo para consultar los depósitos de las cuotas para acompanamiento. 

#. Se desea que el sistema envié mensajes SMS o correos electrónicos a los beneficiarios que caigan en alguna categoría de morosos.

#. Se desea que el sistema genere reportes mensuales del número de seguimientos realizados para utilizarlos como comprobante del trabajo realizado por los analistas.

#. Se desea que el sistema genere "sábanas" de los créditos morosos por municipio que se encuentran en categorías B, C y D para planificar los cobros.

#. El sistema debe contemplar el cambio de las políticas y las tasas de interés para el calculo de las cuotas a corbrar para la recuperacion del credito.

#. Se deben poder efectuar consultas con diferentes filtros en las diferentes oficinas.

#. Los gerentes deben poseer permisos para modificar/corregir datos en el sistema.

#. El nuevo sistema informático debe ser flexible y tener portabilidad para que se ajuste a las nuevas políticas y a las exigencias de cada presidente. Otra característica deseable del nuevo sistema es que sea de fácil mantenimiento.

