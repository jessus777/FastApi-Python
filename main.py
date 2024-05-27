from fastapi import FastAPI

app = FastAPI()
app.title = 'Mi primer aplicacion'

@app.get("/", tags=['Home'])
def  home():
    return "Hi, I am FastAPI"