
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
    def Datos(self):
        #Leer archivo, separado por comas
        nf = "200901COVID19MEXICO.csv"
        #nf = "Covi.csv" 
        self.df = pd.read_csv(nf, encoding = "ISO-8859-1")

    def Estado(self, edo):
        return self.df[self.df['ENTIDAD_RES'] == edo]
    
    def Miq(self, df, leg, txleg):
        "Se usa la columna FECHA DEF para saber cuántos decesos hay"
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
        s_fd.plot(label=lb, lw=0.5)
        #self.ProyLineal(rol_defunc)
        self.ProyPoly(rol_defunc, txleg)

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
        s_fd = pd.Series(df.FECHA_DEF)

        #Otra serie de los datos pero, contando cuántos por FECHA_DEF
        s_fdc = pd.Series(df.FECHA_DEF.value_counts())
        s_fdc = pd.Series(df.FECHA_DEF.value_counts().sort_index())
                  #[:-1])

        rol_defunc = s_fdc.rolling(7)

        #Imprimimos la serie
        print(s_fd)
        #Imprimimos la otra serie
        print(s_fdc)


covi = Covid()
covi.Datos()
#covi.Miq()
covi.Ingreso()
covi.Diabetes()
plt.show()
