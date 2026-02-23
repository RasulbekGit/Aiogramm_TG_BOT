from aiogram import Router

from .admin import router as admin_router
from .commands import router as common_router
from .media import router as media_router

router = Router()

router.include_routers(
    admin_router,
    media_router,
    common_router,
)
