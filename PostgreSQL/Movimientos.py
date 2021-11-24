import psycopg2
from Config import config

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


if __name__ == '__main__':
    get_movimientosB()


#https://towardsdatascience.com/python-and-postgresql-how-to-access-a-postgresql-database-like-a-data-scientist-b5a9c5a0ea43
#https://www.postgresqltutorial.com/postgresql-python/
#https://www.datacamp.com/community/tutorials/tutorial-postgresql-python?utm_source=adwords_ppc&utm_medium=cpc&utm_campaignid=1455363063&utm_adgroupid=65083631748&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=278443377086&utm_targetid=aud-299261629574:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=1010043&gclid=CjwKCAiA4veMBhAMEiwAU4XRr4yw6mSjKpMhb39uiUagmND9E6sXYZkoSbxyl1L6v6-Nkr6udvtNyRoC3agQAvD_BwE
#https://dbeaver.io/
