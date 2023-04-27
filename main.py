from fastapi import FastAPI
from вbreq import *

app = FastAPI()

con = createConnetion()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/list")
async def list():
    resp = listAll(con)
    return resp


@app.post("/refreshTable")
async def refresh():
    refreshTable(con)
    return {'status': 'ok'}


@app.post("/moveProdPar/{productA}")
async def moveParam(productA,productB):
    moveProductsParam(con, [productA], productB)
    return {'status': 'ok'}


@app.delete("/deleteByParam/{param}")
async def deleteBParam(param):
    deleteByParam(con,[param])
    return {'status': 'ok'}


@app.get("/productFromParams/{param}")
async def getProdByParam(param):
    return productsFromParams(con, [param])


@app.get("/productNotFromParams/{param}")
async def getProdByNotParam(param):
    return productsNotInParams(con, [param])


@app.get("/paramFromProduct/{product}")
async def getParamByProd(product):
    return paramFromProducts(con,[product])