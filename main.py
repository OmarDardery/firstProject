from fastapi import FastAPI
import os
from dotenv import load_dotenv
from supabase import create_client, Client
load_dotenv()

url: str = os.environ["SUPABASE_URL"]
key: str = os.environ["SUPABASE_KEY"]
supabase: Client = create_client(url, key)
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/add-person/{name}/{age}")
def add_person(name: str, age: int):
    data = supabase.table("main").insert({"name": name, "age": age}).execute()
    print(data)
    return {"message": "Person added successfully", "data": data}

@app.get("/get-people")
def say_hello():
    data = supabase.table("main").select("*").execute()
    print(data)
    return data