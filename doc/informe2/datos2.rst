﻿﻿Diseño de Datos
===============


Diccionario de Datos
--------------------

    # **Solicitante**

    * **Nombre de planilla**: Propuesta de financiamiento
    * **Descripción**:

    .. tabularcolumns:: |p{4cm}|p{7cm}|

    .. list-table::
       :widths: 40 70
       :header-rows: 1

       * - | Campo
         - | Tipo de dato
       * - Numero
         - Numérico
       * - Nombres_Y_Apellidos
         - Cadena
       * - CI
         - Numerico
       * - RIF
         - AlfaNumerico
       * - Fecha_Nacimiento
         - Fecha
       * - Edad
         - Numerico
       * - Edad
         - Cadena
       * - Sexo
         - Caracter
       * - Direccion_Habitacion
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
       * - Correo_Electronico
         - Cadena
       * - Twitter
         - Cadena
       * - Twitter
         - Cadena


    # **Unidad productiva**

    .. list-table::
       :widths: 40 70
       :header-rows: 1

       * - | Campo
         - | Tipo de dato
       * - Nombre_Unidad_Productiva
         - Cadena
       * - Dirección_UP
         - Cadena
       * - Teléfono_Fijo
         - Numerico
       * - Teléfono_Celular
         - Numerico
       * - Actividad
         - Cadena
       * - Experiencia
         - Cadena
       * - Área_Geográfica
         - Cadena
       * - Area_Funcionamiento
         - Numerico
       * - Tenencia
         - Cadena
       * - Area_M2
         - Numerico
       * - Zona_Geografica
         - Cadena
       * - Servicios
         - Cadena



    # **Actividad productiva**

    .. list-table::
       :widths: 40 70
       :header-rows: 1

       * - | Campo
         - | Tipo de dato
       * - Producto_Derivado
         - Cadena
       * - Materia_Prima
         - Cadena
       * - Donde_Y_Como_obtiene_PM
         - Cadena
       * - Precio_Venta_Producto
         - Numerico
       * - Distribución_Sistema _Ventas
         - Cadena
       * - Numero_de _Trabajadores
         - Numerico
       * - Puestos_Trabajo_Generar
         - Numerico



    # **Plan de inversion**

    .. list-table::
       :widths: 40 70
       :header-rows: 1

       * - | Campo
         - | Tipo de dato
       * - Capital_de_trabajo
         - Cadena
       * - Materia_Prima
         - Cadena
       * - Mano_de_Obra
         - Numerico
       * - Gastos_de_Constitución
         - Numerico
       * - Inversiones_Fijas
         - Cadena
       * - Ampliación_o_Remodelación
         - Cadena
       * - Maquinaria
         - Cadena
       * - Equipo
         - Numerico
       * - Utensilios_herramientas_menores
         - Cadena
       * - Otros
         - Cadena
       * - Inversión_Total
         - Cadena


    # **Conyuge**

    .. list-table::
       :widths: 40 70
       :header-rows: 1

       * - | Campo
         - | Tipo de dato
       * - Cedula_Identidad
         - Cadena
       * - Nombres_Y_Apellidos
         - Cadena
       * - Nacionalidad
         - Numerico
       * - Estado_Civil
         - Numerico
       * - Grado_Instruccion
         - Cadena
       * - Condicion_Vivienda
         - Cadena
       * - Dirección_Habitación
         - Cadena
       * - Municipio
         - Numerico
       * - Telefono_Habitación
         - Cadena
       * - Telefono_Celular
         - Cadena
       * - FAX
         - Cadena
       * - Correo_Electronico
         - Cadena
       * - Observaciones
         - Cadena



    # **Referencias personales y familiares**

    .. list-table::
       :widths: 40 70
       :header-rows: 1

       * - | Campo
         - | Tipo de dato
       * - Referencia_Personal_1
         - Cadena
       * - Referencia_Personal_2
         - Cadena
       * - Referencia_Familiar_1
         - Cadena
       * - Referencia_Familiar_2
         - Cadena


    # **Avalista**

    .. list-table::
       :widths: 40 70
       :header-rows: 1

       * - | Campo
         - | Tipo de dato
       * - Cedula_Identidad
         - Numerico
       * - Nombres_Apellidos
         - Cadena
       * - Direccion_Habitacion
         - Cadena
       * - Telefono_Fijo
         - Numerico
       * - Telefono_Celular
         - Numerico
       * - Nombre_Direccion_Trabajo
         - Cadena
       * - Cargo
         - Cadena
       * - Ingreso_Mensual
         - Numerico
       * - Otros_Ingresos
         - Numerico
       * - Total_Ingresos
         - Numerico

    # **Cuentas Bancarias Aval**

    .. list-table::
       :widths: 40 70
       :header-rows: 1

       * - | Campo
         - | Tipo de dato
       * - Nro_Cuenta
         - Numerico
       * - Nombre_Banco
         - Cadena
       * - Tipo_Cuenta
         - Cadena
       * - Monto
         - Numerico



    # **Activos fijos Aval**

    .. list-table::
       :widths: 40 70
       :header-rows: 1

       * - | Campo
         - | Tipo de dato
       * - Activo
         - Cadena
       * - Titulo
         - Cadena
       * - Avaluo
         - Numerico



    # **Taller**

    .. list-table::
       :widths: 40 70
       :header-rows: 1

       * - | Campo
         - | Tipo de dato
       * - Fecha_Taller
         - Fecha
       * - Persona_Atendio
         - Cadena



    # **Garantia**

    .. list-table::
       :widths: 40 70
       :header-rows: 1

       * - | Campo
         - | Tipo de dato
       * - Nro_Expediente
         - AlfaNumerico
       * - Tipo_Garantia
         - Cadena
       * - Descripcion
         - Cadena
       * - Avaluo
         - Numerico



    # **Requisitos personales**

    .. list-table::
       :widths: 40 70
       :header-rows: 1

       * - | Campo
         - | Tipo de dato
       * - Carta_Residencia
         - Cadena
       * - Documento_Propiedad_Alquiler
         - Cadena
       * - Croquis_Ubicacion
         - Cadena
       * - Exposicion_Motivos
         - Cadena
       * - Registro_Comercio_RIF
         - Cadena
       * - Permisos_Funcionamiento
         - Cadena



    # **Requisitos empresa**

    .. list-table::
       :widths: 40 70
       :header-rows: 1

       * - | Campo
         - | Tipo de dato
       * - Estado_Financiero_2_Ultimos_Años
         - Cadena
       * - Balance_Comprobacion
         - Cadena
       * - Solvencia_Laboral
         - Cadena
       * - Solvencia_SS
         - Cadena
       * - Solvencia_INCES
         - Cadena
       * - Solvencia_BANAVIH
         - Cadena



    # **Requisitos sector**

    .. list-table::
       :widths: 40 70
       :header-rows: 1

       * - | Campo
         - | Tipo de dato
       * - Permiso_Sanidad
         - Cadena
       * - Permiso_Ambiente
         - Cadena
       * - Permiso_Alcaldia
         - Cadena
       * - Permiso_Bomberos
         - Cadena
       * - Permiso_Sanidad
         - Cadena
       * - Permiso_Sanidad
         - Cadena



    # **Requisitos garantia**

    .. list-table::
       :widths: 40 70
       :header-rows: 1

       * - | Campo
         - | Tipo de dato
       * - Certificacion_Ingresos_Constancia_trabajo
         - Cadena
       * - Avaluo_Bien_Mueble
         - Numerico
       * - Seguro_Bien_Mueble
         - Cadena
       * - Documento_Propiedad_Bien_Mueble
         - Cadena
       * - Croquis_Ubicación
         - Cadena
       * - Levantamiento_Topográfico_>1Ha
         - Cadena
       * - Cedula_Identidad_Socio_Conyuge
         - Numerico
       * - Inscripcion_Sogampi
         - Cadena
       * - Carta_Fianza
         - Cadena
       * - Documento_Credito_Notariado
         - Cadena
       * - Fianza_Financiera_Notariado
         - Cadena
       * - Firma
         - Imagen


    # **Consejo directivo**

    .. list-table::
       :widths: 40 70
       :header-rows: 1

       * - | Campo
         - | Tipo de dato
       * - Consejo_Directivo_Nro
         - Numerico
       * - Consejo_Directivo_Fecha
         - Fecha
       * - Hora_Consejo_Directivo
         - Hora
       * - Miembros_Consejo_Directivo
         - Cadena
       * - Nro_Expediente
         - AlfaNumerico
       * - Razon_Social
         - Cadena
       * - Estatus_Desicion
         - Cadena
       * - Plan_Inversion
         - Numerico
       * - Firma
         - Imagen



    # **Control previo**

    .. list-table::
       :widths: 40 70
       :header-rows: 1

       * - | Campo
         - | Tipo de dato
       * - Codigo_Analisis_Juridico
         - AlfaNumerico
       * - Nro_Expediente
         - Cadena
       * - Descripcion_Garantia
         - Cadena
       * - Estatus_Analisis_Juridico
         - Cadena


    # **Inspeccion**

    .. list-table::
       :widths: 40 70
       :header-rows: 1

       * - | Campo
         - | Tipo de dato
       * - Nro_Expediente
         - AlfaNumerico
       * - Tiempo_Funcionamiento
         - Numerico
       * - Cantidad_Productos
         - Numerico
       * - Costos_Actividad
         - Numerico
       * - Sistema_produccion
         - Cadena
       * - Clientes
         - Cadena
       * - Distribucio_Espacio_Fisico
         - Cadena
       * - Condicion_Fisica_Sanitaria
         - Cadena
       * - Maquinaria
         - Cadena
       * - Materia_Prima
         - Cadena
       * - Observaciones
         - Cadena
       * - Firma
         - Imagen


    # **Informe tecnico**

      .. list-table::
       :widths: 40 70
       :header-rows: 1

       * - | Campo
         - | Tipo de dato
       * - Nro_Expediente
         - AlfaNumerico
       * - Fecha_Elaboracion
         - Fecha
       * - Tipo_Empresa
         - Cadena
       * - Saldo_Balance_Personal
         - Numerico
       * - Organizacion_Juridica
         - Cadena
       * - Recomendaciones
         - Cadena
       * - Firma
         - Imagen
       * - Informe_Fotografico_Inspeccion
         - Imagen



    # **Estado de cuentas**



    # **Credito (numero de expediente)**