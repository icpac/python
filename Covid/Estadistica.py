
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
from scipy.stats import norm

nfile = "Covid\\220214COVID19MEXICO.csv"
#nfile= "Covid\\Prueba.csv"
dtypes = { "EDAD": int,
"FECHA_DEF": "category" }
df = pd.read_csv(nfile,
dtype=dtypes,
#parse_dates=["FECHA_DEF"],
usecols=list(dtypes))
#usecols=list(dtypes)+["FECHA_DEF"])

defunciones = df.query("FECHA_DEF != '9999-99-99'")
print("Defunciones:\n", defunciones)

"""
defunciones = df.FECHA_DEF.value_counts().sort_index()
print("Defunciones:\n", defunciones)"""

sr = defunciones["EDAD"]
print(defunciones.head)
media = sr.mean(axis=0)
std = sr.std(axis=0)
print("Media:", media)
print("Desviación estándar:", std)

print(sr)
print("Valores máximo-mínimo, Rango\n")
print(sr.max())
print(sr.min())
print(sr.max()-sr.min())


#plt.figure(figsize=[5, 5])
sr.plot.hist()
plt.title(f"Media: {media}, Std: {std}")

x_axis = np.arange(0, 120, 0.01)
  
  
plt.plot(x_axis, 5000000*norm.pdf(x_axis, media, std), linewidth=5.0, alpha=0.5)
#plt.axis('off')
#plt.gca().set_position([0, 0, 1, 1])
#plt.savefig("Covid\\test.svg")
plt.savefig("Covid\\test.svg", format="svg")
plt.show()