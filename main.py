import asyncio

from fastapi import FastAPI

import uvicorn


if __name__ == "__main__":
    asgi_app = FastAPI()
    uvicorn.run(asgi_app, host="0.0.0.0", port=8000)
