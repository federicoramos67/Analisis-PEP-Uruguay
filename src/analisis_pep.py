# -*- coding: utf-8 -*-
"""
Análisis de Personas Políticamente Expuestas (PEP) - Uruguay

Este script realiza un análisis exploratorio de la lista oficial de PEPs
de Uruguay para categorizar niveles de riesgo y generar reportes para
casos de uso de AML/KYC.
"""

import os
import pandas as pd
import numpy as np

# --- CONFIGURACIÓN ---
DATA_INPUT_PATH = "data/2.lista-actualizada-de-pep.csv"
DATA_OUTPUT_DIR = "data"
REPORT_OUTPUT_PATH = "REPORTE_EJECUTIVO_PEP.txt"

# --- FUNCIONES DE CATEGORIZACIÓN ---

def categorizar_cargo_v2(cargo):
    """
    Categoriza un cargo en un nivel de riesgo. Versión mejorada con más casos.
    """
    cargo_mayuscula = cargo.upper()

    # Alto Riesgo - Poder Ejecutivo/Legislativo
    if any(palabra in cargo_mayuscula for palabra in
           ['MINISTRO', 'MINISTRA', 'SUBSECRETARIO', 'SUBSECRETARIA',
            'PRESIDENTE', 'PRESIDENTA', 'VICEPRESIDENTE', 'VICEPRESIDENTA',
            'INTENDENTE', 'INTENDENTA', 'EMBAJADOR', 'EMBAJADORA',
            'SENADOR', 'SENADORA', 'REPRESENTANTE NACIONAL',
            'REPRESENTANTE PERMANENTE', 'GENERAL', 'ALMIRANTE', 'SECRETARIO GENERAL']):
        return 'Alto - Ejecutivo/Legislativo'

    # Alto Riesgo - Poder Judicial
    elif any(palabra in cargo_mayuscula for palabra in
             ['JUEZ', 'JUEZA', 'FISCAL', 'MAGISTRADO', 'MAGISTRADA']):
        return 'Alto - Poder Judicial'

    # Alto Riesgo - Dirección General
    elif any(palabra in cargo_mayuscula for palabra in
             ['DIRECTOR GENERAL', 'DIRECTORA GENERAL',
              'DIRECTOR NACIONAL', 'DIRECTORA NACIONAL',
              'GERENTE GENERAL']):
        return 'Alto - Dirección General'

    # Medio-Alto - Cargos diplomáticos y policiales
    elif any(palabra in cargo_mayuscula for palabra in
             ['CONSUL GENERAL', 'CÓNSUL GENERAL',
              'JEFE DE POLICIA', 'SUBJEFE DE POLICIA',
              'ENCARGADO DE NEGOCIOS', 'COMISARIO GENERAL']):
        return 'Medio-Alto - Diplomático/Policial'

    # Medio Riesgo - Dirección/Gerencia
    elif any(palabra in cargo_mayuscula for palabra in
             ['DIRECTOR', 'DIRECTORA', 'GERENTE',
              'SUBDIRECTOR', 'SUBDIRECTORA', 'COORDINADOR', 'COORDINADORA']):
        return 'Medio - Dirección/Gerencia'

    # Medio Riesgo - Representación Local
    elif any(palabra in cargo_mayuscula for palabra in
             ['EDIL', 'CONCEJAL', 'ALCALDE', 'ALCALDESA']):
        return 'Medio - Representación Local'

    # Otros
    else:
        return 'Otros'

def categorizar_organismo(organismo):
    """
    Clasifica el organismo según su naturaleza.
    """
    org_mayuscula = organismo.upper()

    if 'MINISTERIO' in org_mayuscula:
        return 'Ministerios'
    elif 'PODER JUDICIAL' in org_mayuscula or 'FISCALIA' in org_mayuscula or 'TRIBUNAL' in org_mayuscula:
        return 'Poder Judicial'
    elif 'PODER LEGISLATIVO' in org_mayuscula or 'JUNTA DEPARTAMENTAL' in org_mayuscula:
        return 'Poder Legislativo'
    elif 'INTENDENCIA' in org_mayuscula:
        return 'Gobiernos Departamentales'
    elif 'BANCO' in org_mayuscula or 'BPS' in org_mayuscula or 'BSE' in org_mayuscula:
        return 'Instituciones Financieras'
    elif any(empresa in org_mayuscula for empresa in ['ANTEL', 'ANCAP', 'OSE', 'UTE', 'ANP']):
        return 'Empresas Públicas'
    elif 'UNIVERSIDAD' in org_mayuscula or 'ANEP' in org_mayuscula:
        return 'Educación'
    else:
        return 'Otros Organismos'

