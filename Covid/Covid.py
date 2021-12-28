
__autor__ = "Tlacaelel Icpac"
__email__ = "tlacaelel.icpac@gmail.com"

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
from sklearn.metrics import r2_score
import datetime
import locale

class Covid:
    def LeeDatos(self, file="Covid.csv"):
        """ Se leen los datos """
        #Leer archivo, separado por comas
        #nf = "200901COVID19MEXICO.csv"
        nf = "D:\iCPAC\Git\python\Covid\\"
        nf += "211005COVID19MEXICO.csv"
        #nf = "Covi.csv" 
        self.df = pd.read_csv(file, encoding = "ISO-8859-1")

    def Estado(self, edo):
        return self.df[self.df['ENTIDAD_RES'] == edo]
    
    def Miq(self, df, leg, txleg):
        """Se usa la columna FECHA DEF para saber cuántos decesos hay"""
        defunciones = df.FECHA_DEF.value_counts().sort_index()

        print(f"Total de Registros: {len(df.index):,}")
        print(f"Total Fechas distintas: {len(defunciones[:-1]):,}")
        print(f"Cuantos muertos hay: {defunciones[:-1].sum():,}")
        print(f"Sobrevivientes: {defunciones[-1]:,}")
        print(f"Total = defunciones + sobrevivientes: {len(df.index):,} ="
              f" {defunciones[:-1].sum():,} + {defunciones[-1]:,}")

        s_fd = pd.Series(defunciones[:-1])
        rol_defunc = s_fd.rolling(7)

        lbm = "Media, defunciones"
        lb = "Defunciones"
        if leg == False:
            lb = ""
            lbm = ""

        rol_defunc.mean().plot(lw=.7, label=lbm)
        #rol_defunc.mean().plot.area()
        #s_fd.plot(label=lb, lw=0.5)
        plt.title("Defunciones por Covid", fontsize=10)
        plt.suptitle("México, -Dic 2021", fontsize=18)
        plt.xticks(rotation=45)
        plt.show()
        #self.ProyLineal(rol_defunc)
        #self.ProyPoly(rol_defunc, txleg)

    def Ingreso(self):
        s_fi = pd.Series(self.df.FECHA_INGRESO.value_counts().sort_index())
        rol_defunc = s_fi.rolling(7)
        rol_defunc.mean().plot(lw=3)
        #rol_defunc.sum().plot(lw=3)
        #rol_defunc.count().plot(lw=3)

        """ Media
        rol2_defunc = s_fi.rolling(14)
        rol2_defunc.mean().plot(lw=3)

        rol3_defunc = s_fi.rolling(21)
        rol3_defunc.mean().plot(lw=3)"""
        
        s_fi.plot()
        plt.title("Fecha de Ingreso con su media ventana 7 días")
        #plt.show()

    def Diabetes(self):
        x = self.df.groupby(self.df.DIABETES)
        #x = df.query("DIABETES == 2")['Y'].sum()
        x = self.df.query("DIABETES == 1")

        s_fi = pd.Series(x.FECHA_INGRESO.value_counts().sort_index())
        rol_defunc = s_fi.rolling(7)
        rol_defunc.mean().plot(lw=3, label="Diabetes")        

            
    def Otro(self):
        #Obtener una serie de los datos leidos, con la columna FECHA_DEF
        s_fd = pd.Series(self.df.FECHA_DEF)

        #Otra serie de los datos pero, contando cuántos por FECHA_DEF
        s_fdc = pd.Series(self.df.FECHA_DEF.value_counts())
        s_fdc = pd.Series(self.df.FECHA_DEF.value_counts().sort_index())
                  #[:-1])

        rol_defunc = s_fdc.rolling(7)

        #Imprimimos la serie
        print(s_fd)
        #Imprimimos la otra serie
        print(s_fdc)

    def MuestraPorSexo(self):
        dfDefSex = self.df[["FECHA_DEF", "SEXO"]]
        #covi.df['SEXO'].replace(1, 'Female',inplace=True)
        #covi.df['SEXO'].replace(2, 'Male',inplace=True)    
        x = self.df.groupby(self.df.SEXO).size()
        #x['SEXO'].replace(1, 'Female',inplace=True)
        #x['SEXO'].replace(2, 'Male',inplace=True)    
        index_values = [ 'Female', 'Male' ]
        x.index = index_values
        print(f"X:{x}")
        #plot = x.plot.pie(y='SEXO', figsize=(4, 4), autopct='%1.1f%%', shadow=True, startangle=45)
        plot = x.plot.pie(figsize=(4, 4), autopct='%1.1f%%', shadow=True, startangle=45)
        plt.title("Covid por SEXO")
        plt.axis('equal')
        plt.tight_layout()
        plt.show()

    def MuestraPorEstado(self):
        defun = self.df.query('FECHA_DEF != "9999-99-99" & ENTIDAD_NAC < 33')
        defunciones = defun.FECHA_DEF.value_counts().sort_index()
        print(defunciones)
        x = self.df.groupby(defun.ENTIDAD_NAC).size()
        index_values = [ 'AS', 'BC', "BS", "CC", "CL",
        "CM", "CS", "CH", "DF", "DG", "GT", "GR", "HG",
        "JC", "MC", "MN", "MS", "NT", "NL", "OC", "PL",
        "QT", "QR", "SP", "SL", "SR", "TC", "TS", "TL",
        "VZ", "YN", "ZS"]
        x.index = index_values
        #plot = x.plot.pie(figsize=(4, 4), autopct='%1.1f%%', shadow=True, startangle=45)
        y = x.sort_values(ascending=False)
        ax = y.plot(kind='bar')
        plt.title("Covid por Estado")
        #plt.axis('equal')
        #plt.tight_layout()
        plt.show()
    
    def ComportamientoSexo(self):
        """Se usa la columna FECHA DEF para saber cuántos decesos hay"""
        #DataFrame, sólo con fecha de defunción y de méxico
        defun = self.df.query('FECHA_DEF != "9999-99-99" & ENTIDAD_NAC < 33')
        #Serie 
        sDefun = defun.FECHA_DEF.value_counts().sort_index()
        sDefun.rename("TODOS", inplace=True)
        #rol_defunc = sDefun.rolling(7)
        #rol_defunc.mean().plot(lw=.7)
        #rol_defunc.mean().plot.area()
        #s_fd.plot(label=lb, lw=0.5)

        defunSex = self.df.query('FECHA_DEF != "9999-99-99" & ENTIDAD_NAC < 33 & SEXO == 2')
        sSexDefun = defunSex.FECHA_DEF.value_counts().sort_index()
        sSexDefun.rename("HOMBRES", inplace=True)

        ndf = pd.concat([sDefun, sSexDefun], axis=1)
        ndf.plot.area(stacked=False)
        print(ndf) 

        #rol_sexDefunc = sSexDefun.rolling(7)
        #rol_sexDefunc.mean().plot.area()

        plt.title("Defunciones por Covid", fontsize=10)
        plt.suptitle("México, -Dic 2021", fontsize=18)
        plt.xticks(rotation=25)
        plt.show()
        

        print("ahi vamos")
        """
        s_fd = pd.Series(defunciones[:-1])
        rol_defunc = s_fd.rolling(7)"""

        """
        rol_defunc.mean().plot(lw=.7, label=lbm)
        #rol_defunc.mean().plot.area()
        #s_fd.plot(label=lb, lw=0.5)
        plt.title("Defunciones por Covid", fontsize=10)
        plt.suptitle("México, -Dic 2021", fontsize=18)
        plt.xticks(rotation=45)
        plt.show()"""




if __name__ == "__main__":
    covi = Covid()
    covi.LeeDatos(file="Covid\\211220COVID19MEXICO.csv")
    #covi.LeeDatos(file="Covid\\Prueba.csv")

    #covi.MuestraPorSexo()
    #covi.MuestraPorEstado()
    #covi.Miq(covi.df, leg=False, txleg="")
    covi.ComportamientoSexo()

    #plot = x.plot.pie(y=x.index, figsize=(5, 5), autopct='%1.1f%%')
   
    # Creating the Series
    #sr = pd.Series(['New York', 'Chicago', 'Toronto', 'Lisbon', 'Rio', 'Chicago', 'Lisbon'])
    
    # Print the series
    #print(sr)
    # find the value counts
    #print(sr.value_counts())

    #covi.Ingreso()
    #covi.Diabetes()
    #plt.show()
