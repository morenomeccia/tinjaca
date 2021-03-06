﻿***************
Diseño de Datos
***************

La estructura y modelado de datos del sistema TINJACA se realizó a partir de los formatos y planillas que utilizan las
diferentes gerencias y dependencias del FOMDES, así como las que son incorporadas en los expedientes en las diferentes
fases del crédito. La información contenida en dichas planillas se incluyen en el Apéndice del presente informe.


Modelo de Datos
===============

El modelo de datos del sistema Tinjacá está centrado en los **Créditos** ya que sus actividades se centran en la
actualidad en el otorgamiento de los créditos y su recuperación.

Los procesos se inician en por uno de los **Solicitantes** el cual está relacionado a una de las **Unidades
Productivas** que realizan cada una, una de las **Actividades Productivas** en virtud de la cual solicita el crédito.

Para efectos legales se requieren los datos de su **Cónyugue** si la tiene y de un **Avalista** si lo requiere.

Tanto de cada uno de los **Solicitantes** como de su respectivo avalista se necesitan uno o mas requisitos como
**Referencias Personales**, **Activos Fijos** y **Cuentas Bancarias** que permitan constatar su solvencia financiera y
capacidad de pago.

El **Solicitante** busca acceder al crédito a través de la **Unidad Productiva**, sujeto cada uno a uno de los **Planes
Inversión**.

Los solicitantes introducen **Propuestas**, y una vez superen un revisión de factibilidad son invitados una o mas veces a los **Talleres** que se
planifican regularmente para una cierta cantidad de **Propuestas**. La invitación a los **Talleres**
incluye una lista de requisitos a consignar. Para ello debe crearse una **Solicitud** formal en FOMDES junto con la exposición de motivos en uno de sus formatos permitidos.

Durante el proceso de aprobación del crédito. El solicitante debe consignar una serie de **Requisitos Personales**,
**Requisitos Empresa** relativos a la **Unidad Productiva**, **Requisitos Sector** propios de cada sector productivo y
**Requisitos Garantía** relacionados con la Garantía utilizada en la **Solicitud**.

Una vez consignados los requisitos se verifica una o mas veces si cumple el **Controles Previos** que realizan los
Analistas Jurídicos, y se realiza una o mas veces la **Inspecciones** e **Inspecciones de Avalúo** que realizan los
Analistas Económicos.

Las **Solicitudes** esperan las **Decisiones Consejo Directivo** para ser aprobados (o no), en cada Consejo
Directivo se delibera sobre uno o mas **Solicitudes**, y una solicitud de crédito podría requerir una o mas **Decisiones
Consejo Directivo** para ser aprobados.

La aprobación de estos **Créditos** está sujeta a las disponibilidades financieras y presupuestarias en relación a los
**Presupuestos** anuales, y la disponibilidad en las **Cuentas Bancarias**.

Una vez aprobados, para cada uno de los **Créditos** se realizan las **Liquidaciones** en una o mas partes. Y esto
activa las **Visitas de Acompañamiento** realizadas por personal de la Gerencia de Crédito para verificar el
cumplimiento de su plan de inversión, y las **Visitas de Cobranza** realizadas por el personal de la Gerencia de
Recuperaciones para recoger pagos, en particular de los **Solicitantes** morosos.

Estas visitas requieren la elaboración de un calendario de **Rutas Acompañamiento** y **Rutas Cobranza** para las cuales
se asignan funcionarios a distintos municipios del Estado Mérida.

Para cada uno de los **Créditos** se reciben **Pagos** hasta su cancelación total.

Si bien las transacciones que generan asientos contables como las **Liquidaciones** o los **Pagos** son relativamente
simples, implementar la contabilidad requeriría la incluir todos los gatos operativos de FOMDES incluyendo la nómina.

----

.. image:: _static/tinjacaER.png
   :alt: Modelo de Datos Tinjacá

*Modelo de Datos del Sistema Tinjacá*

----

Diccionario de Datos
====================