def estimar_edad(ci):
    """
    Estima rango de edad según la CI uruguaya.
    """
    if ci < 20000000:
        return 'Mayor 50 años'
    elif ci < 40000000:
        return '35-50 años'
    else:
        return 'Menor 35 años'

# --- FUNCIÓN PRINCIPAL DE ANÁLISIS ---

def analizar_pep():
    """
    Función principal que ejecuta el pipeline de análisis de PEPs.
    """
    # 1. Carga de datos
    print("Iniciando análisis de PEPs...")
    try:
        df = pd.read_csv(DATA_INPUT_PATH)
        print(f"✅ Dataset cargado: {df.shape}")
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo en '{DATA_INPUT_PATH}'")
        return

    # 2. Limpieza y Verificación
    print("\nVerificando calidad de datos...")
    if df.duplicated().sum() > 0:
        print("⚠️  Se encontraron y eliminaron filas duplicadas.")
        df.drop_duplicates(inplace=True)
    else:
        print("✅ No hay filas duplicadas.")

    # 3. Análisis y Transformación (Feature Engineering)
    print("\nCreando nuevas categorías...")
    df['NIVEL_RIESGO'] = df['CARGO'].apply(categorizar_cargo_v2)
    df['TIPO_ORGANISMO'] = df['ORGANISMO'].apply(categorizar_organismo)
    df['RANGO_EDAD'] = df['CI'].apply(estimar_edad)
    print("✅ Columnas 'NIVEL_RIESGO', 'TIPO_ORGANISMO', 'RANGO_EDAD' creadas.")

    # 4. Análisis Cruzado e Identificación de Casos Críticos
    print("\nRealizando análisis cruzado...")
    criticos = df[
        (df['NIVEL_RIESGO'].str.contains('Alto')) &
        (df['TIPO_ORGANISMO'] == 'Instituciones Financieras')
    ]
    print(f"🚨 Se identificaron {len(criticos)} casos críticos (Alto Riesgo en Finanzas).")

    # 5. Exportación de Resultados
    print("\nExportando resultados...")
    if not os.path.exists(DATA_OUTPUT_DIR):
        os.makedirs(DATA_OUTPUT_DIR)

    # Exportar dataset enriquecido
    df.to_csv(os.path.join(DATA_OUTPUT_DIR, 'pep_enriquecido.csv'), index=False)
    print(f"✅ Dataset enriquecido guardado en '{DATA_OUTPUT_DIR}/pep_enriquecido.csv'")

    # Exportar casos críticos
    criticos_export = criticos[['CI', 'NOMBRE', 'CARGO', 'ORGANISMO', 'NIVEL_RIESGO']]
    criticos_export.to_csv(os.path.join(DATA_OUTPUT_DIR, 'pep_alto_riesgo_finanzas.csv'), index=False)
    print(f"✅ Casos críticos guardados en '{DATA_OUTPUT_DIR}/pep_alto_riesgo_finanzas.csv'")

    # Exportar otros PEPs en finanzas
    fin_todas = df[df['TIPO_ORGANISMO'] == 'Instituciones Financieras']
    fin_resto = fin_todas[~fin_todas['NIVEL_RIESGO'].str.contains('Alto')]
    fin_resto_export = fin_resto[['CI', 'NOMBRE', 'CARGO', 'ORGANISMO', 'NIVEL_RIESGO', 'RANGO_EDAD']]
    fin_resto_export.to_csv(os.path.join(DATA_OUTPUT_DIR, 'pep_medio_riesgo_finanzas.csv'), index=False)
    print(f"✅ PEPs de riesgo medio en finanzas guardados en '{DATA_OUTPUT_DIR}/pep_medio_riesgo_finanzas.csv'")

    print("\nAnálisis completado exitosamente.")

if __name__ == '__main__':
    analizar_pep()
