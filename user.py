from database import CursorFromConnectionFromPool

class User:
    def __init__(self, email, first_name, last_name, id):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def __repr__(self):
        return "User: {} {}".format(self.first_name, self.last_name)

    def save_to_db(self):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('INSERT INTO users (email, first_name, last_name) VALUES (%s, %s, %s)',
                           (self.email, self.first_name, self.last_name))
            print("Saved! Thank you for your input.")

    @classmethod
    def load_db_by_email(cls, email):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('SELECT * FROM users WHERE email=%s', (email,))
            member_data = cursor.fetchone()
            return cls(member_data[1], member_data[2], member_data[3], member_data[0])

    @classmethod
    def print_from_db(cls):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('SELECT * FROM users')
            list_user = cursor.fetchall()
            for user in list_user:
                print(user)

    @classmethod
    def delete_row(cls):
        with CursorFromConnectionFromPool() as cursor:
            where = input('WHERE syntax:')
            return cursor.execute('DELETE FROM users WHERE {}'.format(where))