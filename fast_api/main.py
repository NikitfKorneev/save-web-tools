from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel


app = FastAPI()


books = [
    {
        "id": 1, 
        "name": "Book_1", 
        "Text": "A",
        },
    {
        "id": 2, 
        "name": "Book_2", 
        "Text": "B",
        },
    {
        "id": 3, 
        "name": "Book_3", 
        "Text": "C",
        },
]


@app.get(
        "/",
        tags=["Главная страница"],
        summary="Главная страница")
async def root():
    return {"massage": "Hello World"}

@app.get(
        "/items",
        tags=["Предметы"],
        summary="Получить все предметы")
async def items() -> list:
    return books

@app.get(
        "/items/{id}",
        tags=["Предметы"],
        summary="Получить конкретный предмет")
async def items(id: int) -> dict:
    for book in books:
        if book["id"] == id:
            return book
        
    raise HTTPException(status_code=404, detail="Book not found")


class NewItem(BaseModel):
    name: str
    text: str

    
@app.post("/new_items", tags=["Создание предметов"], summary="Создать один объект")
async def create_iteam(new_item:NewItem):
    books.append({
        "id": len(books)+1,
        "name": new_item.name,
        "text": new_item.text,
    })
    return{"success": True, "message": "Элемент успешно дбавлен"}


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)