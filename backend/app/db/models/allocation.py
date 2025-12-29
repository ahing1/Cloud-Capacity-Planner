from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base

class Allocation(Base):
    __tablename__ = "allocations"

    id: Mapped[int] = mapped_column(primary_key=True)
    run_id: Mapped[str] = mapped_column(index=True)
    t: Mapped[int]

    demand_region: Mapped[str]
    supply_region: Mapped[str]
    sku: Mapped[str]

    amount: Mapped[float]
