from rest_framework import serializers
from .models import Card
from .models import Player
from .models import Game
from .models import Round
from .models import Bet
from .models import Deck


class Midnight_aceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Card
    fields = ['suit', 'rank', 'value']


class Midnight_aceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Player
    fields = ['name', 'score']


class Midnight_aceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Game
    fields = ['name', 'players', 'current_turn', 'deck', 'port', 'status']


class Midnight_aceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Round
    fields = ['numbers', 'active-players', 'community_cards', 'betting_rounds', 'winners']


class Midnight_aceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Bet
    fields = ['player', 'amount', 'bet_type']


class Midnight_aceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Deck
    fields = ['cards', 'shuffled', 'drawn_cards']


