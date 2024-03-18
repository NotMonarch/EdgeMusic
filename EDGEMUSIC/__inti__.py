from EDGEMusic.core.bot import EDGE
from EDGEMusic.core.dir import dirr
from EDGEMusic.core.git import git
from EDGEMusic.core.userbot import Userbot
from EDGEMusic.misc import dbb, heroku, sudo

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = EDGE()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()