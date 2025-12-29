from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base
from sqlalchemy.dialects.postgresql import JSONB


class Event(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True)
    run_id: Mapped[str] = mapped_column(index=True)
    t: Mapped[int]

    type: Mapped[str]
    payload: Mapped[dict] = mapped_column(JSONB)
