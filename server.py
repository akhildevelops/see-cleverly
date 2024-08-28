from fastapi import FastAPI, Depends
from see_cleverly import api_router
from see_cleverly.dependencies import CommonP


app = FastAPI()
app.include_router(api_router)


@app.get("/")
async def root():
    return {"message": "Seecleverly Journey Begins"}


# def main():


# if __name__ == "__main__":
#     main()
