# Análisis de Personas Políticamente Expuestas (PEP) - Uruguay

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Completed-success)

**Análisis exploratorio de datos para prevención de lavado de activos según Ley N° 19.574**

### Project overview (EN)

Exploratory analysis of Uruguay’s official list of Politically Exposed Persons (PEPs), published by SENACLAFT, to categorize risk levels and generate compliance‑oriented outputs (critical cases, enriched datasets and an executive report) for AML/KYC use cases.

---

## 📋 Tabla de Contenidos

- [Descripción del Proyecto](#-descripción-del-proyecto)
- [Contexto y Objetivos](#-contexto-y-objetivos)
- [Tecnologías Utilizadas](#-tecnologías-utilizadas)
- [Metodología](#-metodología)
- [Hallazgos Principales](#-hallazgos-principales)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Cómo Usar Este Proyecto](#-cómo-usar-este-proyecto)
- [Resultados y Archivos Generados](#-resultados-y-archivos-generados)
- [Aplicaciones Prácticas](#-aplicaciones-prácticas)
- [Sobre el Autor](#-sobre-el-autor)
- [Próximos Pasos](#-próximos-pasos)
- [Licencia](#-licencia)
- [Agradecimientos](#-agradecimientos)
- [Estadísticas del Proyecto](#-estadísticas-del-proyecto)

---

## 🎯 Descripción del Proyecto

Este proyecto analiza la **lista oficial de Personas Políticamente Expuestas (PEPs)** de Uruguay publicada por **SENACLAFT** (Secretaría Nacional para la Lucha Contra el Lavado de Activos y el Financiamiento del Terrorismo).

El objetivo es categorizar y priorizar los 857 PEPs registrados según su nivel de riesgo, facilitando el cumplimiento normativo de instituciones financieras y otros sujetos obligados por la **Ley N° 19.574**.

### ¿Qué es una Persona Políticamente Expuesta?

Las PEPs son individuos que desempeñan o han desempeñado funciones públicas prominentes. Por su exposición a decisiones de poder, representan un mayor riesgo potencial de estar involucrados en casos de corrupción o lavado de activos.

---

## 🎓 Contexto y Objetivos

### Contexto Legal

- **Marco normativo**: Ley N° 19.574 (Prevención y Control del Lavado de Activos)
- **Fuente de datos**: [Catálogo de Datos Abiertos del Gobierno de Uruguay](https://catalogodatos.gub.uy/)
- **Actualización**: Diciembre 2025  
- **Privacidad**: Listado público oficial; no se incorporan datos sensibles adicionales y el análisis tiene fines educativos y de apoyo a procesos de Compliance.

### Objetivos del Análisis

1. ✅ **Categorizar** a los 857 PEPs por nivel de riesgo (Alto, Medio, Otros).
2. ✅ **Identificar** casos críticos que requieren debida diligencia reforzada.
3. ✅ **Clasificar** organismos por tipo (Judicial, Legislativo, Financiero, etc.).
4. ✅ **Estimar** perfil etario de los PEPs.
5. ✅ **Generar** reportes ejecutivos y archivos operativos para Compliance.

---

## 🛠️ Tecnologías Utilizadas

| Tecnología | Uso |
|-----------|-----|
| **Python 3.8+** | Lenguaje de programación principal |
| **Pandas 2.0+** | Manipulación y análisis de datos |
| **NumPy** | Operaciones numéricas |
| **Google Colab** | Entorno de desarrollo en la nube |
| **Jupyter Notebook** | Documentación interactiva del análisis |

---

## 📊 Metodología

El proyecto sigue **Los 6 Pasos del Analista de Datos**:

### 1️⃣ Setup y Carga de Datos
- Importación de librerías.
- Carga del dataset oficial (CSV).
- Configuración del entorno.

### 2️⃣ Exploración Inicial
- Análisis de estructura (`head`, `info`, `describe`).
- Identificación de valores únicos.
- Top 10 organismos y cargos.

### 3️⃣ Limpieza y Verificación
- Verificación de duplicados.
- Validación de CIs únicas.
- Control de calidad de datos.

### 4️⃣ Análisis y Transformación
- Creación de categoría `NIVEL_RIESGO` (7 niveles).
- Creación de categoría `TIPO_ORGANISMO` (8 tipos).
- Estimación de `RANGO_EDAD` basada en CI uruguaya.
- **Iteración v1 → v2**: Mejora de categorización detectando errores.

### 5️⃣ Análisis Cruzado
- Identificación de 4 casos críticos (Alto Riesgo en finanzas).
- Análisis detallado de 52 PEPs en instituciones financieras.
- Tablas cruzadas Organismo vs Riesgo.

### 6️⃣ Comunicación y Exportación
- Reporte ejecutivo consolidado.
- Generación de archivos CSV para uso operativo.

---

## 🔍 Hallazgos Principales

### Distribución por Nivel de Riesgo

| Nivel de Riesgo | Cantidad | % |
|-----------------|----------|---|
| **Alto - Ejecutivo/Legislativo** | 181 | 21.1% |
| **Alto - Poder Judicial** | 143 | 16.7% |
| **Alto - Dirección General** | 20 | 2.3% |
| **Medio-Alto - Diplomático/Policial** | 11 | 1.3% |
| **Medio - Dirección/Gerencia** | 229 | 26.7% |
| **Medio - Representación Local** | 186 | 21.7% |
| **Otros** | 87 | 10.2% |

📌 **Total Alto Riesgo: 344 PEPs (40.1%)**  
📌 **Total Medio Riesgo: 426 PEPs (49.7%)**

---

### 🚨 Casos Críticos Identificados

Se detectaron **4 PEPs de Alto Riesgo trabajando DENTRO de instituciones financieras**, que requieren **debida diligencia reforzada** según el Artículo 8 de la Ley 19.574:

| Nombre | Cargo | Institución |
|--------|-------|-------------|
| **José Gerardo Amorin Batlle** | Presidente | BSE (Banco de Seguros del Estado) |
| **Alfonsina Batalla García Da Rosa** | Vicepresidente | BSE |
| **Roberto Borrelli Marchi** | Secretario General | BROU (Banco República) |
| **Darío Gaston Burstin Lederfain** | Vicepresidente | BHU (Banco Hipotecario) |

---

### Distribución por Tipo de Organismo

Poder Legislativo: 244 (28.5%)
Ministerios: 172 (20.1%)
Poder Judicial: 158 (18.4%)
Otros Organismos: 98 (11.4%)
Gobiernos Departamentales: 87 (10.2%)
Instituciones Financieras: 52 (6.1%) ← ATENCIÓN PRIORITARIA
Empresas Públicas: 35 (4.1%)
Educación: 11 (1.3%)

text

---

### Perfil Etario (Estimado por CI)

- **Menor de 35 años**: 185 PEPs (21.6%)
- **Entre 35-50 años**: 412 PEPs (48.1%)
- **Mayor de 50 años**: 260 PEPs (30.3%)

---

## 📂 Estructura del Proyecto

Analisis-PEP-Uruguay/
│
├── 📓 Analisis_PEP_Uruguay.ipynb # Notebook principal con análisis completo
├── 📄 lista-actualizada-de-pep.csv # Dataset original (SENACLAFT)
├── 📄 pep_alto_riesgo_finanzas.csv # 4 casos críticos identificados
├── 📄 REGISTRO_48_PEPs_MEDIO_RIESGO_FINANZAS.csv # Otros PEPs en finanzas
├── 📄 REPORTE_EJECUTIVO_PEP.txt # Reporte consolidado en texto
└── 📘 README.md # Este archivo

text

---

## 💻 Cómo Usar Este Proyecto

### Opción 1: Google Colab (Recomendado)

1. Descargá el archivo `Analisis_PEP_Uruguay.ipynb`.
2. Entrá a [Google Colab](https://colab.research.google.com/).
3. Subí el notebook: `Archivo → Subir notebook`.
4. Subí el dataset `lista-actualizada-de-pep.csv` cuando lo solicite.
5. Ejecutá todas las celdas: `Entorno de ejecución → Ejecutar todas`.

### Opción 2: Jupyter Notebook Local

Clonar el repositorio
git clone https://github.com/federicoramos67/Analisis-PEP-Uruguay.git
cd Analisis-PEP-Uruguay

Crear entorno virtual
python -m venv venv
source venv/bin/activate # En Windows: venv\Scripts\activate

Instalar dependencias
pip install pandas numpy jupyter

Abrir Jupyter
jupyter notebook Analisis_PEP_Uruguay.ipynb

text

### Requisitos

Python >= 3.8
pandas >= 2.0
numpy >= 1.20

text

---

## 📦 Resultados y Archivos Generados

El notebook genera automáticamente:

### 1️⃣ Dataset Enriquecido
Dataset original + 3 columnas nuevas:
- `NIVEL_RIESGO`: Clasificación en 7 niveles.
- `TIPO_ORGANISMO`: Clasificación en 8 categorías.
- `RANGO_EDAD`: Estimación etaria en 3 rangos.

### 2️⃣ Casos Críticos (`pep_alto_riesgo_finanzas.csv`)
- 4 PEPs de máxima prioridad.
- Requieren seguimiento inmediato.
- Uso: alertas automáticas en sistemas KYC.

### 3️⃣ Registro Medio Riesgo (`REGISTRO_48_PEPs_MEDIO_RIESGO_FINANZAS.csv`)
- 48 PEPs en instituciones financieras (sin Alto Riesgo).
- Requieren monitoreo estándar.

### 4️⃣ Reporte Ejecutivo (`REPORTE_EJECUTIVO_PEP.txt`)
- Resumen consolidado para stakeholders.
- Recomendaciones para Compliance.
- Listo para presentar a directorio.

---

## 💼 Aplicaciones Prácticas

Este análisis puede ser utilizado por:

### Sujetos Obligados por la Ley 19.574

✅ **Bancos y entidades financieras**  
✅ **Compañías de seguros**  
✅ **Casas de cambio**  
✅ **Escribanías y notarías**  
✅ **Inmobiliarias**  
✅ **Casinos y salas de juego**  
✅ **Contadores y auditores**  

### Casos de Uso Específicos

1. **Onboarding de clientes**: Cross-check automático de CI contra lista PEP.
2. **Monitoreo continuo**: Alertas cuando un cliente se convierte en PEP.
3. **Auditorías internas**: Verificar cumplimiento de debida diligencia.
4. **Reporte a SENACLAFT**: Documentación de casos detectados.
5. **Capacitación**: Ejemplos prácticos para entrenar equipos de Compliance.

---

## 🎓 Sobre el Autor

**Federico Ramos**  
*Analista de Datos Jr. | Data Analytics | Python*

- 📚 **Formación**: Analista de Datos Jr. - Fundación Telefónica / Universidad Católica del Uruguay.
- 💼 **Especialización**: Análisis exploratorio, Compliance, Prevención de Lavado de Activos.
- 🛠️ **Stack técnico**: Python, Pandas, SQL, Git, Jupyter.

### 📫 Contacto

- **LinkedIn**: [www.linkedin.com/in/federicoramosf](https://www.linkedin.com/in/federicoramosf)
- **GitHub**: [https://github.com/federicoramos67](https://github.com/federicoramos67)
- **Email**: [federidoramos6767@gmail.com](mailto:federidoramos6767@gmail.com)

---

## 📈 Próximos Pasos

Posibles mejoras futuras para este proyecto:

- [ ] Dashboard interactivo con Streamlit o Plotly Dash.
- [ ] API REST para consultas en tiempo real.
- [ ] Visualizaciones con Matplotlib/Seaborn.
- [ ] Análisis de series temporales (evolución histórica de PEPs).
- [ ] Machine Learning para predicción de riesgo.
- [ ] Integración con sistemas KYC/AML existentes.

---

## 📄 Licencia

Este proyecto está bajo la **Licencia MIT**.

Los datos utilizados son de dominio público y fueron obtenidos del [Catálogo de Datos Abiertos del Gobierno de Uruguay](https://catalogodatos.gub.uy/).  
Este repositorio se ofrece con fines educativos y de apoyo analítico, y no constituye asesoramiento legal ni reemplaza los sistemas formales de Compliance de ninguna institución.

---

## 🙏 Agradecimientos

- **SENACLAFT** por publicar datos abiertos de calidad.
- **Fundación Telefónica / UCU** por la formación en Data Analytics.
- **Comunidad de Python** por las librerías de código abierto.

---

## 📊 Estadísticas del Proyecto

![Lines of Code](https://img.shields.io/badge/Lines%20of%20Code-~800-blue)
![Commits](https://img.shields.io/badge/Commits-1-green)
![Last Updated](https://img.shields.io/badge/Last%20Updated-Diciembre%202025-orange)

---

**⭐ Si este proyecto te resultó útil, considerá darle una estrella en GitHub.**

---

*Desarrollado con 💙 en Uruguay*
