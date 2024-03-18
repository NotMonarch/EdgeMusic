from EDGEMUSIC.core.bot import EDGE
from EDGEMUSIC.core.dir import dirr
from EDGEMUSIC.core.git import git
from EDGEMUSIC.core.userbot import Userbot
from EDGEMUSIC.misc import dbb, heroku, sudo

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