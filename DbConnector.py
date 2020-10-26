import pypyodbc
class DbConnector():

    def verifyCategory(self, CategoryName):
        try:
            connection = pypyodbc.connect('Driver={SQL Server};'
                                          'Server=CPSTQA;'
                                          'Database=CPST;'
                                          'Trusted_Connection=yes;')
            cursor = connection.cursor()
            print(CategoryName)
            sql_department_query = "select * from [CPST].[dbo].[ClinicalInterventionCategory] where [Name]='" + CategoryName + "'"
            cursor.execute(sql_department_query)
            print("Query executed successfully")
            for row in cursor:
                print(row)
            print(cursor.rowcount)

        except Exception as e:
            print("Exception Occured :", e)
        return cursor.rowcount
