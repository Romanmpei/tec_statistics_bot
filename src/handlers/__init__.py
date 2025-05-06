from .fallback import router as fallback_router
from .common import router as common_router
from .menu import router as menu_router
from .stats import router as stats_router

routers = (
    common_router,
    menu_router,
    stats_router,
    fallback_router
)
