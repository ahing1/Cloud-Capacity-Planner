from sqlalchemy import String, DateTime, JSON
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
import uuid
from app.db.base import Base

class Run(Base):
    __tablename__ = "runs"

    id: Mapped[str] = mapped_column(
        String, primary_key=True, default=lambda: str(uuid.uuid4())
    )

    scenario_name: Mapped[str] = mapped_column(String, index=True)
    planner_name: Mapped[str] = mapped_column(String, index=True)
    status: Mapped[str] = mapped_column(String, index=True)

    seed: Mapped[int]
    config: Mapped[dict] = mapped_column(JSON)

    started_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    finished_at: Mapped[datetime | None]
