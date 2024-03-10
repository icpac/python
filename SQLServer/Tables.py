
import pyodbc  
import configparser

class SqlCodigo():
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('SQLServer\config.ini')

        self.SERVER = config.get('Configuracion', 'SERVER')
        self.DATABASE = config.get('Configuracion', 'DATABASE')
        self.USERNAME = 'sa'
        self.PASSWORD = config.get('Configuracion', 'PASSWORD')

    def conexion(self):
        connectionString  = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.SERVER};DATABASE={self.DATABASE};UID={self.USERNAME};PWD={self.PASSWORD};Encrypt=No'
        self.conn = pyodbc.connect(connectionString)

    def cursor(self):        
        self.curs = self.conn.cursor()

    def manejadores(self):
        print(pyodbc.drivers())

    def cabezaModelo(self, lineas, tabla):
        lineas.append("")
        lineas.append("Table")
        lineas.append("")
        lineas.append(tabla[2]) 
        nomtabla = str(tabla[2]).lower()
        lineas.append(f"List<{str(tabla[2])}Model> {nomtabla}Init = new List<{str(tabla[2])}Model>();")
        lineas.append(f"modelBuilder.Entity<{str(tabla[2])}Model>({nomtabla} =>")
        lineas.append("{")
        lineas.append(f'{nomtabla}.ToTable("{str(tabla[2])}");')
        return lineas

    def propiedadesContext(self):
        """
        column_data = curs.columns(table=row[2], catalog=DATABASE, schema='dbo').fetchall()
        for col in column_data:
            if col[3] == "Id":
                lineas.append(f"{nomtabla}.HasKey(x => x.Id);")
            else:                
                lineas.append(f"{nomtabla}.Property(x => x.{col[3]});")  
        lineas.append(f"{nomtabla}.HasData({nomtabla}Init);")
        lineas.append("});")"""


    def codigoClase(self, lineas, columns, tabla):
        lineas.append("")
        lineas.append("")
        lineas.append(f"    public class {str(tabla[2])}Model")
        lineas.append("{")
        
        for col in columns:
            if col[3] == "Id":
                lineas.append(f"\tpublic int Id {{ get; set; }}")
            else:        
                if col[5] == "int":
                    lineas.append(f"\tpublic int {col[3]} {{ get; set; }}")
                elif col[5] == "datetime":
                    lineas.append(f"\tpublic DateTime {col[3]} {{ get; set; }}")
                elif col[5] == "bit" or col[5] == "varbinary":
                    lineas.append(f"\tpublic bool {col[3]} {{ get; set; }}")
                elif col[5] == "nvarchar" or col[5] == "nchar":
                    lineas.append(f"\tpublic string {col[3]} {{ get; set; }}")
                elif col[5] == "varbinay":
                    lineas.append(f"\tpublic byte[] {col[3]} {{ get; set; }}")
                elif col[5] == "numeric":
                    lineas.append(f"\tpublic double {col[3]} {{ get; set; }}")
                else:
                    lineas.append(f"nosta {col[5]}  ************************************************")
        lineas.append("}")
        return lineas


    def creaCodigoTabla(self, tabla):
        lineas = []
        columns = self.curs.columns(table=tabla[2], catalog=self.DATABASE, schema='dbo').fetchall()
        lineas = self.codigoClase(lineas, columns, tabla)
        return lineas
  

    def creaArchivoCodigo(self, lineas, nomTabla):
        n_names = ["{}\n".format(i) for i in lineas]
        nomComp = f'C:\iCPAC\Proyectos\C#\Codigo\{nomTabla}.cs'
        with open(nomComp, 'w') as fp:
            fp.writelines(n_names)
   

    def creaCodigo(self):
        self.conexion()
        self.cursor()
        for tabla in self.curs.tables(tableType = 'TABLE').fetchall():
            linea = self.creaCodigoTabla(tabla)
            self.creaArchivoCodigo(linea, tabla[2])



src = SqlCodigo()
src.manejadores()
src.creaCodigo()

print("Termino")