import mysql.connector


class DBConnector:
    def __init__(self):
        self.__db: mysql.connector = None
        self.__DBConnect()
        self.__cursor = self.__db.cursor()

    def __DBConnect(self):
        self.__db = mysql.connector.connect(host="localhost",
                                            user="root",
                                            password="root",
                                            database="helloworldmvc")

    def __DBClose(self):
        self.__db.close()

    def getCursor(self):
        return self.__cursor

    @staticmethod
    def _cursorResultsToJSon(cursorResults):
        columns = [column[0] for column in cursorResults.description]
        results = []
        for row in cursorResults.fetchall():
            results.append(dict(zip(columns, row)))
        return results

    def getHelloWorldByNum(self, num):
        self.__cursor.callproc("helloWorldByNum", [num])
        results = self._cursorResultsToJSon(next(self.__cursor.stored_results()))
        if len(results) == 0:
            return ""
        return results[0]["message"]
