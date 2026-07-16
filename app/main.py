from fastapi import FastAPI
from app.routes.transactions import router as transaction_router
from app.config import settings
from app.routes.events import router as event_router
from app.routes.reconciliation import router as reconciliation_router

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
)

app.include_router(event_router)
app.include_router(transaction_router)
app.include_router(reconciliation_router)


@app.get("/")
def root():
    return {
        "message": "Payment Reconciliation Service is running."
    }