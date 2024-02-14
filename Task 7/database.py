import sqlite3
import json

from application_objects import *


class DataOperations:
    def __init__(self):
        self.DATABASE = "database.db"
        
        self.configure()

    def configure(self):
        """Creates all the tables neccessary for the application.
        """
        conn = sqlite3.connect(self.DATABASE)
        c = conn.cursor()

        c.execute("""
        create table IF NOT EXISTS User(
            username text,
            following User,
            liked list,
            disliked list
        )
        """)

        conn.commit()
        conn.close()

    def store_user(self, user: User):
        """saves the User object in database

        Args:
            user (User): User to be saved in database
        """
        conn = sqlite3.connect(self.DATABASE)
        c = conn.cursor()

        find_user = self.find_user(user.username)
        if find_user is None: # creates a new User
            c.execute('INSERT INTO User VALUES (:username, :following, :liked, :disliked)',{
                'username': user.username,
                'following': json.dumps(user.following),
                'liked': json.dumps(user.liked),
                'disliked': json.dumps(user.disliked)
            })
        else: # Update existing user
            c.execute("""UPDATE User SET
                username= :uname,
                following= :following,
                liked= :liked,
                disliked= :disliked
                WHERE oid= :oid""",{
                    'uname': user.username,
                    'following': json.dumps(user.following),
                    'liked': json.dumps(user.liked),
                    'disliked': json.dumps(user.disliked),
                    'oid': find_user.oid
                })

        conn.commit()
        conn.close()

    def get_all_users(self) -> list[User]:
        """fetch all the User objects from the database

        Returns:
            list[User]: list of User
        """
        conn = sqlite3.connect(self.DATABASE)
        c = conn.cursor()
        c.execute("SELECT *, oid FROM User")
        retrieved_users:list[tuple] = c.fetchall()
        users:list[User] = []
        for user in retrieved_users:
            users.append(User(*user))
        conn.close()
        return users

    def find_user(self, username: str) -> User | None:
        """Searches for the user with given username in the database. Returns None if not found

        Args:
            username (str): username of the user

        Returns:
            User | None: User object of given username
        """
        conn = sqlite3.connect(self.DATABASE)
        c = conn.cursor()

        all_users = self.get_all_users()
        target = None
        for user in all_users:
            if user.username == username:
                target = user

        
        conn.commit()
        conn.close()
        if target is None:
            # print("WARNING: User not found")
            return target
        else:
            return target


    def delete_user(self, username: str):
        """Deletes the user of given username

        Args:
            username (str): the username of the user to be deleted
        """
        conn = sqlite3.connect(self.DATABASE)
        c = conn.cursor()

        if self.find_user(username) is not None:
            c.execute('''DELETE FROM User WHERE username = ?''', (username,))
        else:
            print("WARNING: User not found")
        conn.commit()
        conn.close()


def main():
    dataOperations = DataOperations()

    user = User("test", ["test2", "test3"], ["liked post1"], ["disliked post1"])
    # dataOperations.delete_user("test")
    dataOperations.store_user(user)
    user = User("test", ["test2", "test3"], ["liked post1", "liked post2"], ["disliked post1"])
    dataOperations.store_user(user)
    dataOperations.find_user("test").print_details()
    dataOperations.get_all_users()
    dataOperations.delete_user("test")


if __name__ == "__main__":
    main()