.. index:: !Solicitantes, Beneficiarios

Solicitantes
------------

    .. tabularcolumns:: |p{4cm}|p{7cm}|

    .. list-table::
       :widths: 40 70
       :header-rows: 1

       * - | Campo
         - | Tipo de dato
       * - Código
         - Numérico
       * - Nombres
         - Cadena
       * - Apellidos
         - Cadena
       * - CI
         - Numérico
       * - RIF
         - AlfaNumérico
       * - Fecha_Nacimiento
         - Fecha
       * - Edad
         - Numérico
       * - Sexo
         - Carácter
       * - Dirección_Habitación
         - Cadena
       * - Municipio
         - Cadena
       * - Parroquia
         - Cadena
       * - Profesión_Oficio
         - Cadena
       * - Teléfono_Fijo
         - Cadena
       * - Teléfono_Celular
         - Cadena
       * - Correo_Electrónico
         - Cadena


.. index:: !Unidades Productivas

Unidades Productivas
--------------------

    .. list-table::
       :widths: 40 70
       :header-rows: 1

       * - | Campo
         - | Tipo de dato
       * - Código
         - Numérico
       * - Nombre_Unidad_Productiva
         - Cadena
       * - Dirección_UP
         - Cadena
       * - Teléfono_Fijo
         - Numérico
       * - Teléfono_Celular
         - Numérico
       * - Actividad
         - Cadena
       * - Experiencia
         - Cadena
       * - Área_Geográfica
         - Cadena
       * - Área_Funcionamiento
         - Numérico
       * - Tenencia
         - Cadena
       * - Área_M2
         - Numérico
       * - Zona_Geográfica
         - Cadena
       * - Servicios
         - Cadena
       * - Código_Solicitante
         - Numérico


.. index:: !Actividad Productiva

Actividad Productiva
--------------------

    .. list-table::
       :widths: 40 70
       :header-rows: 1

       * - | Campo
         - | Tipo de dato
       * - Código
         - Numérico
       * - Producto_Derivado
         - Cadena
       * - Materia_Prima
         - Cadena
       * - Donde_Y_Como_obtiene_MP
         - Cadena
       * - Precio_Venta_Producto
         - Numérico
       * - Distribución_Sistema _Ventas
         - Cadena
       * - Numero_de _Trabajadores
         - Numérico
       * - Puestos_Trabajo_Generar
         - Numérico
       * - Observaciones
         - Cadena
       * - Código_UnidadProductiva
         - Numérico
       * - Código_Propuesta
         - Numérico


.. index:: !Planes de Inversión

Planes Inversión
----------------

    .. list-table::
       :widths: 40 70
       :header-rows: 1

       * - | Campo
         - | Tipo de dato
       * - Código
         - Numérico
       * - Capital_de_trabajo
         - Cadena
       * - Materia_Prima
         - Cadena
       * - Mano_de_Obra
         - Numérico
       * - Gastos_de_Constitución
         - Numérico
       * - Inversiones_Fijas
         - Cadena
       * - Ampliación_o_Remodelación
         - Cadena
       * - Maquinaria
         - Cadena
       * - Equipo
         - Numérico
       * - Utensilios_herramientas_menores
         - Cadena
       * - Otros
         - Cadena
       * - Inversión_Total
         - Cadena
       * - Consigno_facturas
         - Lógico
       * - Observaciones
         - Cadena
       * - Código_ActividadProductiva
         - Numérico
       * - Código_Propuesta
         - Numérico


.. index:: !Cónyuges

Cónyuges
--------

    .. list-table::
       :widths: 40 70
       :header-rows: 1

       * - | Campo
         - | Tipo de dato
       * - Código
         - Numérico
       * - Cedula_Identidad
         - Cadena
       * - Nombres
         - Cadena
       * - Apellidos
         - Cadena
       * - Nacionalidad
         - Numérico
       * - Estado_Civil
         - Numérico
       * - Grado_Instrucción
         - Cadena
       * - Condición_Vivienda
         - Cadena
       * - Dirección_Habitación
         - Cadena
       * - Municipio
         - Numérico
       * - Teléfono_Habitación
         - Cadena
       * - Teléfono_Celular
         - Cadena
       * - FAX
         - Cadena
       * - Correo_Electrónico
         - Cadena
       * - Observaciones
         - Cadena
       * - Código_Solicitante
         - Numérico


