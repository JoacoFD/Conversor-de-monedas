# Currency Converter App

Una aplicación intuitiva y fácil de usar para la conversión de monedas en tiempo real. Esta herramienta permite a los usuarios realizar conversiones precisas entre diferentes monedas utilizando tasas de cambio actualizadas, obtenidas de una API externa confiable.

## Tabla de Contenidos

- [Descripción](#descripción)
- [Características](#características)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Requisitos Previos](#requisitos-previos)
- [Configuración del Entorno](#configuración-del-entorno)
- [Ejecución de la Aplicación](#ejecución-de-la-aplicación)
- [API de Tasas de Cambio](#api-de-tasas-de-cambio)
- [Capturas de Pantalla](#capturas-de-pantalla)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## Descripción

Currency Converter App es una aplicación web diseñada para facilitar la conversión de divisas. Con una interfaz clara y fácil de usar, esta aplicación permite convertir cantidades entre diferentes monedas de forma rápida y precisa. Las tasas de cambio se actualizan en tiempo real, proporcionando a los usuarios una experiencia confiable.

## Características

- **Actualización en Tiempo Real**: Las tasas de cambio se obtienen en tiempo real mediante una API externa.
- **Interfaz Intuitiva**: Interfaz de usuario moderna, fácil de navegar y estéticamente agradable.
- **Soporte Multidivisa**: Conversión entre múltiples monedas populares.
- **Precisión**: Resultados confiables con la mayor exactitud en los cálculos.

## Tecnologías Utilizadas

- **Python (Flask)**: Proporciona la infraestructura del backend y la gestión de rutas.
- **JavaScript (Fetch API)**: Se utiliza para manejar las solicitudes y actualizaciones del frontend en tiempo real.
- **HTML/CSS**: Estructura y estilos para una interfaz de usuario amigable.
- **Apilayer Currency API**: API para obtener tasas de cambio precisas y actualizadas.

## Requisitos Previos

- **Python 3.7 o superior**
- **Clave de API de Apilayer Currency API**: Necesaria para obtener tasas de cambio en tiempo real.

## Configuración del Entorno

1. **Clona este repositorio** en tu máquina local y navega al directorio del proyecto:
   ```bash
   git clone https://github.com/tu_usuario/currency-converter.git
   cd currency-converter
   ## Crea un Entorno Virtual
Es recomendable usar un entorno virtual para gestionar las dependencias del proyecto. Esto asegura que las bibliotecas instaladas no interfieran con otros proyectos.

**En windows**: python -m venv .venv
**En macOS/Linux**: python -m venv .venv

## Activa en entorno

**En windows:**: .venv\Scripts\activate
**En macOS/Linux**: source .venv/bin/activate

## Instala Dependencias

Con el entorno virtual activado, instala las dependencias necesarias listadas en requirements.txt: **pip install -r requirements.txt**

## Obtén una Clave de API
 Para obtener las tasas de cambio en tiempo real, necesitarás una clave de API de Apilayer Currency API. Regístrate en https://Apilayer.com y obtén tu clave. Agrega esta clave en el archivo app.py
 **API_KEY = 'tu_clave_api_aquí'**

## Ejecución de la Aplicación

**python app.py**
