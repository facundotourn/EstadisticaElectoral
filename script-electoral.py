import pandas as pd

try:
    g = pd.read_excel(".\\excels\\resultados_1983_-_presidente_y_vicepresidente_667.xlsx")
except:
    print("No existe ese archivo")

anios = ["1993", "1995", "1997", "1999", "2001", "2003", "2005", "2007", "2009", "2011", "2015", "2017", "2019"]
instancias = ["Paso", "Primera vuelta", "Segunda vuelta"]
tipos = ["Diputados", "Presidente", "Senadores"]

for anio in anios:
    for instancia in instancias:
        for tipo in tipos:
            try:
                g = pd.read_excel(".\\" + instancia * "\\" + tipo + "\\" + anio + ".xls")
            except:
                print("No hubo " + instancia + " de " + tipo + " en el año " + anio)