.. index:: !Referencias Personales

Referencias personales y familiares
-----------------------------------

    .. list-table::
       :widths: 40 70
       :header-rows: 1

       * - | Campo
         - | Tipo de dato
       * - Código
         - Numérico
       * - Cedula_Identidad
         - Cadena
       * - Nombres
         - Cadena
       * - Apellidos
         - Cadena
       * - Dirección_Habitación
         - Cadena
       * - Municipio
         - Numérico
       * - Teléfono_Habitación
         - Cadena
       * - Teléfono_Celular
         - Cadena
       * - Código_Solicitante
         - Numérico


.. index:: !Avalistas

Avalistas
---------

    .. list-table::
       :widths: 40 70
       :header-rows: 1

       * - | Campo
         - | Tipo de dato
       * - Código
         - Numérico
       * - Cedula_Identidad
         - Numérico
       * - Nombres
         - Cadena
       * - Apellidos
         - Cadena
       * - Dirección_Habitación
         - Cadena
       * - Teléfono_Fijo
         - Numérico
       * - Teléfono_Celular
         - Numérico
       * - Nombre_Dirección_Trabajo
         - Cadena
       * - Cargo
         - Cadena
       * - Ingreso_Mensual
         - Numérico
       * - Otros_Ingresos
         - Numérico
       * - Total_Ingresos
         - Numérico
       * - Código_Propuesta
         - Numérico


.. index:: Avalistas, Cuentas Bancarias

Cuentas Bancarias Avalista
--------------------------

    .. list-table::
       :widths: 40 70
       :header-rows: 1

       * - | Campo
         - | Tipo de dato
       * - Código
         - Numérico
       * - Nro_Cuenta
         - Numérico
       * - Nombre_Banco
         - Cadena
       * - Tipo_Cuenta
         - Cadena
       * - Monto
         - Numérico
       * - Código_Avalista
         - Numérico


.. index:: Avalista, Activos Fijos

Activos fijos Avalista
----------------------

    .. list-table::
       :widths: 40 70
       :header-rows: 1

       * - | Campo
         - | Tipo de dato
       * - Código
         - Numérico
       * - Activo
         - Cadena
       * - Titulo
         - Cadena
       * - Avaluo
         - Numérico
       * - Código_Avalista
         - Numérico


.. index:: !Talleres

Talleres
--------

    .. list-table::
       :widths: 40 70
       :header-rows: 1

       * - | Campo
         - | Tipo de dato
       * - Código
         - Numérico
       * - Fecha_Taller
         - Fecha
       * - Funcionario
         - Cadena


.. index:: !Garantías

Garantías
---------

    .. list-table::
       :widths: 40 70
       :header-rows: 1

       * - | Campo
         - | Tipo de dato
       * - Código
         - Numérico
       * - Nro_Expediente
         - AlfaNumérico
       * - Tipo_Garantía
         - Cadena
       * - Descripcion
         - Cadena
       * - Avaluo
         - Numérico
       * - Código_Propuesta
         - Numérico


.. index:: !Requisitos, Requisitos Personales

Requisitos personales
---------------------

    .. list-table::
       :widths: 40 70
       :header-rows: 1

       * - | Campo
         - | Tipo de dato
       * - Código
         - Numérico
       * - Carta_Residencia
         - Binario
       * - Documento_Propiedad_Alquiler
         - Binario
       * - Croquis_Ubicacion
         - Binario
       * - Exposicion_Motivos
         - Binario
       * - Registro_Comercio_RIF
         - Binario
       * - Permisos_Funcionamiento
         - Binario
       * - Código_Solicitud
         - Numérico


