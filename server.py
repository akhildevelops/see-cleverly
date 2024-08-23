from fastapi import FastAPI
from see_cleverly import api_router

app = FastAPI()
app.include_router(api_router)


@app.get("/")
async def root():
    return {"message": "Seecleverly Journey Begins"}


# def main():


# if __name__ == "__main__":
#     main()
