import json
from pathlib import Path

from .hockey import Hockey

with open(Path(__file__).parent / "info.json") as fp:
    __red_end_user_data_statement__ = json.load(fp)["end_user_data_statement"]


async def setup(bot):
    cog = Hockey(bot)
    await cog.initialize_pickems()
    bot.add_cog(cog)
