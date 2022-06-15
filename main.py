from fastapi import FastAPI
from url_shortener import router

# Create the app
app = FastAPI()

# Add the router
app.include_router(router.url_shortener, prefix="/url-shortener")
