from pony.orm import *

db = Database()
db.bind(provider='mysql', host='db', user='root', passwd='Scooby25', db='se')
set_sql_debug(True)