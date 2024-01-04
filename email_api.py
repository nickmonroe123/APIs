from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/my-first-api")
def hello(name = None):

    if name is None:
        text = 'Hello!'

    else:
        text = 'Hello ' + name + '!'

    return text


if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')