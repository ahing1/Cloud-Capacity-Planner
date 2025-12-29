from pydantic import BaseModel, Field
from typing import Dict, Any, Optional
from datetime import datetime

class RunCreate(BaseModel):
    scenario_name: str = Field(min_length=1)
    planner_name: str = Field(min_length=1)
    seed: int = 42
    config: Dict[str, Any] = Field(default_factory=dict)

class RunOut(BaseModel):
    id: str
    scenario_name: str
    planner_name: str
    status: str
    seed: int
    config: Dict[str, Any]
    started_at: datetime