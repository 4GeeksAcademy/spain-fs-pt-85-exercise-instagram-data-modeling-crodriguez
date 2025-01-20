import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base, mapped_column
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    
    id = mapped_column(Integer, primary_key=True)
    username = mapped_column(String(50), nullable=False)
    firstname = mapped_column(String(50))
    lastname = mapped_column(String(100))
    email = mapped_column(String(100), nullable=False)
    follower = relationship("User", back_populates="follower")

class Post(Base):
    __tablename__ = 'post'

    id = mapped_column(Integer, primary_key=True)
    user_id = mapped_column(ForeignKey('user.id'))
    user = relationship("Post", back_populates="user")

class Media(Base):
    __tablename__ = 'media'

    id = mapped_column(Integer, primary_key=True)
    type = mapped_column(String(250))
    url = mapped_column(String(250))
    post_id = mapped_column(ForeignKey('post.id'))
    post = relationship("Media", back_populates="post")

class Comment(Base):
    __tablename__ = 'comment'

    id = mapped_column(Integer, primary_key=True)
    comment_text = mapped_column(String(250))
    author_id = mapped_column(ForeignKey('user.id'))
    post_id = mapped_column(ForeignKey('post.id'))
    user = relationship("Comment", back_populates="user")
    post = relationship("Comment", back_populates="post")
    

class Follower(Base):
    __tablename__ = 'follower'
    
    id = mapped_column(Integer, primary_key=True)
    user_from_id = mapped_column(ForeignKey('user.id'))
    user_to_id = mapped_column(ForeignKey('user.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
