import pandas as pd
    
    
anios = ["1993", "1995", "1997", "1999", "2001", "2003", "2005", "2007", "2009", "2011", "2013", "2015", "2017", "2019"]
instancias = ["PASO", "Primera vuelta", "Segunda vuelta"]
tipos = ["Diputados", "Presidente" ]#, "Senadores"]

def getNuevasColumnas(size):
    i = 0
    arr = []
    while i < size:
        arr.append(str(i))
    
    return arr

def procesarHoja (path,hoja):
    data_hoja = pd.read_excel(path,hoja);
    data_hoja.columns 
    retorno = {}
    data_hoja.columns = getNuevasColumnas(data_hoja.columns.size)
    #retorno['columna'] = data_hoja['col1']
    return data_hoja['0']


def procesarArchivo(anio, instancia, tipo, path):
    hojas = pd.ExcelFile(path).sheet_names
    hojas.pop(0)
    data = {}
    
    if int(anio) <= 2013:
        hojas.pop(-1)   
        
    for hoja in hojas:
        data[hoja] = procesarHoja(path,hoja)
    return data;

for anio in anios:
    for instancia in instancias:
        for tipo in tipos:
            print(".\\excels\\" + instancia + "\\" + tipo + "\\" + anio + ".xlsx")
            try:
                path = ".\\excels\\" + instancia + "\\" + tipo + "\\" + anio + ".xlsx"
                data = procesarArchivo(anio,instancia,tipo,path)
                
                print("Detectado")
            except FileNotFoundError:
                print("No hubo " + instancia + " de " + tipo + " en el año " + anio)
            print()
            
            
