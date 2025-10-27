def update_user(rowid, name=None, age=None, hobby=None):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    fields = []
    values = []

    if name is not None:
        fields.append("name = ?")
        values.append(name)
    if age is not None:
        fields.append("age = ?")
        values.append(age)
    if hobby is not None:
        fields.append("hobby = ?")
        values.append(hobby)

    if not fields:
        print("❗ Нет данных для обновления.")
        conn.close()
        return

    sql = f"UPDATE users SET {', '.join(fields)} WHERE rowid = ?"
    values.append(rowid)

    cursor.execute(sql, values)
    conn.commit()
    conn.close()

    print(f"✅ Пользователь с rowid={rowid} обновлён.")





    import sqlite3

    def read_user_by_id(rowid):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        cursor.execute("SELECT rowid, name, age, hobby FROM users WHERE rowid = ?", (rowid,))
        user = cursor.fetchone()

        conn.close()

        if user:
            print(f"ID: {user[0]} | NAME: {user[1]} | AGE: {user[2]} | HOBBY: {user[3]}")
        else:
            print(f"❌ Пользователь с ID {rowid} не найден.")