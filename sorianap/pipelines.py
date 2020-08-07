# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import time
import datetime
ts = time.time()
timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
import mysql.connector

class SorianapPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host='mx94.hostgator.mx',
            user='digit163_tony',
            password='yaquedaporfA123.',
            db='digit163_remoto'
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS pruebasph_tb""")
        self.curr.execute("""create table pruebasph_tb(
                        percent int,
                        title text,
                        pricel float,
                        priceh float,
                        direccion text,
                        fecha timestamp
                        )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""insert into pruebasori_tb values (%s,%s,%s,%s,%s,%s)""", (
                        int(item['percent']),
                        str(item['title']),
                        float(item['pricel']),
                        float(item['priceh']),
                        str(item['direccion']),
                        timestamp
        ))
        self.conn.commit()
