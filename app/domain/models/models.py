from datetime import datetime
from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    fullname = Column(String, nullable=False)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)
    first_access = Column(Boolean, default=True)
    active = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime,  default=datetime.now())

    scopes = relationship("Scope", secondary="user_scope", back_populates="users")

    def __init__(self, fullname, username, password, is_admin):
        self.fullname = fullname
        self.username = username
        self.password = password
        self.is_admin = is_admin


class Scope(Base):
    __tablename__ = 'scopes'

    id = Column(Integer, primary_key=True)
    scope = Column(String, nullable=False)

    users = relationship("User",secondary="user_scope",back_populates="scopes")


class UserScope(Base):
    __tablename__ = 'user_scope'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    scope_id = Column(Integer, ForeignKey('scopes.id'), nullable=False)

    def __init__(self, user_id, scope_id):
        self.user_id = user_id
        self.scope_id = scope_id
