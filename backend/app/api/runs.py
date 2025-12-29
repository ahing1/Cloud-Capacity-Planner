from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.db.session import get_db
from app.db.models.run import Run
from app.schemas.run import RunCreate

router = APIRouter(prefix="/runs", tags=["runs"])

@router.post("")
async def create_run(payload: RunCreate, db: AsyncSession = Depends(get_db)):
    run = Run(
        scenario_name=payload.scenario_name,
        planner_name=payload.planner_name,
        seed=payload.seed,
        config=payload.config,
        status="pending",
    )
    db.add(run)
    await db.commit()
    await db.refresh(run)
    return {"run_id": run.id, "status": run.status}

@router.get("")
async def list_runs(db: AsyncSession = Depends(get_db)):
    res = await db.execute(select(Run).order_by(Run.started_at.desc()))
    return res.scalars().all()
