from typing import Union, Annotated

from fastapi import FastAPI, Query, Path

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/items/")
async def read_items(q: Annotated[str, Query(min_length=3, max_length=50)], skip:int = 50, limit:int = 10):
    return {"q": q, "skip": skip, "limit": limit}

# def main():
#     print("Hello from fastapi-azure!")


# if __name__ == "__main__":
#     main()
