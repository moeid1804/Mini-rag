import os
from fastapi import FastAPI
from routes import base, data
from dotenv import load_dotenv
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.staticfiles import StaticFiles

load_dotenv(".env")
# app = FastAPI()
app = FastAPI(docs_url=None, redoc_url=None)

# 2. Add offline environment flags
os.environ["TRANSFORMERS_OFFLINE"] = "1"
os.environ["HF_DATASETS_OFFLINE"] = "1"
# 3. Mount the static folder (Make sure you have a folder named 'static' with the .js and .css files)
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(base.router)
app.include_router(data.data_router)


# 5. Add the custom offline Swagger route
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
    )


# 6. Run using Uvicorn
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
