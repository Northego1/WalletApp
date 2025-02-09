from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from api.v1 import routes


@asynccontextmanager
async def lifespan(_: FastAPI):
    # container.init_resources()
    # container.wire(modules=['api.v1.routes'])
    yield

app = FastAPI(lifespan=lifespan)




app.include_router(routes.router)
    

if __name__ == '__main__':


    uvicorn.run('main:app', reload=True)