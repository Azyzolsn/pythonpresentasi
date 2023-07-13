from model import Book
from config import database
import uuid 

class BookRepo():
    
    @staticmethod
    async def retrieve():
        _book = []
        collection = database.get_collection('book').find()
        async for book in collection:
            _book.append(book)
        return _book
    
    @staticmethod
    async def insert(book: Book):
        id = str(uuid.uuid4())
        _book = {
            "_id":id,
            "title": book.title,
            "description": book.description
        }
        await database.get_collection('book').insert_one(_book)
        
    @staticmethod
    async def update(id: str, book: Book):
        _book = await database.get_collection('book').find_one({"_id": id})
        if _book is not None:
            _book["title"] = book.title
            _book["description"] = book.description
            await database.get_collection('book').update_one({"_id": id}, {"$set": _book})
        else:
            # Handle case when no document is found
            # (e.g., raise an exception or return an appropriate response)
            raise Exception("No document found with the given id")



        
    @staticmethod
    async def retrieve_id(id:str):
        return await database.get_collection('book').find_one({"_id":id})
    
    @staticmethod
    async def delete(id: str):
        await database.get_collection('book').delete_one({"_id": id})
