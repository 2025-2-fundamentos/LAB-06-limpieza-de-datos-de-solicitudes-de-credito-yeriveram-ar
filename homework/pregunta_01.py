"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""

import pandas as pd
import os
def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
def load_data(input_file):
    df = pd.read_csv(input_file, sep=";", index_col=0)
    return df


def text_normalization(dataframe, columna):
    dataframe[columna] = (
        dataframe[columna]
        .str.lower()
        .str.strip()
        .str.replace("_", " ")
        .str.replace("-", " ")
        .str.replace(",", "")
        .str.replace(".00", "")
        .str.replace("$", "")
        .str.strip()
    )
    return dataframe


def main(input_file, output_file):
    columnas = ["sexo", "tipo_de_emprendimiento", "idea_negocio", "monto_del_credito", "línea_credito",]
    df = load_data(input_file)

    for columna in columnas:
        df = text_normalization(df, columna)

    df["barrio"] = df["barrio"].str.lower().str.replace("_", " ").str.replace("-", " ")
    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int)
    df["monto_del_credito"] = df["monto_del_credito"].astype(float)
    df["fecha_de_beneficio"] = pd.to_datetime(
        df["fecha_de_beneficio"], format="%d/%m/%Y", errors="coerce"
    ).combine_first(pd.to_datetime(df["fecha_de_beneficio"], format="%Y/%m/%d", errors="coerce"))
    df = df.drop_duplicates()
    df = df.dropna()
    save_output(df, "solicitudes_de_credito", output_file)


def save_output(dataframe, name, output_directory="../files/output"):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    dataframe.to_csv(f"{output_directory}/{name}.csv", sep=";", index=False,)



if "__main__" in __name__:
    main(
        input_file="files/input/solicitudes_de_credito.csv",
        output_file="files/output",
    )