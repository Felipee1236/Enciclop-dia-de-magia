class MagiaClasse:
    def __init__(self, magia_id, classe_id):
        self.magia_id = magia_id
        self.classe_id = classe_id

    @staticmethod
    def associar_magia_classe(connection, magia_id, classe_id):
        cursor = connection.cursor()
        query = "INSERT INTO Magia_has_Classe (Magia_idMagia, Classe_idClasse) VALUES (%s, %s)"
        try:
            cursor.execute(query, (magia_id, classe_id))
            connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Erro ao associar magia à classe: {e}")
            cursor.close()
            return False

    @staticmethod
    def remover_associacao(connection, magia_id, classe_id):
        cursor = connection.cursor()
        query = "DELETE FROM Magia_has_Classe WHERE Magia_idMagia = %s AND Classe_idClasse = %s"
        cursor.execute(query, (magia_id, classe_id))
        connection.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        return affected_rows > 0

    @staticmethod
    def get_classes_por_magia(connection, magia_id):
        cursor = connection.cursor()
        query = """SELECT c.idClasse, c.Nome 
                   FROM Classe c 
                   JOIN Magia_has_Classe mc ON c.idClasse = mc.Classe_idClasse 
                   WHERE mc.Magia_idMagia = %s 
                   ORDER BY c.Nome"""
        cursor.execute(query, (magia_id,))
        results = cursor.fetchall()
        cursor.close()
        classes = []
        for result in results:
            classes.append({'id': result[0], 'nome': result[1]})
        return classes

    @staticmethod
    def get_magias_por_classe(connection, classe_id):
        cursor = connection.cursor()
        query = """SELECT m.idMagia, m.Nome, m.Nivel, m.Escola 
                   FROM Magia m 
                   JOIN Magia_has_Classe mc ON m.idMagia = mc.Magia_idMagia 
                   WHERE mc.Classe_idClasse = %s 
                   ORDER BY m.Nivel, m.Nome"""
        cursor.execute(query, (classe_id,))
        results = cursor.fetchall()
        cursor.close()
        magias = []
        for result in results:
            magias.append({
                'id': result[0], 
                'nome': result[1], 
                'nivel': result[2], 
                'escola': result[3]
            })
        return magias

    @staticmethod
    def get_todas_associacoes(connection):
        cursor = connection.cursor()
        query = """SELECT m.Nome as Magia, m.Nivel, c.Nome as Classe
                   FROM Magia m
                   JOIN Magia_has_Classe mc ON m.idMagia = mc.Magia_idMagia
                   JOIN Classe c ON mc.Classe_idClasse = c.idClasse
                   ORDER BY m.Nivel, m.Nome, c.Nome"""
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        associacoes = []
        for result in results:
            associacoes.append({
                'magia': result[0],
                'nivel': result[1],
                'classe': result[2]
            })
        return associacoes

