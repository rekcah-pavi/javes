from sqlalchemy import BigInteger, Boolean, Column, LargeBinary, Numeric, String, UnicodeText
from userbot.modules.sql_helper import SESSION, BASE


class rkwelcome(BASE):
    __tablename__ = "rkwelcome"
    chat_id = Column(Numeric, primary_key=True)
    should_clean_rkwelcome = Column(Boolean, default=False)
    previous_rkwelcome = Column(BigInteger)
    f_mesg_id = Column(Numeric)

    def __init__(
        self,
        chat_id,
        should_clean_rkwelcome,
        previous_rkwelcome,
        f_mesg_id
    ):
        self.chat_id = chat_id
        self.should_clean_rkwelcome = should_clean_rkwelcome
        self.previous_rkwelcome = previous_rkwelcome
        self.f_mesg_id = f_mesg_id


rkwelcome.__table__.create(checkfirst=True)


def get_current_rkwelcome_settings(chat_id):
    try:
        return SESSION.query(rkwelcome).filter(rkwelcome.chat_id == chat_id).one()
    except:
        return None
    finally:
        SESSION.close()


def add_rkwelcome_setting(
    chat_id,
    should_clean_rkwelcome,
    previous_rkwelcome,
    f_mesg_id
):
    adder = SESSION.query(rkwelcome).get(chat_id)
    if adder:
        adder.should_clean_rkwelcome = should_clean_rkwelcome
        adder.previous_rkwelcome = previous_rkwelcome
        adder.f_mesg_id = f_mesg_id
    else:
        adder = rkwelcome(
            chat_id,
            should_clean_rkwelcome,
            previous_rkwelcome,
            f_mesg_id
        )
    SESSION.add(adder)
    SESSION.commit()


def rm_rkwelcome_setting(chat_id):
    rem = SESSION.query(rkwelcome).get(chat_id)
    if rem:
        SESSION.delete(rem)
        SESSION.commit()


def update_previous_rkwelcome(chat_id, previous_rkwelcome):
    row = SESSION.query(rkwelcome).get(chat_id)
    row.previous_rkwelcome = previous_rkwelcome
    # commit the changes to the DB
    SESSION.commit()
