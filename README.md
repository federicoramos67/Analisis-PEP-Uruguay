# Análisis de Personas Políticamente Expuestas (PEP) - Uruguay

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-green)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7%2B-orange)
![Seaborn](https://img.shields.io/badge/Seaborn-0.12%2B-9cf)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Completo-success)

**Análisis exploratorio de datos para prevención de lavado de activos según Ley N° 19.574**

### Project overview (EN)

Exploratory analysis of Uruguay's official list of Politically Exposed Persons (PEPs), published by SENACLAFT, to categorize risk levels and generate compliance-oriented outputs (critical cases, enriched datasets, visualizations and an executive report) for AML/KYC use cases.

---

## 📋 Tabla de Contenidos

- [Descripción del Proyecto](#-descripción-del-proyecto)
- [Contexto y Objetivos](#-contexto-y-objetivos)
- [Tecnologías Utilizadas](#-tecnologías-utilizadas)
- [Visualizaciones](#-visualizaciones)
- [Metodología](#-metodología)
- [Hallazgos Principales](#-hallazgos-principales)
- [Casos Críticos Identificados](#-casos-críticos-identificados)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Cómo Usar Este Proyecto](#-cómo-usar-este-proyecto)
- [Resultados y Archivos Generados](#-resultados-y-archivos-generados)
- [Aplicaciones Prácticas](#-aplicaciones-prácticas)
- [Próximos Pasos](#-próximos-pasos)
- [Licencia](#-licencia)

---

## 🎯 Descripción del Proyecto

Este proyecto analiza la **lista oficial de Personas Políticamente Expuestas (PEPs)** de Uruguay publicada por **SENACLAFT** (Secretaría Nacional para la Lucha Contra el Lavado de Activos y el Financiamiento del Terrorismo).

El objetivo es categorizar y priorizar los 857 PEPs registrados según su nivel de riesgo, facilitando el cumplimiento normativo de instituciones financieras y otros sujetos obligados por la **Ley N° 19.574**.

---

## 🎓 Contexto y Objetivos

### Contexto Legal

- **Marco normativo**: Ley N° 19.574 y decreto reglamentario N° 379/018.
- **Fuente de datos**: Recurso "Lista actualizada de PEP" del Catálogo de Datos Abiertos del Gobierno de Uruguay.
- **Privacidad**: Listado público oficial, sin datos sensibles adicionales.

### Objetivos del Análisis

1. **Categorizar** a los 857 PEPs por nivel de riesgo.
2. **Identificar** casos críticos que requieren debida diligencia reforzada.
3. **Clasificar** organismos por tipo.
4. **Estimar** perfil etario.
5. **Generar** reportes ejecutivos, archivos operativos y visualizaciones profesionales.

---

## 🛠️ Tecnologías Utilizadas

| Tecnología | Uso |
|-----------|-----|
| **Python 3.8+** | Lenguaje principal |
| **Pandas 2.0+** | Análisis y transformación de datos |
| **NumPy** | Operaciones numéricas |
| **Matplotlib 3.7+** | Visualizaciones (estilo oscuro profesional) |
| **Seaborn 0.12+** | Heatmaps y gráficos estadísticos |
| **Jupyter Notebook** | Análisis interactivo, compatible con Google Colab |

---

## 📊 Visualizaciones

El proyecto incluye **5 visualizaciones profesionales** con estilo oscuro consistente
(fondo `#0f0f17`, rojo `#e63946`, teal `#2a9d8f`), generadas en el notebook principal.

### 1. Distribución por Nivel de Riesgo
Barras horizontales ordenadas por cantidad, con coloreado semántico por nivel de riesgo (rojo = alto, teal = medio, púrpura = otros).

### 2. Top 15 Organismos con Más PEPs
Gráfico de barras verticales coloreado por tipo institucional con leyenda integrada.

### 3. Distribución por Tipo de Organismo (Dona)
Gráfico de dona con tabla de datos complementaria al costado.

### 4. Sector Financiero Destacado
Panel doble: PEPs por institución financiera + tabla de casos críticos de alto riesgo.

### 5. Heatmap Rango Etario × Tipo de Organismo
Mapa de calor de concentración demográfica + distribución etaria global.

> Los archivos PNG se generan en `notebooks/` al ejecutar el notebook.

---

## 📊 Metodología

El proyecto sigue un pipeline de análisis reproducible:

1.  **Setup y Carga de Datos**: El script `src/analisis_pep.py` y el notebook cargan el dataset desde `data/`.
2.  **Limpieza y Verificación**: Comprobaciones de duplicados y valores nulos.
3.  **Análisis y Transformación**: Se crean columnas adicionales (`NIVEL_RIESGO`, `TIPO_ORGANISMO`, `RANGO_EDAD`) para enriquecer el dataset.
4.  **Análisis Cruzado**: Se identifican PEPs en instituciones financieras y se detectan casos críticos.
5.  **Visualizaciones**: 5 gráficos profesionales con estilo oscuro consistente.
6.  **Comunicación y Exportación**: Se generan reportes y archivos derivados en `data/`.

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

### Distribución por Tipo de Organismo

| Tipo de Organismo | PEPs | % |
|-------------------|------|---|
| Poder Legislativo | 244 | 28.5% |
| Ministerios | 172 | 20.1% |
| Poder Judicial | 158 | 18.4% |
| Otros Organismos | 98 | 11.4% |
| Gobiernos Departamentales | 87 | 10.2% |
| Instituciones Financieras | 52 | 6.1% |
| Empresas Públicas | 35 | 4.1% |
| Educación | 11 | 1.3% |

---

## 🚨 Casos Críticos Identificados

PEPs de **alto riesgo** en el **sector financiero** (máxima prioridad para due diligence):

| Nombre | Cargo | Institución |
|--------|-------|-------------|
| José Gerardo Amorin Batlle | Presidente | BSE |
| Alfonsina Batalla García Da Rosa | Vicepresidente | BSE |
| Roberto Borrelli Marchi | Secretario General | BROU |
| Darío Gaston Burstin Lederfain | Vicepresidente | BHU |

---

## 📂 Estructura del Proyecto

```
Analisis-PEP-Uruguay/
│
├── data/
│   ├── 2.lista-actualizada-de-pep.csv       # Dataset oficial SENACLAFT
│   ├── pep_enriquecido.csv                  # Dataset con columnas de análisis
│   ├── pep_alto_riesgo_finanzas.csv         # 4 casos críticos
│   └── pep_medio_riesgo_finanzas.csv        # 48 PEPs riesgo medio en finanzas
│
├── notebooks/
│   ├── 1.Analisis_PEP_Uruguay.ipynb         # Notebook principal (Colab-ready)
│   ├── viz_01_riesgo_distribucion.png
│   ├── viz_02_top_organismos.png
│   ├── viz_03_tipo_organismo.png
│   ├── viz_04_sector_financiero.png
│   └── viz_05_rango_etario.png
│
├── src/
│   └── analisis_pep.py                      # Script principal de análisis
│
├── requirements.txt
└── README.md
```

---

## 💻 Cómo Usar Este Proyecto

### Opción A — Google Colab (recomendado, sin instalación)

1. Abrir el notebook `notebooks/1.Analisis_PEP_Uruguay.ipynb` en Google Colab.
2. El notebook clona el repositorio automáticamente en la primera celda de setup.
3. Ejecutar todas las celdas en orden (`Runtime > Run all`).

### Opción B — Local

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/federicoramos67/Analisis-PEP-Uruguay.git
    cd Analisis-PEP-Uruguay
    ```

2.  **Crear un entorno virtual e instalar dependencias:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3.  **Ejecutar el script de análisis:**
    ```bash
    python src/analisis_pep.py
    ```

4.  **O abrir el notebook:**
    ```bash
    jupyter notebook notebooks/1.Analisis_PEP_Uruguay.ipynb
    ```

---

## 📦 Resultados y Archivos Generados

El notebook y el script generan los siguientes archivos:

**En `data/`:**
- `pep_enriquecido.csv`: Dataset completo con `NIVEL_RIESGO`, `TIPO_ORGANISMO`, `RANGO_EDAD`.
- `pep_alto_riesgo_finanzas.csv`: 4 PEPs de alta prioridad en sector financiero.
- `pep_medio_riesgo_finanzas.csv`: 48 PEPs de riesgo medio en sector financiero.

**En `notebooks/`:**
- 5 gráficos PNG con estilo oscuro profesional (150 DPI).

---

## 💼 Aplicaciones Prácticas

- Onboarding KYC
- Monitoreo continuo
- Auditorías internas
- Reporte a SENACLAFT
- Capacitación en AML/CFT

---

## 📈 Próximos Pasos

- [x] Visualizaciones profesionales (estilo oscuro, 5 gráficos)
- [x] Notebook interactivo completo (Google Colab compatible)
- [ ] Dashboard interactivo (Plotly/Dash)
- [ ] API REST
- [ ] Series temporales
- [ ] Modelos predictivos
- [ ] Integración KYC

---

## 📄 Licencia

Licencia **MIT**. Datos públicos oficiales de SENACLAFT. Uso educativo y analítico.
