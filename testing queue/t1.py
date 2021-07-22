import mysql.connector

from queue_dll import Queue,Node
from queue_dll import push,pop,is_empty
from queue_dll import display_top,display_back

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="vijay1234",
    database="testdb"
    )

def fill_queue():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM MUSIC")
    records = cursor.fetchall()

    arr = []
    q = Queue()

    for row in records:
        arr.append([row[1],int(row[6])])

    arr = sorted(arr, key=lambda x: x[1])[::-1]

    for i in range(len(arr)):
        push(q,Node(arr[i][0],arr[i][1]))

    return q
