import psycopg2

connection = psycopg2.connect("dbname=example user=qingyuan password=MAzhang199711#")

# cursor is the interface: queing up and making transactions
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE table2 (
        id INTEGER PRIMARY KEY,
        complete BOOLEAN NOT NULL DEFAULT FALSE
    );
''')

cursor.execute('INSERT INTO table2 (id, complete) VALUES (1, true);')

# cursor.execute will not execute the commands in sql immediately, it need to commit first,
# so here we commit both as a whole unit
connection.commit()

# if we decide not do other works in this session:
connection.close()
cursor.close()