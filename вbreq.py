import sqlite3


def createConnetion():
    return sqlite3.connect("LapaDb.db")


def initCursor(connection):
    return connection.cursor()


def createTable(connection):
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS products(
    productid INT PRIMARY KEY,
    product TEXT NOT NULL,
    productParam TEXT)""")
    connection.commit()


def dropTable(connection):
    cursor = initCursor(connection)
    cursor.execute("""DROP TABLE products""")
    connection.commit()


def addProduct(connection, product):
    cursor = initCursor(connection)
    cursor.executemany("""INSERT INTO products VALUES (?,?,?);""",product)
    connection.commit()


def listAll(connection):
    cursor = initCursor(connection)
    cursor.execute("""SELECT * from products""")
    all = cursor.fetchall()
    print(all)
    connection.commit()

    return {'bd': all}


def paramFromProducts(connection, products):
    cursor = initCursor(connection)
    cursor.execute('''SELECT productParam from products where product = ?;''', products)
    param = cursor.fetchall()
    print(param)
    connection.commit()
    return {'param': param}


def productsNotInParams(connection, notParams):
    cursor = initCursor(connection)
    cursor.execute('''SELECT product FROM products WHERE productParam NOT IN (?);''', notParams)
    prod = cursor.fetchall()
    print(prod)
    connection.commit()
    return {'products': prod}


def productsFromParams(connection, params):
    cursor = initCursor(connection)
    cursor.execute('''SELECT product from products where productParam = ?;''', params)
    prod = cursor.fetchall()
    print(prod)
    connection.commit()
    return {'products': prod}


def deleteByParam(connection,params):
    cursor = initCursor(connection)
    cursor.execute('''DELETE FROM products WHERE productParam = ?;''', params)
    connection.commit()


def moveProductsParam(connection, productA, productB):
    cursor = initCursor(connection)
    cursor.execute("""SELECT productParam FROM products WHERE product =?;""", productA)
    paramA = cursor.fetchone()
    args = [(paramA[0]), productB]
    print(args)
    cursor.execute("""UPDATE products SET productParam = null where product =?;""", productA)
    cursor.execute("""UPDATE products SET productParam =? where product =?;""",args)
    connection.commit()

def refreshTable(connection):
    dropTable(connection)
    createTable(connection)
    prod = [('01', 'Samsung-A51', 'lag'), ('02', 'Pixel-A6', 'tensor'), ('03', 'Realme-GT', 'realme')]
    addProduct(connection, prod)

con = createConnetion()
#createTable(con)
listAll(con)
moveProductsParam(con, ['Pixel-A6'], 'Realme-GT')
listAll(con)
refreshTable(con)
listAll(con)


