import pandas as pd
    
    
anios = ["1993", "1995", "1997", "1999", "2001", "2003", "2005", "2007", "2009", "2011", "2015", "2017", "2019"]
instancias = ["PASO", "Primera vuelta", "Segunda vuelta"]
tipos = ["Diputados", "Presidente" ]#, "Senadores"]

            
def procesarArchivo(data, anio, instancia, tipo, path):
    hojas = pd.ExcelFile(path).sheet_names
    print(hojas)
    for hoja in hojas
    
    return;

for anio in anios:
    for instancia in instancias:
        for tipo in tipos:
            print(".\\excels\\" + instancia + "\\" + tipo + "\\" + anio + ".xlsx")
            try:
                path = ".\\excels\\" + instancia + "\\" + tipo + "\\" + anio + ".xlsx"
                data = pd.read_excel(path)
                procesarArchivo(data,anio,instancia,tipo,path)
                print("Detectado")
            except FileNotFoundError:
                print("No hubo " + instancia + " de " + tipo + " en el año " + anio)
            print()
            
            
