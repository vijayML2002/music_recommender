import mysql.connector
import rankaggregation as ra
import time
import math

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="vijay1234",
    database="testdb"
    )

def normalize(x):
    amin, amax = min(x), max(x)
    for i, val in enumerate(x):
        x[i] = (val-amin) / (amax-amin)
        x[i] = round(x[i],3)
    return x
    
def prepare_data():
    music_index = []
    count = []
    time = []

    try:
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM MUSIC")
        records = cursor.fetchall()

        for row in records:
            music_index.append(row[0])
            count.append(row[2])
            time.append(row[4])

    except:
        print("Error")
        pass

    music_index = [int(l) for l in music_index]
    count = normalize([int(l) for l in count])
    time = normalize([int(l) for l in time])

    return music_index,count,time


def calculate_dfo(x,y):
    assert len(x) == len(y)

    dfo = []
    theta = []

    for a,b in zip(x,y):
        
        val = math.pow(a,2) + math.pow(b,2)
        val = math.sqrt(val)
        val = round(val,3)

        th = math.atan2(a,b)
        th = round(th,3)

        dfo.append(val)
        theta.append(th)

    return dfo,theta

def rankdata(arr,index):

    new_index = [i for i in index]
    
    assert len(arr)==len(new_index)
    ranked_list = []
    while True:
        if len(arr) == 0:
            break

        curr_min = max(arr)

        for i,element in enumerate(arr):
            if element == curr_min:
                ranked_list.append(new_index[i])
                del(new_index[i])
                del(arr[i])
                break

    return ranked_list
    

        
def cummulative_rank():
    index,count,time = prepare_data()
    r,theta = calculate_dfo(count,time)

    r_ranked = rankdata(r,index)
    theta_ranked = rankdata(theta,index)

    str_r = [str(i) for i in r_ranked]
    str_theta = [str(i) for i in theta_ranked]

    agg = ra.RankAggregator()
    cum_rank = agg.borda([str_r,str_theta])
    
    return cum_rank

def update_hp():
    cumm_r = cummulative_rank()

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM MUSIC")
    records = cursor.fetchall()
    
    for element in cumm_r:
        for row in records:
            if row[0] == int(element[0]):
                break

        query = """ UPDATE MUSIC
                SET hp_num = %s
                WHERE id = %s """
        data = (str(element[1]),row[0])

        cursor.execute(query,data)
        mydb.commit()

    print("Update of hot_number is completed")
        




        
        



















    


