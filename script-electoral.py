import pandas as pd
    
    
anios = ["1993", "1995", "1997", "1999", "2001", "2003", "2005", "2007", "2009", "2011", "2013", "2015", "2017", "2019"]
instancias = ["PASO", "Primera vuelta", "Segunda vuelta"]
tipos = ["Diputados", "Presidente" ]#, "Senadores"]

def procesarHoja (path,hoja):
    return pd.read_excel(path,hoja);


def procesarArchivo(anio, instancia, tipo, path):
    hojas = pd.ExcelFile(path).sheet_names
    hojas.pop(0)
    data = {}
    
    if int(anio) <= 2013:
        hojas.pop(-1)   
        
    for hoja in hojas:
        data[hoja] = procesarHoja(path,hoja)
    return;

for anio in anios:
    for instancia in instancias:
        for tipo in tipos:
            print(".\\excels\\" + instancia + "\\" + tipo + "\\" + anio + ".xlsx")
            try:
                path = ".\\excels\\" + instancia + "\\" + tipo + "\\" + anio + ".xlsx"
                procesarArchivo(anio,instancia,tipo,path)
                
                print("Detectado")
            except FileNotFoundError:
                print("No hubo " + instancia + " de " + tipo + " en el año " + anio)
            print()
            
            
