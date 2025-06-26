class Escritor:
    def __init__(self, id_escritor, nome):
        self.id_escritor = id_escritor
        self.nome = nome

    def create(self, connection):
        cursor = connection.cursor()
        query = "INSERT INTO Escritor (Nome) VALUES (%s)"
        cursor.execute(query, (self.nome,))
        connection.commit()
        self.id_escritor = cursor.lastrowid
        cursor.close()
        return self.id_escritor

    @staticmethod
    def read(connection, id_escritor):
        cursor = connection.cursor()
        query = "SELECT idEscritor, Nome FROM Escritor WHERE idEscritor = %s"
        cursor.execute(query, (id_escritor,))
        result = cursor.fetchone()
        cursor.close()
        if result:
            return Escritor(result[0], result[1])
        return None

    @staticmethod
    def read_all(connection):
        cursor = connection.cursor()
        query = "SELECT idEscritor, Nome FROM Escritor ORDER BY Nome"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        escritores = []
        for result in results:
            escritores.append(Escritor(result[0], result[1]))
        return escritores

    def update(self, connection):
        cursor = connection.cursor()
        query = "UPDATE Escritor SET Nome = %s WHERE idEscritor = %s"
        cursor.execute(query, (self.nome, self.id_escritor))
        connection.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        return affected_rows > 0

    @staticmethod
    def delete(connection, id_escritor):
        cursor = connection.cursor()
        query = "DELETE FROM Escritor WHERE idEscritor = %s"
        cursor.execute(query, (id_escritor,))
        connection.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        return affected_rows > 0

