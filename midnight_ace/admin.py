from django.contrib import admin
from .models import Card
from .models import Player
from .models import Game
from .models import Round
from .models import Bet
from .models import Deck

admin.site.register(Card)
admin.site.register(Player)
admin.site.register(Game)
admin.site.register(Round)
admin.site.register(Bet)
admin.site.register(Deck)
