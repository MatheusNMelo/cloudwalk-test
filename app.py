from datetime import datetime
from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from cloudwalk_test import antifraud_engine


app = FastAPI(title="Cloudwalk Anti-Fraud API", version="1.0.0")


class TransactionPayload(BaseModel):
    transaction_id: int
    merchant_id: int
    user_id: int
    card_number: str
    transaction_date: datetime
    transaction_amount: float
    device_id: Optional[int] = None


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/evaluate")
def evaluate_transaction(payload: TransactionPayload) -> dict:
    try:
        result = antifraud_engine.evaluate(payload.model_dump(mode="json"))
        return result
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Evaluation failed: {exc}")
