# Análisis de Personas Políticamente Expuestas (PEP) - Uruguay

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Completed-success)

**Análisis exploratorio de datos para prevención de lavado de activos según Ley N° 19.574**

### Project overview (EN)

Exploratory analysis of Uruguay’s official list of Politically Exposed Persons (PEPs), published by SENACLAFT, to categorize risk levels and generate compliance-oriented outputs (critical cases, enriched datasets and an executive report) for AML/KYC use cases.

---

## 📋 Tabla de Contenidos

- [Descripción del Proyecto](#-descripción-del-proyecto)
- [Contexto y Objetivos](#-contexto-y-objetivos)
- [Tecnologías Utilizadas](#-tecnologías-utilizadas)
- [Metodología](#-metodología)
- [Hallazgos Principales](#-hallazgos-principales)
- [Casos Críticos Identificados](#-casos-críticos-identificados)
- [Distribución por Tipo de Organismo](#distribución-por-tipo-de-organismo)
- [Perfil Etario (Estimado)](#perfil-etario-estimado)
- [Estructura del Proyecto](#estructura-del-proyecto)
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

Las PEPs son personas que desempeñan o han desempeñado en los últimos años funciones públicas de importancia en el país o en el extranjero, como altos cargos del Poder Ejecutivo, Legislativo, Judicial, fuerzas armadas, empresas estatales u otras entidades públicas, lo que las vuelve de mayor riesgo potencial en materia de corrupción o lavado de activos.

---

## 🎓 Contexto y Objetivos

### Contexto Legal

- **Marco normativo**: Ley N° 19.574 y decreto reglamentario N° 379/018.  
- **Fuente de datos**: Recurso “Lista actualizada de PEP” del Catálogo de Datos Abiertos del Gobierno de Uruguay.  
- **Actualización**: Datos a diciembre de 2025.  
- **Privacidad**: Listado público oficial, sin datos sensibles adicionales.

### Objetivos del Análisis

1. **Categorizar** a los 857 PEPs por nivel de riesgo.  
2. **Identificar** casos críticos que requieren debida diligencia reforzada.  
3. **Clasificar** organismos por tipo.  
4. **Estimar** perfil etario.  
5. **Generar** reportes ejecutivos y archivos operativos.

---

## 🛠️ Tecnologías Utilizadas

| Tecnología | Uso |
|-----------|-----|
| **Python 3.8+** | Lenguaje principal |
| **Pandas 2.0+** | Análisis de datos |
| **NumPy** | Operaciones numéricas |
| **Google Colab** | Entorno en la nube |
| **Jupyter Notebook** | Desarrollo y documentación |

---

## 📊 Metodología

El proyecto sigue **Los 6 Pasos del Analista de Datos**:

### 1️⃣ Setup y Carga de Datos
- Importación de librerías  
- Descarga del dataset (XLSX/CSV)  
- Conversión a `lista-actualizada-de-pep.csv`

### 2️⃣ Exploración Inicial
- `head`, `info`, `describe`  
- Identificación de columnas clave  
- Ranking de organismos y cargos

### 3️⃣ Limpieza y Verificación
- Duplicados  
- Verificación de CI únicas  
- Manejo de nulos  
- Corrección de formatos irregulares

### 4️⃣ Análisis y Transformación
- Creación de `NIVEL_RIESGO` (7 niveles)  
- `TIPO_ORGANISMO` (8 categorías)  
- `RANGO_EDAD` (3 rangos)

### 5️⃣ Análisis Cruzado
- PEPs en instituciones financieras  
- Detección de 4 casos críticos  
- Tablas cruzadas

### 6️⃣ Comunicación y Exportación
- Reporte ejecutivo  
- Exportación de datasets derivados

---

## 🔍 Hallazgos Principales

### Distribución por Nivel de Riesgo

| Nivel de Riesgo | Cantidad | % |
|-----------------|----------|---|
| Alto - Ejecutivo/Legislativo | 181 | 21.1% |
| Alto - Poder Judicial | 143 | 16.7% |
| Alto - Dirección General | 20 | 2.3% |
| Medio-Alto - Diplomático/Policial | 11 | 1.3% |
| Medio - Dirección/Gerencia | 229 | 26.7% |
| Medio - Representación Local | 186 | 21.7% |
| Otros | 87 | 10.2% |

📌 **Alto riesgo: 344 (40.1%)**  
📌 **Medio riesgo: 426 (49.7%)**

---

## 🚨 Casos Críticos Identificados

| Nombre | Cargo | Institución |
|--------|-------|-------------|
| José Gerardo Amorin Batlle | Presidente | BSE |
| Alfonsina Batalla García Da Rosa | Vicepresidente | BSE |
| Roberto Borrelli Marchi | Secretario General | BROU |
| Darío Gaston Burstin Lederfain | Vicepresidente | BHU |

---

## Distribución por Tipo de Organismo

- Poder Legislativo: 244 (28.5%)  
- Ministerios: 172 (20.1%)  
- Poder Judicial: 158 (18.4%)  
- Otros Organismos: 98 (11.4%)  
- Gobiernos Departamentales: 87 (10.2%)  
- Instituciones Financieras: 52 (6.1%)  
- Empresas Públicas: 35 (4.1%)  
- Educación: 11 (1.3%)

---

## Perfil Etario (Estimado)

- **Menor de 35**: 185 (21.6%)  
- **35–50**: 412 (48.1%)  
- **Mayor de 50**: 260 (30.3%)  

---

## 📂 Estructura del Proyecto

```
Analisis-PEP-Uruguay/
│
├── 📓 Analisis_PEP_Uruguay.ipynb
├── 📄 lista-actualizada-de-pep.csv
├── 📄 pep_alto_riesgo_finanzas.csv
├── 📄 REGISTRO_48_PEPs_MEDIO_RIESGO_FINANZAS.csv
├── 📄 REPORTE_EJECUTIVO_PEP.txt
└── 📘 README.md
```

---

## 💻 Cómo Usar Este Proyecto

### Opción 1: Google Colab
1. Subir el notebook  
2. Subir el dataset  
3. Ejecutar todas las celdas  

### Opción 2: Jupyter Local

```bash
git clone https://github.com/federicoramos67/Analisis-PEP-Uruguay.git
cd Analisis-PEP-Uruguay
python -m venv venv
source venv/bin/activate
pip install pandas numpy jupyter
jupyter notebook Analisis_PEP_Uruguay.ipynb
```

---

## 📦 Resultados y Archivos Generados

### 1️⃣ Dataset Enriquecido
Columnas agregadas:
- `NIVEL_RIESGO`
- `TIPO_ORGANISMO`
- `RANGO_EDAD`

### 2️⃣ Casos Críticos
4 PEPs de alta prioridad.

### 3️⃣ Registro Medio Riesgo
48 PEPs vinculados al sector financiero.

### 4️⃣ Reporte Ejecutivo
Formato texto listo para entregar.

---

## 💼 Aplicaciones Prácticas

- Onboarding KYC  
- Monitoreo continuo  
- Auditorías internas  
- Reporte a SENACLAFT  
- Capacitación  

---

## 🎓 Sobre el Autor

**Federico Ramos**  
*Analista de Datos Jr.*

- Python, Pandas, SQL  
- Análisis exploratorio  
- Compliance & PLAFT  

**Contacto:**  
- LinkedIn  
- GitHub  
- Email  

---

## 📈 Próximos Pasos

- [ ] Dashboard interactivo  
- [ ] API REST  
- [ ] Visualizaciones  
- [ ] Series temporales  
- [ ] Modelos predictivos  
- [ ] Integración KYC  

---

## 📄 Licencia

Licencia **MIT**  
Datos públicos oficiales de SENACLAFT  
Uso educativo y analítico  

---

## 🙏 Agradecimientos

- SENACLAFT  
- Fundación Telefónica / UCU  
- Comunidad Python  

---

## 📊 Estadísticas del Proyecto

![Lines of Code](https://img.shields.io/badge/Lines%20of%20Code-~800-blue)
![Commits](https://img.shields.io/badge/Commits-1-green)
![Last Updated](https://img.shields.io/badge/Last%20Updated-Diciembre%202025-orange)

---

**⭐ Si este proyecto te fue útil, considerá darle una estrella.**

*Desarrollado con 💙 en Uruguay*
