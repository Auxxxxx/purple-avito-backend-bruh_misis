import uvicorn
from fastapi import FastAPI

from routers import user, auth, item
from db.models import user as t_user, item as t_item, associations as t_associations
from db.db import engine
import alembic.config

app = FastAPI(
    title="Purple It Hack. Avtito track by BruhMisis"
)

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(item.router)

alembicArgs = [
    'upgrade', 'head',
]
alembic.config.main(argv=alembicArgs)

# t_user.Base.metadata.create_all(engine)
# t_item.Base.metadata.create_all(engine)
# t_associations.Base.metadata.create_all(engine)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80)
