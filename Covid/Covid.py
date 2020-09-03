
__autor__ = "Tlacaelel Icpac"
__email__ = "tlacaelel.icpac@gmail.com"

import pandas as pd
import matplotlib.pyplot as plt

class Covid:
    def Datos(self):
        #Leer archivo, separado por comas
        nf = "200901COVID19MEXICO.csv"
        #nf = "Covi.csv" 
        self.df = pd.read_csv(nf, encoding = "ISO-8859-1")


    def Miq(self):
        print("Total de Registros : ", len(self.df.index))
        print("Total de Defunciones: ", len(self.df.FECHA_DEF.value_counts().sort_index()[:-1]))
        # deberían salir como 65 mil
        sm = self.df.FECHA_DEF.value_counts().sort_index()[:-1]
        print(sm)
        print(sm.sum())
        print("Último:", self.df.FECHA_DEF.value_counts().sort_index()[-1])

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
