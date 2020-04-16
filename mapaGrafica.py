import networkx as nx
import matplotlib.pyplot as plt

#1 Baja California
#2 Baja California Sur
#3 Sonora
#4 Chihuahua
#5 Sinaloa
#6 Durango
#7 Coahuila
#8 Nayarit
#9 Jalisco
#10 Zacatecas
#11 San Luis Potosi
#12 Nuevo León
#13 Colima
#14 Michoacan
#15 Guanajuato
#16 Aguascalientes
#17 Queretaro
#18 Hidalgo
#19 Veracruz
#20 Tamaulipas
#21 Estado de México
#22 Tlaxcala
#23 Puebla
#24 Oaxaca
#25 Chiapas
#26 Tabasco
#27 Guerrero
#28 Morelos
#29 Ciudad de Mexico
#30 Campeche
#31 Yucatán
#32 Quintana Roo
"""
nodos = [('1', '2', {'weight':8}) , ('1', '3'),
         ('3', '4'), ('3', '5'),
         ('4', '5'), ('4', '6'), ('4', '7'),
         ('5', '6'), ('5', '8'),
         ('6', '8'), ('6', '9'), ('6', '10'), ('6', '7'),
         ('7', '10'), ('7', '11'), ('7', '12'),
         ('8', '9'), ('8', '10'),
         ('9', '13'), ('9', '14'), ('9', '15'), ('9', '11'), ('9', '10'), ('9', '16'),
         ('10', '16'), ('10', '15'), ('10', '11'), ('10', '12'),
         ('11', '12'), ('11', '15'), ('11', '17'), ('11', '18'), ('11', '19'), ('11', '20'),
         ('12', '20'),
         ('13', '14'),
         ('14', '15'), ('14', '17'),
         ('15', '17'),

         ('17', '21'), ('17', '18'),
         ('18', '21'), ('18', '22'), ('18', '23'), ('18', '19'),
         ('19', '20'), ('19', '23'), ('19', '24'), ('19', '25'), ('19', '26'),

         ('21', '27'), ('21', '28'), ('21', '29'), ('21', '23'), ('21', '22'),
         ('22', '23'),
         ('23', '28'), ('23', '27'), ('23', '24'),
         ('24', '25'), ('24', '27'),
         ('25', '26'),
         ('26', '30'),
         ('27', '28'),
         ('28', '29'),
         
         ('30', '31'), ('30', '32'),
         ('31', '32'),
     ]
"""

g = nx.Graph()
g.add_node('BC1', pos=(5, 18))
g.add_node('BS2', pos=(7, 12))

g.add_node('SN3', pos=(8, 17))
g.add_edge('BC1', 'SN3')

g.add_node('CH4', pos=(12, 16))
g.add_edge('SN3', 'CH4')

g.add_node('SI5', pos=(11, 11))
g.add_edge('SN3', 'SI5')

g.add_node('CO7', pos=(16, 14))
g.add_edge('CH4', 'SI5')
g.add_edge('CH4', 'CO7')

g.add_node('DR6', pos=(13, 12))
g.add_edge('SI5', 'DR6')
g.add_edge('CH4', 'DR6')

g.add_node('NY8', pos=(14, 8))
g.add_edge('SI5', 'NY8')
g.add_edge('DR6', 'NY8')

g.add_node('JL9', pos=(14, 6))
g.add_edge('DR6', 'JL9')
g.add_edge('DR6', 'CO7')

g.add_node('ZC10', pos=(15, 10))
g.add_edge('DR6', 'ZC10')

g.add_edge('BC1', 'BS2')

g.add_node('SN11', pos=(18, 9))
g.add_node('NL12', pos=(19, 13))
g.add_node('CL13', pos=(14, 5))
g.add_node('MC14', pos=(16, 5))
g.add_node('GT15', pos=(17, 7))
g.add_node('AG16', pos=(16, 9))
g.add_node('QR17', pos=(19, 8))
g.add_node('HG18', pos=(20, 7))
g.add_node('VR19', pos=(23, 6))
g.add_node('TM20', pos=(21, 10))
g.add_node('ED21', pos=(19, 5.5))
g.add_node('TX22', pos=(21, 5.5))
g.add_node('PB23', pos=(21, 5))
g.add_node('OX24', pos=(22.5, 2.5))
g.add_node('CP25', pos=(27, 2.5))
g.add_node('TB26', pos=(26, 4.5))
g.add_node('GR27', pos=(18, 3))
g.add_node('MR28', pos=(19.5, 4.5))
g.add_node('CD29', pos=(19.5, 5))
g.add_node('CM30', pos=(29, 5))
g.add_node('YC31', pos=(30, 8))
g.add_node('QR32', pos=(31, 6))


g.add_edge('CO7', 'ZC10')
g.add_edge('CO7', 'SN11')
g.add_edge('CO7', 'NL12')

g.add_edge('NY8', 'JL9')
g.add_edge('NY8', 'ZC10')

g.add_edge('JL9', 'ZC10')
g.add_edge('JL9', 'SN11')
g.add_edge('JL9', 'CL13')
g.add_edge('JL9', 'MC14')
g.add_edge('JL9', 'GT15')
g.add_edge('JL9', 'AG16')

g.add_edge('ZC10', 'SN11')
g.add_edge('ZC10', 'NL12')
g.add_edge('ZC10', 'GT15')
g.add_edge('ZC10', 'AG16')

g.add_edge('SN11', 'NL12')
g.add_edge('SN11', 'GT15')
g.add_edge('SN11', 'QR17')
g.add_edge('SN11', 'HG18')
g.add_edge('SN11', 'VR19')
g.add_edge('SN11', 'TM20')

g.add_edge('NL12', 'TM20')

g.add_edge('CL13', 'MC14')

g.add_edge('MC14', 'GT15')
g.add_edge('MC14', 'QR17')

g.add_edge('GT15', 'QR17')

g.add_edge('QR17', 'HG18')
g.add_edge('QR17', 'ED21')

g.add_edge('HG18', 'VR19')
g.add_edge('HG18', 'ED21')
g.add_edge('HG18', 'TX22')
g.add_edge('HG18', 'PB23')

g.add_edge('VR19', 'TM20')
g.add_edge('VR19', 'PB23')
g.add_edge('VR19', 'OX24')
g.add_edge('VR19', 'CP25')
g.add_edge('VR19', 'TB26')

g.add_edge('ED21', 'MC14')
g.add_edge('ED21', 'TX22')
g.add_edge('ED21', 'PB23')
g.add_edge('ED21', 'GR27')
g.add_edge('ED21', 'MR28')
g.add_edge('ED21', 'CD29')

g.add_edge('TX22', 'PB23')

g.add_edge('PB23', 'OX24')
g.add_edge('PB23', 'GR27')
g.add_edge('PB23', 'MR28')

g.add_edge('OX24', 'CP25')
g.add_edge('OX24', 'GR27')

g.add_edge('CP25', 'TB26')

g.add_edge('TB26', 'CM30')

g.add_edge('GR27', 'MR28')
g.add_edge('GR27', 'MC14')

g.add_edge('MR28', 'CD29')

g.add_edge('CM30', 'YC31')
g.add_edge('CM30', 'QR32')

g.add_edge('YC31', 'QR32')

#g = nx.Graph(nodos)
#g['1']['2']['weight'] = 8

pos = nx.get_node_attributes(g, 'pos')
plt.grid(True)
nx.draw(g, pos, with_labels=True)
print (nx.degree(g, 'GR27'))


plt.show()
