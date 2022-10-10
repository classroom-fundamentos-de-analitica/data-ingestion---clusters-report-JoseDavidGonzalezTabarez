"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def ingest_data():
    import re
    
    i = 0
    dict_linea = {}
    df = pd.DataFrame()
    with open('./clusters_report.txt') as f:
        for line in f:

            line = re.sub(r"\s+", " ", line)
            if len(line)>1 and i > 3:
                if line.split()[0].isnumeric() == True:
                    try: 
                        dict_linea['Principales palabras clave'] = ' '.join(dict_linea['Principales palabras clave'])
                        df = df.append(dict_linea, ignore_index=True)
                    except: pass
                    dict_linea = {'Cluster': line.split()[0],
                                'Cantidad de palabras clave': line.split()[1],
                                'Porcentaje de palabras clave': ''.join(line.split()[2:4]),
                                'Principales palabras clave': line.split()[4:]}
                else: 
                    dict_linea['Principales palabras clave'].append(' '.join(line.split()))
            i += 1
    dict_linea['Principales palabras clave'] = ' '.join(dict_linea['Principales palabras clave'])
    df = df.append(dict_linea, ignore_index=True)

    return df
