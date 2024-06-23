from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:postgres@db/todo_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


app = FastAPI()

class TodoItem(Base):
    __tablename__ = 'todo'
    id = Column(Integer, primary_key = True, index = True)
    statement = Column(String, index = True)

Base.metadata.create_all(bind=engine)

class TodoCreate(BaseModel):
    statement: str

@app.post('/create_todo')
async def create_todo(todo: TodoCreate):
    db = SessionLocal()
    db_todo = TodoItem(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    db.close()
    return db_todo


@app.get('/get_todo')
async def get_todos(skip: int = 0):
    db = SessionLocal()
    todo_list = db.query(TodoItem).offset(skip).all()
    db.close()
    return todo_list

@app.delete('/delete_todo')
async def delete_todo(todo_id: int):
    db = SessionLocal()
    todo = db.query(TodoItem).filter(TodoItem.id == todo_id).first()
    db.delete(todo)
    db.commit()
    db.close()
    

        


        


