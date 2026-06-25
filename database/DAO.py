from database.DB_connect import DBConnect


class DAO:
    @staticmethod
    def getNodes():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select g.Chromosome as cromosomi
from genes g
where g.Chromosome is not null and g.Chromosome !=0"""
        cursor.execute(query)

        for row in cursor:
            result.append(row['cromosomi'])
        cursor.close()
        conn.close()
        return result


    @staticmethod
    def getEdges():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
            select distinct c1.cromosomi as c1 ,c2.cromosomi as c2
from (
select g.Chromosome as cromosomi, g.GeneID as idA
from genes g
where g.Chromosome is not null and g.Chromosome !=0
)c1,
(select g.Chromosome as cromosomi, g.GeneID as idB
from genes g
where g.Chromosome is not null and g.Chromosome !=0)c2, interactions i 
where c1.cromosomi <>c2.cromosomi and c1.idA<>c2.idB and c1.ida =i.GeneID1 
and c2.idb =i.GeneID2 
"""
        cursor.execute(query)

        for row in cursor:
            result.append(row)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getPeso(cromosoma1,cromosoma2):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)

        query = """select sum( distinct i.Expression_Corr ) as peso
from genes g1, genes g2, interactions i
where i.GeneID1 =g1.GeneID and i.GeneID2 =g2.GeneID 
and g1.Chromosome =%s and g2.Chromosome =%s
"""
        cursor.execute(query, (cromosoma1,cromosoma2))

        row = cursor.fetchone()
        peso = row["peso"]

        cursor.close()
        conn.close()

        return peso