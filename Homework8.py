import sqlite3
def create_user_summary_view():
    conn = sqlite3.connect('user_grades.db')
    cursor = conn.cursor()

    cursor.execute("""
    CREATE VIEW IF NOT EXISTS user_summary AS
    SELECT 
        u.id AS user_id,
        u.name AS name,
        u.age AS age,
        u.hobby AS hobby,
        g.subject AS subject,
        g.grade AS grade
    FROM users u
    LEFT JOIN grades g ON u.id = g.user_id
    """)

    conn.commit()
    conn.close()
    print("✅ Представление 'user_summary' успешно создано.")






    import sqlite3

    def create_user_summary_view():
        conn = sqlite3.connect('user_grades.db')
        cursor = conn.cursor()

        cursor.execute("""
        CREATE VIEW IF NOT EXISTS user_summary AS
        SELECT 
            u.id AS user_id,
            u.name AS name,
            u.age AS age,
            u.hobby AS hobby,
            ROUND(AVG(g.grade), 2) AS avg_grade
        FROM users u
        LEFT JOIN grades g ON u.id = g.user_id
        GROUP BY u.id
        """)

        conn.commit()
        conn.close()
        print("✅ Представление 'user_summary' (средняя оценка) успешно создано.")

