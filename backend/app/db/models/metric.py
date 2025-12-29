from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base

class Metric(Base):
    __tablename__ = "metrics"

    id: Mapped[int] = mapped_column(primary_key=True)
    run_id: Mapped[str] = mapped_column(index=True)

    t: Mapped[int]  # timestep

    dropped: Mapped[float]
    total_demand: Mapped[float]
    availability: Mapped[float]

    util_avg: Mapped[float]
    util_max: Mapped[float]

    spillover: Mapped[float]
    cost: Mapped[float]

    slo_violated: Mapped[bool]
