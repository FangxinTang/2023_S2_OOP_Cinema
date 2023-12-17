"""For endpoints"""


import litestar as ls
from litestar import status_codes
from sqlalchemy.ext import asyncio as sa_asyncio

from .. import service as global_service
from . import models


class TemplateRoutes(ls.Controller):
    """API routes for CRUD operations on the TEMPLATE model."""

    path = "/TEMPLATE"

    @ls.get("/test")
    async def test_route(self) -> dict:
        """Test route for TEMPLATE."""
        return {"path": self.path, "result": "success"}

    @ls.get("/")
    async def get_TEMPLATEs(
        self, request: ls.Request, transaction: sa_asyncio.AsyncSession
    ) -> list[models._TEMPLATE]:
        query = await global_service.get_all(
            db_session=transaction, model=models._TEMPLATE
        )
        return query

    @ls.get("/{template_id:str}")
    async def get__TEMPLATE(
        self,
        request: ls.Request,
        transaction: sa_asyncio.AsyncSession,
        template_id: str,
    ) -> models._TEMPLATE:
        query: models._TEMPLATE = await global_service.get_one_by_id(
            db_session=transaction, model=models._TEMPLATE, model_id=template_id
        )
        if query:
            return query
        else:
            return ls.Response(status_code=status_codes.HTTP_400_BAD_REQUEST)

    @ls.post("/")
    async def create__TEMPLATEs(
        self,
        request: ls.Request,
        data: models._TEMPLATE,
        transaction: sa_asyncio.AsyncSession,
    ) -> models._TEMPLATE:
        return {"path": self.path}

    @ls.patch(
        "/{template_id:str}",
    )
    async def update__TEMPLATE(
        self,
        request: ls.Request,
        template_id: str,
        data: models._TEMPLATE,
        transaction: sa_asyncio.AsyncSession,
    ) -> models._TEMPLATE:
        ...
        return {"path": self.path}

    @ls.delete("/{template_id:str}")
    async def delete__TEMPLATE(
        self, template_id: str, transaction: sa_asyncio.AsyncSession
    ) -> None:
        ...
        return None
