from aiogram import BaseMiddleware
from sqlalchemy.exc import IntegrityError
from db import SessionLocal, User

class UserMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        if hasattr(event, "from_user"):
            user_id = event.from_user.id
            db = SessionLocal()
            if not db.query(User).filter_by(user_id=user_id).first():
                try:
                    db.add(User(user_id=user_id))
                    db.commit()
                except IntegrityError:
                    db.rollback()
            db.close()
        return await handler(event, data)
