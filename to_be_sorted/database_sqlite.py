
import sqlite3

class DB_SQLITE(object):
	def __init__(self, database='users.db', table='users'):
		self.connection = sqlite3.connect(database)
		self.cursor = self.connection.cursor()
		self.table = table
		
		if self.table == 'users':
			sql_users_table = '''CREATE TABLE IF NOT EXISTS users (
									id text NOT NULL
									name text
									country text
									permition_level integer NOT NULL);'''
			self.create_table(sql_users_table)
		else:
			print("Please create your table!")
	
	def commit(self):
		self.connection.commit()
	
	def close_connection(self):
		self.connection.close()
		
	def create_table(self, sql_db_table):
		if not sql_db_table.startswith("CREATE TABLE"):
			print("Check your create table command...")
			return
		self.cursor.excecute(sql_db_table)
		print("Table created")
	
	def excecute_sql_command(self, sql_command):
		self.cursor.excecute(sql_command)
	
	def add_to_database(self, data, table=self.table):
		if not isinstance(data, tuple):
			data = tuple(data)
		self.cursor.excecute("INSERT INTO" + table +\
							 "stocks VALUES (?)", data)
		self.connection.commit()
	
	def get_user_info(self, user_id):
		


if __name__ == "__main__":
	database = DB_SQLITE()
	