.. index:: !Requisitos, Requisitos Empresa

Requisitos Empresa
------------------

    .. list-table::
       :widths: 40 70
       :header-rows: 1

       * - | Campo
         - | Tipo de dato
       * - Código
         - Numérico
       * - Estado_Financiero_2_Ultimos_Años
         - Binario
       * - Balance_Comprobacion
         - Binario
       * - Solvencia_Laboral
         - Binario
       * - Solvencia_SS
         - Binario
       * - Solvencia_INCES
         - Binario
       * - Solvencia_BANAVIH
         - Binario
       * - Código_Solicitud
         - Numérico


.. index:: !Requisitos, Requisitos Sector

Requisitos Sector
-----------------

    .. list-table::
       :widths: 40 70
       :header-rows: 1

       * - | Campo
         - | Tipo de dato
       * - Código
         - Numérico
       * - Permiso_Sanidad
         - Binario
       * - Permiso_Ambiente
         - Binario
       * - Permiso_Alcaldia
         - Binario
       * - Permiso_Bomberos
         - Binario
       * - Permiso_Sanidad
         - Binario
       * - Permiso_Otro
         - Binario
       * - Código_Solicitud
         - Numérico


.. index:: !Requisitos, Requisitos Garantía

Requisitos Garantía
-------------------

    .. list-table::
       :widths: 40 70
       :header-rows: 1

       * - | Campo
         - | Tipo de dato
       * - Código
         - Numérico
       * - Certificacion_Ingresos_Constancia_trabajo
         - Cadena
       * - Avaluo_Bien_Mueble
         - Numérico
       * - Seguro_Bien_Mueble
         - Cadena
       * - Documento_Propiedad_Bien_Mueble
         - Cadena
       * - Croquis_Ubicación
         - Cadena
       * - Levantamiento_Topográfico
         - Cadena
       * - Cedula_Identidad_Socio_Conyuge
         - Numérico
       * - Inscripcion_Sogampi
         - Cadena
       * - Carta_Fianza
         - Cadena
       * - Documento_Crédito_Notariado
         - Cadena
       * - Fianza_Financiera_Notariado
         - Cadena
       * - Firma
         - Imagen
       * - Código_Solicitud
         - Numérico


.. index:: !Consejo Directivo

Consejo directivo
-----------------

    .. list-table::
       :widths: 40 70
       :header-rows: 1

       * - | Campo
         - | Tipo de dato
       * - Código
         - Numérico
       * - Consejo_Directivo_Nro
         - Numérico
       * - Consejo_Directivo_Fecha
         - Fecha
       * - Hora_Consejo_Directivo
         - Hora
       * - Miembros_Consejo_Directivo
         - Cadena
       * - Nro_Expediente
         - AlfaNumérico
       * - Razon_Social
         - Cadena
       * - Estatus_Decisión
         - Cadena
       * - Plan_Inversion
         - Numérico
       * - Firma
         - Imagen


.. index:: !Control Previo

Control Previo
--------------

    .. list-table::
       :widths: 40 70
       :header-rows: 1

       * - | Campo
         - | Tipo de dato
       * - Código
         - Numérico
       * - Código_Analisis_Juridico
         - AlfaNumérico
       * - Descripcion_Garantía
         - Cadena
       * - Estatus_Analisis_Juridico
         - Cadena
       * - Observaciones
         - Cadena
       * - Código_Solicitud
         - Numérico


.. index:: !Avaluo

Avaluos
-------

    .. list-table::
       :widths: 40 70
       :header-rows: 1

       * - | Campo
         - | Tipo de dato
       * - Código
         - Numérico
       * - Fecha_avaluo
         - Fecha
       * - Descripcion_inmueble
         - Cadena
       * - Valor_inmueble
         - Numerico
       * - Ubicacion_inmueble
         - Cadena
       * - Linderos_inmueble
         - Cadena
       * - Caracteristicas_sector
         - Cadena
       * - Observaciones
         - Cadena
       * - Código_Solicitud
         - Numérico


