import uvicorn
from fastapi import FastAPI, Depends
from starlette.middleware.cors import CORSMiddleware

from dependencies import get_db
from routers import user, item, location, microcategory
from db.models import user as t_user, item as t_item, associations as t_associations
from db.db import engine, SessionLocal
import alembic.config

app = FastAPI(
    title="Purple It Hack. Avtito track by BruhMisis"
)

app.include_router(user.router)
app.include_router(item.router)
app.include_router(location.router)
app.include_router(microcategory.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*s"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

alembicArgs = [
    'upgrade', 'head',
]
alembic.config.main(argv=alembicArgs)

# t_user.Base.metadata.create_all(engine)
# t_item.Base.metadata.create_all(engine)
# t_associations.Base.metadata.create_all(engine)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80)
