import sqlite3

conn = sqlite3.connect('helper.db')

c=conn.cursor()
c.execute(""" CREATE table hp_code (
                hp_cd_id integer,
                hp_cd_desc text,
                hp_cd_script text)    
    """)
conn.commit()

c.execute(""" CREATE table hp_code_tag (
                hp_cd_id integer,
                tag text)    
    """)
conn.commit()





class ap_db():
    def __init__(self):
        self.dbfile='helper.db'
    def ap_conn(self):
        conn = sqlite3.connect(self.dbfile)
        self.cur=conn.cursor()
    def get_hp_cd(self):
        pass 
    def add_hp_cd(self):
        pass

