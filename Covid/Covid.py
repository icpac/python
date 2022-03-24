
__autor__ = "Tlacaelel Icpac"
__email__ = "tlacaelel.icpac@gmail.com"

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
from sklearn.metrics import r2_score
import datetime
import locale
from matplotlib.ticker import StrMethodFormatter

class Covid:
    def LeeDatos(self, file="Covid.csv"):
        """ Se leen los datos """
        #Leer archivo, separado por comas
        dtypes = {
            "DIABETES": "category",
            "HIPERTENSION": "category",
            "OBESIDAD": "category"
        }
        self.df = pd.read_csv(file, 
        dtype = dtypes,
        usecols=list(dtypes) + ["FECHA_DEF"],
        parse_dates=["FECHA_DEF"],
        encoding = "ISO-8859-1").set_index("FECHA_DEF")

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
        plt.title("Defunciones por Covid (Fuente: Datos abiertos gobierno de México)", fontsize=10)
        plt.suptitle("México, Del inicio hasta 3 Ene 2022", fontsize=18)
        plt.xticks(rotation=20)
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
        rol_defunc = sDefun.rolling(7)
        #rol_defunc.mean().plot(lw=.7)
        #rol_defunc.mean().plot.area()
        #s_fd.plot(label=lb, lw=0.5)

        defunSex = self.df.query('FECHA_DEF != "9999-99-99" & ENTIDAD_NAC < 33 & SEXO == 2')
        sSexDefun = defunSex.FECHA_DEF.value_counts().sort_index()
        sSexDefun.rename("HOMBRES", inplace=True)
        rol_sexDefunc = sSexDefun.rolling(7)

        #ndf = pd.concat([sDefun, sSexDefun], axis=1)
        ndf = pd.concat([rol_defunc.mean(), rol_sexDefunc.mean()], axis = 1)
        ndf.plot.area(stacked=False)
        print(ndf) 

        #rol_sexDefunc.mean().plot.area()

        plt.title("Defunciones por Covid", fontsize=10)
        plt.suptitle("México, -Dic 2021", fontsize=18)
        plt.xticks(rotation=25)
        plt.show()
        

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

    def Comorbilidad(self):
        """
        defunDia = self.df.query('FECHA_DEF != "9999-99-99" & ENTIDAD_NAC < 33 & DIABETES == 1')
        sDiab = defunDia.FECHA_DEF.value_counts().sort_index()
        sDiab.rename("DIABETES", inplace=True)
        #rol_diabe = sDiab.rolling(42)

        defunHip = self.df.query('FECHA_DEF != "9999-99-99" & ENTIDAD_NAC < 33 & HIPERTENSION == 1')
        sHip = defunHip.FECHA_DEF.value_counts().sort_index()
        sHip.rename("HIPERTENSION", inplace=True)
        #rol_hip = sHip.rolling(42)

        #ndf = pd.concat([rol_diabe.mean(), rol_hip.mean()], axis = 1)
        ndf = pd.concat([sDiab, sHip], axis = 1)
        ndf.index.rename("FECHA_DEF", inplace = True)
        print(ndf)

        # Converting the index as date
        ndf.index = pd.to_datetime(ndf.index)

        #ndf.reset_index(inplace=True)
        per = ndf.index.to_period("M")  # new way to get the same
        
        #ndf.index = pd.to_datetime(ndf['FECHA_DEF'], format='%m/%d/%y %I:%M%p')
        print(ndf.index)
        g = ndf.groupby(by=[ndf.index.month, ndf.index.year])        

        print(ndf)
        #g = ndf.groupby(per)        
        #g.sum()

        print(f"g: {g}")
        #ndf.pivot("column", "group", "val").plot(kind='bar')
        #ndf.plot(x='Team',"""
        
        """ Se enoja por Fecha_def
        ndf.plot(x='FECHA_DEF',
            kind='bar',
            stacked=False,
            title='Grouped Bar Graph with dataframe')"""
        #fig, ax = plt.subplots(figsize=(10,7))
        #ndf.groupby(['FECHA_DEF']).count()['DIABETES'].plot(ax=ax)
        #ndf.groupby(['FECHA_DEF']).count()['HIPERTENSION'].plot(ax=ax)
        """
        g.plot(
        kind='bar',
        stacked=False,
        title='Grouped Bar Graph with dataframe', ax=ax)"""

        """
        plt.title("Defunciones por Covid", fontsize=10)
        plt.suptitle("México, -Dic 2021", fontsize=18)
        plt.xticks(rotation=25)
        plt.show()"""

        #defun.plot(x='FECHA_DEF',
        #    kind='bar',
        #    stacked=False,
        #    title='Grouped Bar Graph with dataframe')
        #print(covi.df.tail())
        dfD = covi.df.query('FECHA_DEF != "9999-99-99" & (DIABETES == "1")')
        dfH = covi.df.query('FECHA_DEF != "9999-99-99" & (HIPERTENSION == "1")')
        #covi.df['FECHA_DEF'] = pd.to_datetime(covi.df['FECHA_DEF'])
        dfD.index = pd.to_datetime(dfD.index)
        dfH.index = pd.to_datetime(dfH.index)
        """
        print(covi.df.head())
        print(covi.df.index.min())
        print(covi.df.index.max())
        print(f"Tipos df: {covi.df.dtypes}")"""
        #print(type(covi.df.FECHA_DEF)) 
        #print(covi.df[0].FECHA_DEF.year)
        #n_by_state = covi.df.groupby([covi.df["FECHA_DEF"]])["DIABETES"].count()
        n_by_date  = dfD.groupby(by = [dfD.index.year, dfD.index.month])['DIABETES'].count()
        n_by_dateH = dfH.groupby(by = [dfH.index.year, dfH.index.month])['HIPERTENSION'].count()
        #n_by_date = covi.df.groupby(by = [covi.df.index.year, covi.df.index.month]).filter(lambda x: x['DIABETES'] == '1')

        #newDf = pd.concat(n_by_date, n_by_dateH) 
        newDf = pd.concat([n_by_date,n_by_dateH], axis=1) # 'index')
        #n_by_date.plot(kind='bar')
        newDf.plot(kind='bar')
        #n_by_state.head(10)  
        print(n_by_date)
        plt.title("Defunciones por Covid", fontsize=10)
        plt.suptitle("México, -Dic 2021", fontsize=18)
        plt.xticks(rotation=25)
            
        plt.show()


    def Comorbilidad2(self):
        """
        sDiab = defunDia.FECHA_DEF.value_counts().sort_index()
        sDiab.rename("DIABETES", inplace=True)
        #rol_diabe = sDiab.rolling(42)

        defunHip = self.df.query('FECHA_DEF != "9999-99-99" & ENTIDAD_NAC < 33 & HIPERTENSION == 1')
        sHip = defunHip.FECHA_DEF.value_counts().sort_index()
        sHip.rename("HIPERTENSION", inplace=True)
        #rol_hip = sHip.rolling(42)

        #ndf = pd.concat([rol_diabe.mean(), rol_hip.mean()], axis = 1)
        ndf = pd.concat([sDiab, sHip], axis = 1)
        ndf.index.rename("FECHA_DEF", inplace = True)
        print(ndf)

        # Converting the index as date
        ndf.index = pd.to_datetime(ndf.index)

        #ndf.reset_index(inplace=True)
        per = ndf.index.to_period("M")  # new way to get the same
        
        #ndf.index = pd.to_datetime(ndf['FECHA_DEF'], format='%m/%d/%y %I:%M%p')
        print(ndf.index)
        g = ndf.groupby(by=[ndf.index.month, ndf.index.year])        

        print(ndf)
        #g = ndf.groupby(per)        
        #g.sum()

        print(f"g: {g}")
        #ndf.pivot("column", "group", "val").plot(kind='bar')
        #ndf.plot(x='Team',"""
        
        """ Se enoja por Fecha_def
        ndf.plot(x='FECHA_DEF',
            kind='bar',
            stacked=False,
            title='Grouped Bar Graph with dataframe')"""
        #fig, ax = plt.subplots(figsize=(10,7))
        #ndf.groupby(['FECHA_DEF']).count()['DIABETES'].plot(ax=ax)
        #ndf.groupby(['FECHA_DEF']).count()['HIPERTENSION'].plot(ax=ax)
        """
        g.plot(
        kind='bar',
        stacked=False,
        title='Grouped Bar Graph with dataframe', ax=ax)"""

        """
        plt.title("Defunciones por Covid", fontsize=10)
        plt.suptitle("México, -Dic 2021", fontsize=18)
        plt.xticks(rotation=25)
        plt.show()"""

        #defun.plot(x='FECHA_DEF',
        #    kind='bar',
        #    stacked=False,
        #    title='Grouped Bar Graph with dataframe')
        #print(covi.df.tail())
        dfD = self.df.query('FECHA_DEF != "9999-99-99" & (DIABETES == "1")')
        dfH = self.df.query('FECHA_DEF != "9999-99-99" & (HIPERTENSION == "1")')
        dfO = self.df.query('FECHA_DEF != "9999-99-99" & (OBESIDAD == "1")')
        #covi.df['FECHA_DEF'] = pd.to_datetime(covi.df['FECHA_DEF'])
        dfD.index = pd.to_datetime(dfD.index)
        dfH.index = pd.to_datetime(dfH.index)
        dfO.index = pd.to_datetime(dfO.index)
        """
        print(covi.df.head())
        print(covi.df.index.min())
        print(covi.df.index.max())
        print(f"Tipos df: {covi.df.dtypes}")"""
        #print(type(covi.df.FECHA_DEF)) 
        #print(covi.df[0].FECHA_DEF.year)
        #n_by_state = covi.df.groupby([covi.df["FECHA_DEF"]])["DIABETES"].count()
        n_by_date  = dfD.groupby(by = [dfD.index.year, dfD.index.month])['DIABETES'].count()
        n_by_dateH = dfH.groupby(by = [dfH.index.year, dfH.index.month])['HIPERTENSION'].count()
        n_by_dateO = dfO.groupby(by = [dfO.index.year, dfO.index.month])['OBESIDAD'].count()
        #n_by_date = covi.df.groupby(by = [covi.df.index.year, covi.df.index.month]).filter(lambda x: x['DIABETES'] == '1')

        #newDf = pd.concat(n_by_date, n_by_dateH) 
        newDf = pd.concat([n_by_date,n_by_dateH, n_by_dateO], axis=1) # 'index')
        #n_by_date.plot(kind='bar')
        newDf.plot(kind='bar', stacked = True)
        #n_by_state.head(10)  
        print(n_by_date)
        plt.title("Defunciones por Covid (Datos abiertos Gob. Mex.)", fontsize=10)
        plt.suptitle("México, -Dic 2021", fontsize=18)
        plt.xticks(rotation=35)
            
        plt.show()

    def Correlacion(self):
        """ Se leen los datos """
        dtypes = {
            "NEUMONIA": "category",
            "DIABETES": "category",
            "EPOC": "category",
            "ASMA": "category",
            "INMUSUPR": "category",
            "HIPERTENSION": "category",
            "OTRA_COM": "category",
            "CARDIOVASCULAR": "category",
            "OBESIDAD": "category"
        }

        file = "Covid\\Prueba.csv"
        file = "Covid\\220103COVID19MEXICO.csv"
        self.df = pd.read_csv(file, 
        dtype = dtypes,
        usecols=list(dtypes) + ["FECHA_DEF"],
        parse_dates=["FECHA_DEF"],
        encoding = "ISO-8859-1").set_index("FECHA_DEF")

        dfD = self.df.query('FECHA_DEF != "9999-99-99"')
        dfD.index = pd.to_datetime(dfD.index)
        n_by_date  = dfD.groupby(by = [dfD.index.year, dfD.index.month]).count()
        print("Tipo date\n", type(n_by_date))
        print(n_by_date)
        #st = n_by_date["DIABETES"]
        st = n_by_date["INMUSUPR"]
        stc = st.cumsum()
        print(stc)

        self.PlotCorrelacion("DIABETES", stc)
        self.PlotCorrelacion("NEUMONIA", stc)
        self.PlotCorrelacion("EPOC", stc)
        self.PlotCorrelacion("ASMA", stc)
        self.PlotCorrelacion("INMUSUPR", stc)
        self.PlotCorrelacion("HIPERTENSION", stc)
        self.PlotCorrelacion("OTRA_COM", stc)
        self.PlotCorrelacion("OBESIDAD", stc)
        self.PlotCorrelacion("CARDIOVASCULAR", stc)
        

        #plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
        plt.legend(loc='upper left', borderaxespad=0.)
        plt.show()


        
    def PlotCorrelacion(self, campo, stc):
        dfDia = self.df.query('FECHA_DEF != "9999-99-99" & (' + campo + ' == "1")')
        dfDia.index = pd.to_datetime(dfDia.index)
        n_by_dateDia  = dfDia.groupby(by = [dfDia.index.year, dfDia.index.month])[campo].count()
        #nstc = n_by_dateDia.cumsum()
        nstc = n_by_dateDia
        
        df=pd.concat([stc,nstc],axis=1)

        nss = df.iloc[:, 0]

        plt.scatter(nss, df.iloc[:, 1], label=campo)

    def Histograma(self):
        #file = "Covid\\Prueba.csv"
        file = "Covid\\220103COVID19MEXICO.csv"
        self.df = pd.read_csv(file,
        usecols=["FECHA_SINTOMAS", "FECHA_DEF", "DIABETES"],
        parse_dates=["FECHA_SINTOMAS", "FECHA_DEF"])
        """
        self.df['FECHA_INGRESO'] = self.df['FECHA_INGRESO'].astype('datetime64[ns]')
        self.df['FECHA_DEF'] = self.df['FECHA_DEF'].astype('datetime64[ns]')"""

        ndfDef = self.df.query('FECHA_DEF != "9999-99-99"')
        #ndfDef['FECHA_DEF'] = ndfDef['FECHA_DEF'].astype('datetime64[ns]')
        ndfDef['FECHA_DEF'] = pd.to_datetime(ndfDef['FECHA_DEF'])#, format='%d%b%Y')

        print(f"Shape: {ndfDef.shape}")
        print(f"Tipos: {ndfDef.dtypes}")
        
        ndfDef[['FECHA_SINTOMAS','FECHA_DEF']] = ndfDef[['FECHA_SINTOMAS','FECHA_DEF']].apply(pd.to_datetime) #if conversion required
        ndfDef['C'] = (ndfDef['FECHA_DEF'] - ndfDef['FECHA_SINTOMAS']).dt.days        

        diasDf  = ndfDef.query('C > 63')
        print(diasDf.sort_values("C").tail())
        ax = diasDf.hist(column="C", bins=25, grid=False,figsize=(10,6), color='#86bf91', zorder=2, rwidth=0.9)
        ax = ax[0]
        for x in ax:
            # Despine
            x.spines['right'].set_visible(False)
            x.spines['top'].set_visible(False)
            x.spines['left'].set_visible(False)

            # Switch off ticks
            x.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="off", right="off", labelleft="on")

            # Draw horizontal axis lines
            vals = x.get_yticks()
            for tick in vals:
                x.axhline(y=tick, linestyle='dashed', alpha=0.4, color='#eeeeee', zorder=1)

            # Remove title
            x.set_title("")

            # Set x-axis label
            x.set_xlabel("Duración con Síntomas (días)", labelpad=20, weight='bold', size=12)

            # Set y-axis label
            x.set_ylabel("Pacientes", labelpad=20, weight='bold', size=12)

            # Format y-axis label
            x.yaxis.set_major_formatter(StrMethodFormatter('{x:,g}'))        
            
            
        plt.title("Histograma de Duración con Sintomas")
        plt.legend(loc='upper left', borderaxespad=0.)        
        plt.show()


    def DonutChart(self):
        # https://towardsdatascience.com/donut-plot-for-data-analysis-5aacac591741
        # https://www.analyticsvidhya.com/blog/2021/06/donut-plots-data-visualization-with-python/
        file = "Covid\\Prueba.csv"
        file = "Covid\\220103COVID19MEXICO.csv"

        df = pd.read_csv(file,
        usecols=["ENTIDAD_NAC", "FECHA_DEF", "DIABETES"],
        parse_dates=["FECHA_DEF"])

        defun = df.query('FECHA_DEF != "9999-99-99" & ENTIDAD_NAC < 33')
        """
        defunciones = defun.FECHA_DEF.value_counts().sort_index()
        print(type(defunciones))
        print(defunciones.tail())
        print(defunciones)"""

        x = df.groupby(defun.ENTIDAD_NAC).size()
        print(type(x))
        print(x.tail())
        index_values = [ 'Ags', 'BC', "BCS", "Camp", "Coah",
        "Col", "Chis", "Chih", "CDMx", "Dgo", "Gto", "Gro", "Hgo",
        "Jal", "EdoMex", "Mich", "Mor", "Nay", "NL", "Oax", "Pue",
        "Qro", "QRoo", "SLP", "Sin", "Son", "Tab", "Tamps", "Tlax",
        "Ver", "Yuc", "Zac"]
        
        x.index = index_values
        #data = x.sort_values(ascending=False)
        data = x

        plt.title("Covid por Estado")
        total = sum(data)
        print(total)
        data_per = data/total*100
        print(data_per)
        explode = (0, 0, 0, 0, 0, 0,
        0,0,0.2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
        #plt.pie(data, explode=explode, labels = [round(i,2) for i in (list(data_per))])
        plt.pie(data, explode=explode, labels = index_values)
        circle = plt.Circle((0,0), 0.5, color='white')
        p=plt.gcf()
        p.gca().add_artist(circle)
        plt.show()

    def GraphBubble(self):
        """ Se leen los datos """
        dtypes = {
            "NEUMONIA": "category",
            "DIABETES": "category",
            "EPOC": "category",
            "ASMA": "category",
            "INMUSUPR": "category",
            "HIPERTENSION": "category",
            "OTRA_COM": "category",
            "CARDIOVASCULAR": "category",
            "OBESIDAD": "category"
        }

        file = "Covid\\Prueba.csv"
        #file = "Covid\\220103COVID19MEXICO.csv"
        #DataFrame
        df = pd.read_csv(file, 
        dtype = dtypes,
        usecols=list(dtypes) + ["FECHA_DEF"],
        parse_dates=["FECHA_DEF"],
        encoding = "ISO-8859-1").set_index("FECHA_DEF")

        #DataFrame
        dfD = df.query('FECHA_DEF != "9999-99-99"')
        dfD.index = pd.to_datetime(dfD.index)

        #DataFrame
        n_by_date  = dfD.groupby(by = [dfD.index.year, dfD.index.month]).count()

        print("Tipo date\n", type(n_by_date))
        print(n_by_date.tail())

        #st = n_by_date["DIABETES"]
        print(f"Shape: {len(n_by_date.index)}")
        datax = np.arange(len(n_by_date.index))
        print(f"Datax: {datax}")
        
        
        st = n_by_date["INMUSUPR"]
        stc = st.cumsum()
        stc = st
        print(stc)


        campo = "DIABETES"
        dfDia = df.query('FECHA_DEF != "9999-99-99" & (' + campo + ' == "1")')
        dfDia.index = pd.to_datetime(dfDia.index)
        n_by_dateDia  = dfDia.groupby(by = [dfDia.index.year, dfDia.index.month])[campo].count()
        std = n_by_dateDia[campo]




        np.random.seed(42)
        N = 100
        N = len(n_by_date.index)
        N = len(n_by_dateDia.index)
        x = np.random.normal(170, 20, N)
        x = np.arange(N)
        y = x + np.random.normal(5, 25, N)
        y = x + stc
        colors = np.random.rand(N)
        colors = np.empty(N); 
        colors = np.full(N, "#88c999")
        colorsD = np.full(N, "#88c888")

        area = (25 * np.random.rand(N))**2
        area = (.0025 * y)**2
        areaD = (.0025 * std)**2
        df = pd.DataFrame({
        'X': np.append(x, x),
        'Y': y.append(std),
        'Colors': np.append(colors, colorsD),
        "bubble_size":area.append(areaD)})

        print(f"Df: {df}")
        """
        dfD = pd.DataFrame({
            'X': x,
            'Y': std,
            "bubble_size": (.0025 * std)**2})"""

        print(df.head(n=3))
        # scatter plot with scatter() function
        """
        plt.scatter('X', 'Y', data=df)
        plt.xlabel("X", size=16)
        plt.ylabel("y", size=16)
        plt.title("Scatter Plot with Matplotlib", size=18)"""

        """
        # scatter plot with scatter() function
        # transparency with "alpha"
        # bubble size with "s"
        plt.scatter('X', 'Y', 
             s='bubble_size',
             alpha=0.5, 
             data=df)
        plt.xlabel("X", size=16)
        plt.ylabel("y", size=16)
        plt.title("Bubble Plot with Matplotlib", size=18)"""

        # scatter plot with scatter() function
        # transparency with "alpha"
        # bubble size with "s"
        # color the bubbles with "c"
        plt.scatter('X', 'Y',
             s='bubble_size',
             c='Colors',
             alpha=0.5, data=df)

        plt.xlabel("X", size=16)
        plt.ylabel("y", size=16)
        plt.title("Bubble Plot with Colors: Matplotlib", size=18)

        plt.show()



if __name__ == "__main__":
    # Set max rows displayed in output to 25
    pd.set_option("display.max_rows", 25)

    covi = Covid()
    # Cada uno lo lee
    #covi.LeeDatos(file="Covid\\220103COVID19MEXICO.csv")
    #covi.LeeDatos(file="Covid\\Prueba.csv")
    #covi.Comorbilidad2()


    #covi.MuestraPorSexo()
    #covi.MuestraPorEstado()
    #covi.Miq(covi.df, leg=False, txleg="")
    #covi.ComportamientoSexo()
    #covi.Comorbilidad()
    #covi.Correlacion()
    #covi.Histograma()
    #covi.DonutChart()
    covi.GraphBubble()

    #plot = x.plot.pie(y=x.index, figsize=(5, 5), autopct='%1.1f%%')
   
    # Print the series
    #print(sr)
    # find the value counts
    #print(sr.value_counts())

    #covi.Ingreso()
    #covi.Diabetes()
    #plt.show()
