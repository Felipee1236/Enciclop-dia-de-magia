class Magia:
    def __init__(self, id_magia, nome, nivel, alcance, duracao, concentracao, escola, ritual, descricao, escritor_id):
        self.id_magia = id_magia
        self.nome = nome
        self.nivel = nivel
        self.alcance = alcance
        self.duracao = duracao
        self.concentracao = concentracao
        self.escola = escola
        self.ritual = ritual
        self.descricao = descricao
        self.escritor_id = escritor_id

    def create(self, connection):
        cursor = connection.cursor()
        query = """INSERT INTO Magia (Nome, Nivel, Alcance, Duracao, Concentracao, 
                   Escola, Ritual, Descricao, Escritor_idEscritor) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(query, (self.nome, self.nivel, self.alcance, self.duracao, 
                              self.concentracao, self.escola, self.ritual, 
                              self.descricao, self.escritor_id))
        connection.commit()
        self.id_magia = cursor.lastrowid
        cursor.close()
        return self.id_magia

    @staticmethod
    def read(connection, id_magia):
        cursor = connection.cursor()
        query = """SELECT idMagia, Nome, Nivel, Alcance, Duracao, Concentracao, 
                   Escola, Ritual, Descricao, Escritor_idEscritor 
                   FROM Magia WHERE idMagia = %s"""
        cursor.execute(query, (id_magia,))
        result = cursor.fetchone()
        cursor.close()
        if result:
            return Magia(result[0], result[1], result[2], result[3], result[4], 
                        result[5], result[6], result[7], result[8], result[9])
        return None

    @staticmethod
    def read_all(connection):
        cursor = connection.cursor()
        query = """SELECT idMagia, Nome, Nivel, Alcance, Duracao, Concentracao, 
                   Escola, Ritual, Descricao, Escritor_idEscritor 
                   FROM Magia ORDER BY Nivel, Nome"""
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        magias = []
        for result in results:
            magias.append(Magia(result[0], result[1], result[2], result[3], result[4], 
                               result[5], result[6], result[7], result[8], result[9]))
        return magias

    def update(self, connection):
        cursor = connection.cursor()
        query = """UPDATE Magia SET Nome = %s, Nivel = %s, Alcance = %s, 
                   Duracao = %s, Concentracao = %s, Escola = %s, Ritual = %s, 
                   Descricao = %s, Escritor_idEscritor = %s WHERE idMagia = %s"""
        cursor.execute(query, (self.nome, self.nivel, self.alcance, self.duracao, 
                              self.concentracao, self.escola, self.ritual, 
                              self.descricao, self.escritor_id, self.id_magia))
        connection.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        return affected_rows > 0

    @staticmethod
    def delete(connection, id_magia):
        cursor = connection.cursor()
        # Primeiro remove as associações com classes
        query_rel = "DELETE FROM Magia_has_Classe WHERE Magia_idMagia = %s"
        cursor.execute(query_rel, (id_magia,))
        
        # Depois remove a magia
        query = "DELETE FROM Magia WHERE idMagia = %s"
        cursor.execute(query, (id_magia,))
        connection.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        return affected_rows > 0

    @staticmethod
    def read_by_escola(connection, escola):
        cursor = connection.cursor()
        query = """SELECT idMagia, Nome, Nivel, Alcance, Duracao, Concentracao, 
                   Escola, Ritual, Descricao, Escritor_idEscritor 
                   FROM Magia WHERE Escola = %s ORDER BY Nivel, Nome"""
        cursor.execute(query, (escola,))
        results = cursor.fetchall()
        cursor.close()
        magias = []
        for result in results:
            magias.append(Magia(result[0], result[1], result[2], result[3], result[4], 
                               result[5], result[6], result[7], result[8], result[9]))
        return magias

    @staticmethod
    def read_by_nivel(connection, nivel):
        cursor = connection.cursor()
        query = """SELECT idMagia, Nome, Nivel, Alcance, Duracao, Concentracao, 
                   Escola, Ritual, Descricao, Escritor_idEscritor 
                   FROM Magia WHERE Nivel = %s ORDER BY Nome"""
        cursor.execute(query, (nivel,))
        results = cursor.fetchall()
        cursor.close()
        magias = []
        for result in results:
            magias.append(Magia(result[0], result[1], result[2], result[3], result[4], 
                               result[5], result[6], result[7], result[8], result[9]))
        return magias

