# Análisis de Personas Políticamente Expuestas (PEP) - Uruguay

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Refactored-success)

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
- **Fuente de datos**: Recurso “Lista actualizada de PEP” del Catálogo de Datos Abiertos del Gobierno de Uruguay.
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

---

## 📊 Metodología

El proyecto ha sido reestructurado para seguir un enfoque basado en scripts, mejorando la automatización y reproducibilidad:

1.  **Setup y Carga de Datos**: El script `src/analisis_pep.py` carga el dataset desde el directorio `data/`.
2.  **Limpieza y Verificación**: Se realizan comprobaciones de duplicados y valores nulos.
3.  **Análisis y Transformación**: Se crean columnas adicionales (`NIVEL_RIESGO`, `TIPO_ORGANISMO`, `RANGO_EDAD`) para enriquecer el dataset.
4.  **Análisis Cruzado**: Se identifican PEPs en instituciones financieras y se detectan casos críticos.
5.  **Comunicación y Exportación**: Se generan reportes y archivos derivados en el directorio `data/`.

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

## 📂 Estructura del Proyecto

```
Analisis-PEP-Uruguay/
│
├── data/
│   ├── 2.lista-actualizada-de-pep.csv
│   └── (otros archivos generados...)
│
├── src/
│   └── analisis_pep.py
│
├── requirements.txt
└── README.md
```

---

## 💻 Cómo Usar Este Proyecto

### Requisitos

- Python 3.8 o superior
- Git

### Pasos

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

3.  **Ejecutar el análisis:**
    ```bash
    python src/analisis_pep.py
    ```

---

## 📦 Resultados y Archivos Generados

El script generará los siguientes archivos en el directorio `data/`:

-   `pep_enriquecido.csv`: El dataset completo con las columnas de análisis agregadas (`NIVEL_RIESGO`, `TIPO_ORGANISMO`, `RANGO_EDAD`).
-   `pep_alto_riesgo_finanzas.csv`: Una lista de los 4 PEPs de alta prioridad identificados.
-   `pep_medio_riesgo_finanzas.csv`: Un registro de los 48 PEPs de riesgo medio vinculados al sector financiero.

---

## 💼 Aplicaciones Prácticas

-   Onboarding KYC
-   Monitoreo continuo
-   Auditorías internas
-   Reporte a SENACLAFT
-   Capacitación

---

## 📈 Próximos Pasos

-   [ ] Dashboard interactivo
-   [ ] API REST
-   [ ] Visualizaciones
-   [ ] Series temporales
-   [ ] Modelos predictivos
-   [ ] Integración KYC

---

## 📄 Licencia

Licencia **MIT**. Datos públicos oficiales de SENACLAFT. Uso educativo y analítico.
