try:
    from userbot.modules.sql_helper import SESSION, BASE
except ImportError:
    raise AttributeError

from sqlalchemy import Column, String, UnicodeText


class globelmute(BASE):
    __tablename__ = "globelmute"
    sender = Column(String(14), primary_key=True)

    def __init__(self, sender):
        self.sender = str(sender)


globelmute.__table__.create(checkfirst=True)


def is_globelmuted(sender_id):
    try:
        return SESSION.query(globelmute).all()
    except BaseException:
        return None
    finally:
        SESSION.close()


def globelmute(sender):
    adder = globelmute(str(sender))
    SESSION.add(adder)
    SESSION.commit()


def unglobelmute(sender):
    rem = SESSION.query(globelmute).get((str(sender)))
    if rem:
        SESSION.delete(rem)
        SESSION.commit()
