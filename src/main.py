from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from api.v1 import routes
from container import container


@asynccontextmanager
async def lifespan(_: FastAPI):
    db = container.db()
    await db.get_ready_connection_pool()
    yield


app = FastAPI(lifespan=lifespan)


app.include_router(routes.router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
