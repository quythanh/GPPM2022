from datetime import date
import sqlite3

path = "mysite/data/users.sqlite"

def toList(cursor):
    listData = []
    for value in cursor:
        newData = {}
        newData["id"] = value[0]
        newData["name"] = value[1]
        newData["gender"] = "Nam" if value[2] else "Nữ"
        newData["birthday"] = value[3]
        newData['height'] = value[4]
        newData['weight'] = value[5]
        
        if (value[6] == 0):
            newData['blood'] = 'A'
        elif (value[6] == 1):
            newData['blood'] = 'B'
        elif (value[6] == 2):
            newData['blood'] = 'AB'
        else:
            newData['blood'] = 'O'

        newData["bmi"] = round(value[5]/(value[4]/100)**2, 1)
        newData['age'] = date.today().year - int(value[3].split('/')[-1])
        
        listData.append(newData)

    return listData

def execute(SQL, params=()):
    connect = sqlite3.connect(path)
    cursor = connect.cursor()
    cursor.execute(SQL, params)
    connect.commit()
    connect.close()
    return cursor.rowcount

def getUser(id):
    connect = sqlite3.connect(path)
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM INFO WHERE ID = ?", (id))
    data = toList(cursor)
    connect.commit()
    connect.close()
    return data[0]

def writeHealth(data, id):
    sql = ("INSERT INTO HEALTH(Mach, NhietDo, NhipTho, SpO2, HuyetApMax, "
        "HuyetApMin, Symptoms) values(?, ?, ?, ?, ?, ?, ?) WHERE ID = ?")