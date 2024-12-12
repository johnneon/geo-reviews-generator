from fastapi import APIRouter

router = APIRouter(prefix="")


@router.get("/")
async def root():
    """Empty method, just for test is app running"""

    return {"message": "Hi! For test, you should send POST request "
                       "to the `/predict` endpoint,with following parameters:",
            "body": {
                "rubrics": "Кафе",
                "name_org": "Плакучая ива",
                "org_address": "г. Сочи, ул. Войкова, 3",
                "rating": 1
            }}