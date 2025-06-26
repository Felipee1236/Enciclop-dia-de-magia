class Classe:
    def __init__(self, id_classe, nome):
        self.id_classe = id_classe
        self.nome = nome

    def create(self, connection):
        cursor = connection.cursor()
        query = "INSERT INTO Classe (Nome) VALUES (%s)"
        cursor.execute(query, (self.nome,))
        connection.commit()
        self.id_classe = cursor.lastrowid
        cursor.close()
        return self.id_classe

    @staticmethod
    def read(connection, id_classe):
        cursor = connection.cursor()
        query = "SELECT idClasse, Nome FROM Classe WHERE idClasse = %s"
        cursor.execute(query, (id_classe,))
        result = cursor.fetchone()
        cursor.close()
        if result:
            return Classe(result[0], result[1])
        return None

    @staticmethod
    def read_all(connection):
        cursor = connection.cursor()
        query = "SELECT idClasse, Nome FROM Classe ORDER BY Nome"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        classes = []
        for result in results:
            classes.append(Classe(result[0], result[1]))
        return classes

    def update(self, connection):
        cursor = connection.cursor()
        query = "UPDATE Classe SET Nome = %s WHERE idClasse = %s"
        cursor.execute(query, (self.nome, self.id_classe))
        connection.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        return affected_rows > 0

    @staticmethod
    def delete(connection, id_classe):
        cursor = connection.cursor()
        query = "DELETE FROM Classe WHERE idClasse = %s"
        cursor.execute(query, (id_classe,))
        connection.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        return affected_rows > 0

