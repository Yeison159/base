from clases.DataBase import Database


class usuario(Database):
    def __init__(self):
        #pass se pone cuando no hay nada en el inicializador
        pass

    def consultarSuamrio(self):

        data = self.list_employees()
        return data

    def getuser(self, id):
        data = self.lisByUser(id)
        return data

    def get_doce(self):
        data = self.lisBycount()
        return data
