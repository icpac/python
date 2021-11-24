import psycopg2
from Config import config
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo
import sys

def get_movimientosB():
    """ query data from the vendors table """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('SELECT "Monto" FROM "MovimientoB"')
        print("The number of parts: ", cur.rowcount)
        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()



def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        params = config()
        conn = psycopg2.connect(**params)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1) 
    print("Connection successful")
    return conn


def postgresql_to_dataframe(conn, select_query, column_names):
    """
    Tranform a SELECT query into a pandas dataframe
    """
    cursor = conn.cursor()
    try:
        cursor.execute(select_query)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        cursor.close()
        return 1
    
    # Naturally we get a list of tupples
    tupples = cursor.fetchall()
    cursor.close()
    
    # We just need to turn it into a pandas dataframe
    df = pd.DataFrame(tupples, columns=column_names)
    return df


if __name__ == '__main__':
    # Connect to the database
    conn = connect()

    column_names = ["Monto", "Concepto"]
    # Execute the "SELECT *" query
    select = '''SELECT "Monto", "ConceptoB"."Clave" FROM "MovimientoB"
LEFT JOIN "ConceptoB"
ON "MovimientoB"."Concepto" = "ConceptoB"."Oid";'''
    df = postgresql_to_dataframe(conn, select, column_names)
    print(df.head())

    data = [go.Bar(x=df["Concepto"] , y=df["Monto"])]
    layout = go.Layout(title="Movimientos por Concepto",
                   xaxis= dict(title="Conceptos"),
                   yaxis= dict(title="Montos"),
                   barmode = "stack" )
    fig = go.Figure(data=data, layout=layout)
    fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
    pyo.plot(fig)    
    
    """
    get_movimientosB()"""


#https://towardsdatascience.com/python-and-postgresql-how-to-access-a-postgresql-database-like-a-data-scientist-b5a9c5a0ea43
#https://www.postgresqltutorial.com/postgresql-python/
#https://www.datacamp.com/community/tutorials/tutorial-postgresql-python?utm_source=adwords_ppc&utm_medium=cpc&utm_campaignid=1455363063&utm_adgroupid=65083631748&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=278443377086&utm_targetid=aud-299261629574:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=1010043&gclid=CjwKCAiA4veMBhAMEiwAU4XRr4yw6mSjKpMhb39uiUagmND9E6sXYZkoSbxyl1L6v6-Nkr6udvtNyRoC3agQAvD_BwE
#https://dbeaver.io/
