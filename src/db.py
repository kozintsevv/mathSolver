import sqlite3


class BotDB:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def user_exists(self, user_id):
        """Проверяем, есть ли юзер в базе"""
        result = self.cursor.execute(
            "SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id,)
        )
        return bool(len(result.fetchall()))

    def add_user(self, user_id, user_name):
        """Добавляем юзера в базу"""
        self.cursor.execute(
            "INSERT INTO `users` (`user_id`,`user_name`) VALUES (?,?)",
            (user_id, user_name),
        )
        return self.conn.commit()

    def increment_action(self, user_id):
        result = self.cursor.execute(
            "SELECT `actions` FROM `users` WHERE `user_id`=?", (user_id,)
        )
        action = result.fetchone()[0] + 1
        self.cursor.execute(
            "UPDATE `users` SET actions = ? WHERE user_id = ?", (action, user_id)
        )
        return self.conn.commit()

    def get_statistic(self):
        result = self.cursor.execute("SELECT * FROM `users`")
        return result

    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()
