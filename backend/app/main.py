from fastapi import FastAPI
from app.api.health import router as health_router
from app.api.runs import router as runs_router

app = FastAPI(
    title="Cloud Capacity Planner Simulator API",
    version="0.1.0",
)

# Routers
app.include_router(health_router)
app.include_router(runs_router)


@app.get("/version", tags=["meta"])
async def version():
    return {"version": app.version}