.. index:: !Fotografias

Fotografias Avaluos
-------------------

    .. list-table::
       :widths: 40 70
       :header-rows: 1

       * - | Campo
         - | Tipo de dato
       * - Código
         - Numérico
       * - Foto
         - Binario
       * - Descripción
         - Cadena
       * - Observaciones
         - Cadena
       * - Fecha_captura
         - Fecha
       * - Código_Avaluo
         - Numérico


.. index:: !Inspecciones

Inspecciones
------------

    .. list-table::
       :widths: 40 70
       :header-rows: 1

       * - | Campo
         - | Tipo de dato
       * - Código
         - Numérico
       * - Fecha_inspeccion
         - Fecha
       * - Tiempo_Funcionamiento
         - Numérico
       * - Cantidad_Productos
         - Numérico
       * - Costos_Actividad
         - Numérico
       * - Sistema_produccion
         - Cadena
       * - Clientes
         - Cadena
       * - Distribucion_Espacio_Fisico
         - Cadena
       * - Condición_Fisica_Sanitaria
         - Cadena
       * - Maquinaria
         - Cadena
       * - Materia_Prima
         - Cadena
       * - Observaciones
         - Cadena
       * - Código_Solicitud
         - Numérico


.. index:: !Fotografias

Fotografias Inspecciones
------------------------

    .. list-table::
       :widths: 40 70
       :header-rows: 1

       * - | Campo
         - | Tipo de dato
       * - Código
         - Numérico
       * - Foto
         - Binario
       * - Descripción
         - Cadena
       * - Observaciones
         - Cadena
       * - Fecha_captura
         - Fecha
       * - Código_Inspección
         - Numérico


.. index:: !Informes Técnicos

Informes Técnicos
-----------------

      .. list-table::
       :widths: 40 70
       :header-rows: 1

       * - | Campo
         - | Tipo de dato
       * - Código
         - Numérico
       * - Fecha_Elaboracion
         - Fecha
       * - Tipo_Empresa
         - Cadena
       * - Saldo_Balance_Personal
         - Numérico
       * - Organizacion_Juridica
         - Cadena
       * - Recomendaciones
         - Cadena
       * - Código_Solicitud
         - Numérico


.. index:: !Pagos, Caja

Pagos
-----

      .. list-table::
       :widths: 40 70
       :header-rows: 1

       * - | Campo
         - | Tipo de dato
       * - Código
         - Numérico
       * - Concepto
         - Cadena
       * - Total
         - Numérico
       * - Interés_capital
         - Numérico
       * - Interés_mora
         - Numérico
       * - Código_Crédito
         - Numérico


.. index:: !Propuestas

Propuestas
----------

      .. list-table::
       :widths: 40 70
       :header-rows: 1

       * - | Campo
         - | Tipo de dato
       * - Código
         - Numérico
       * - Sector
         - Numérico
       * - Código_Solicitante
         - Numérico
       * - Código_UnidadProductiva
         - Numérico
       * - Código_Taller
         - Numérico


.. index:: !Solicitudes

Solicitudes
-----------

      .. list-table::
       :widths: 40 70
       :header-rows: 1

       * - | Campo
         - | Tipo de dato
       * - Código
         - Numérico
       * - Numero_expediente
         - Alfanumérico
       * - Código_Consejo
         - Numérico


.. index:: !Créditos, Estados de Cuenta

Créditos
--------

      .. list-table::
       :widths: 40 70
       :header-rows: 1

       * - | Campo
         - | Tipo de dato
       * - Código
         - Numérico
       * - Monto_total
         - Numérico
       * - Monto_cuota
         - Numérico
       * - Periodos_gracia
         - Numérico
       * - Periodo_pago
         - Numérico
       * - Tasas_interés
         - Numérico
       * - Interés_mora
         - Numérico
       * - Fecha_liquidación
         - Fecha
       * - Fecha_ultima
         - Fecha









