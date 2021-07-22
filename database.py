import mysql.connector
import time

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="vijay1234",
    database="testdb"
    )

def delete_table(x):
    cursor = mydb.cursor()
    sql = "DROP TABLE {}".format(x)
    cursor.execute(sql)

def create_table(x):
    cursor = mydb.cursor()
    sql = """CREATE TABLE {} (id INT AUTO_INCREMENT PRIMARY KEY,
             path VARCHAR(255), no_clicks VARCHAR(255), mood VARCHAR(255),
             last_seen VARCHAR(255) , l_l VARCHAR(255), hp_num VARCHAR(255))""".format(x)
    cursor.execute(sql)
    
def insert_music(music_path):
    cursor = mydb.cursor()

    add_music = ("INSERT INTO MUSIC "
                 "(path,no_clicks,mood,last_seen,l_l,hp_num)"
                 "VALUES (%(mus_pth)s, %(no)s, %(md)s, %(ld)s, %(ll)s, %(hp)s)")

    music_details = {
        'mus_pth': music_path,
        'no': 0,
        'md': 0.5,
        'ld': round(time.time()),
        'll': 0,
        'hp': 0,
        }


    cursor.execute(add_music,music_details)
    mydb.commit()

def delete_all():
    cursor = mydb.cursor()
    cursor.execute("TRUNCATE TABLE MUSIC")

def song_bucket():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM MUSIC")
    records = cursor.fetchall()
    return records

def update_clicks(song):
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM MUSIC")
    records = cursor.fetchall()

    for row in records:
        if row[1]==song:
            index = row[0]
            freq = row[2]
            break

    query = """ UPDATE MUSIC
                SET no_clicks = %s
                WHERE id = %s """
    freq = int(freq) + 1
    data = (str(freq),index)


    query2 = """ UPDATE MUSIC
                SET last_seen = %s
                WHERE id = %s """
    data2 = (str(round(time.time())),index)
    
    try:
        cursor.execute(query,data)
        mydb.commit()
        cursor.execute(query2,data2)
        mydb.commit()
        
    except:
        print("Error while updating data")
        pass

def mark_song(song):
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM MUSIC")
    records = cursor.fetchall()

    for row in records:
        if row[1]==song:
            index = row[0]
            freq = row[2]
            break

    query = """ UPDATE MUSIC
                SET l_l = %s
                WHERE id = %s """
    data = (str(1),index)

    cursor.execute(query,data)
    mydb.commit()


    
def clear_mark():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM MUSIC")
    records = cursor.fetchall()

    try:
        for row in records:
            if row[5]=='1':
                index = row[0]
                freq = row[2]
                break

        query = """ UPDATE MUSIC
                    SET l_l = %s
                    WHERE id = %s """

        data = (str(0),index)

        cursor.execute(query,data)
        mydb.commit()
    
    except:
        pass
