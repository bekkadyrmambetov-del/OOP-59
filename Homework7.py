import sqlite3

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