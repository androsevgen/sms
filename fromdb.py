import conn_db

try:
    cur = conn_db.con.cursor()
    cur.execute("""select * from sbl_wave WHERE wave_id IN 'Z-7VA'""")
    for res in cur:
        print(res)
except:
    conn_db.con.close()

