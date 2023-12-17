"""For endpoints"""

import litestar as ls


class DatabaseRoutes(ls.Controller):
    """Private route"""

    path = "/_database"

    @ls.get("/test", return_dto=None)
    async def test_route(self) -> dict:
        return {"path": self.path, "result": "success"}
