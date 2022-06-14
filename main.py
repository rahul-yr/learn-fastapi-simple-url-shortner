from fastapi import FastAPI
from url_shortner import router

# Create the app
app = FastAPI()

# Add the router
app.include_router(router.url_shortner, prefix="/url-shortner")
