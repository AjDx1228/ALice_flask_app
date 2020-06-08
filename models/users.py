from data import db_session
from data import users


def add_user(ip):
    session = db_session.create_session()
    user_db = users.User()
    user_ip = ip
    
    session.add(user_db)
    session.commit()