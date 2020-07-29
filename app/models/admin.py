import sqlalchemy as sa

from app.db import Base


ADMIN_USER_ACTIVE = 1
ADMIN_USER_INACTIVE = 0


class AdminUser(Base):
    """User who will manage web dashboard"""
    __tablename__ = 'admin_users'

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    username = sa.Column(sa.String, unique=True)
    password = sa.Column(sa.String)
    status = sa.Column(sa.SmallInteger, default=ADMIN_USER_ACTIVE)
