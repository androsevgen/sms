import conn_db

try:
    cur = conn_db.con.cursor()
    cur.execute("""select id, contact_id, phone_num, encoding, lang, offer_id, src_id, xml_text from sbl_list""")
    for res in cur:
        print(res)
except:
    conn_db.con.close()

