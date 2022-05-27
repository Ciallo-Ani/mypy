import sqlite3


def haveMap(inp: tuple, comp: list, mapidx: int):
    for x in comp:
        if inp[mapidx] == x[mapidx]:
            return True
    return False


def tiersConvert(bhopcursor: sqlite3.Cursor, mycursor: sqlite3.Cursor):
    bhopcursor.execute("SELECT * FROM maptiers;")
    bhopresult = bhopcursor.fetchall()

    mycursor.execute("SELECT * FROM maptiers;")
    myresult = mycursor.fetchall()

    for x in bhopresult:
        if haveMap(x, myresult, 0):
            continue

        try:
            mycursor.execute("INSERT INTO maptiers VALUES (?, ?)", x)
        except sqlite3.IntegrityError as e:
            print("value {} have conflict".format(x))


def zonesConvert(bhopcursor: sqlite3.Cursor, mycursor: sqlite3.Cursor):
    bhopcursor.execute("SELECT * FROM mapzones;")
    mycursor.execute("SELECT * FROM mapzones;")

    bhopresult = bhopcursor.fetchall()
    myresult = mycursor.fetchall()

    for x in bhopresult:
        if haveMap(x, myresult, 1):
            continue

        try:
            mycursor.execute("INSERT INTO mapzones VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", x)
        except sqlite3.IntegrityError as e:
            print("value {} have conflict".format(x))


def main():
    mydb = sqlite3.connect(r"C:\Users\Administrator\Desktop\shavit.sq3")
    mycursor = mydb.cursor()

    bhopdb = sqlite3.connect(r"C:\Users\Administrator\Desktop\mytiers.db")
    bhopcursor = bhopdb.cursor()
    tiersConvert(bhopcursor, mycursor)

    bhopdb = sqlite3.connect(r"C:\Users\Administrator\Desktop\myzones.db")
    bhopcursor = bhopdb.cursor()
    zonesConvert(bhopcursor, mycursor)

    mydb.commit()
    mydb.close()


if __name__ == '__main__':
    main()
