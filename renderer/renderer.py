class Renderer:
    async def parse(self, msg: str): ...

    def session(self): ...


class FullTextRenderer(Renderer):
    async def parse(self, msg: str): ...
