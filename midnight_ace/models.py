from django.db import models


class Card(models.Model):
  suit = models.CharField(max_length=10)
  rank = models.CharField(max_length=5)
  value = models.IntegerField()

  def __str__(self):
    return f"{self.rank} of {self.suit} (Value: {self.value})"


class Player(models.Model):
  name = models.CharField(max_length=100)
  score = models.IntegerField()

  def __str__(self):
    return f"{self.name} (Score: {self.score})"


class Game(models.Model):
  name = models.CharField(max_length=100)
  players = models.ManyToManyField(Player, related_name="games_played")
  current_turn = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="current_turn_for_game")
  deck = models.ManyToManyField(Card)
  pot = models.IntegerField()
  status = models.CharField(max_length=20)

  def __str__(self):
    player_names = ', '.join(player.name for player in self.players.all())
    return f"{self.name} (Status: {self.status}, Players: {player_names}, Pot: {self.pot})"


class Round(models.Model):
  number = models.IntegerField()
  active_players = models.ManyToManyField(Player, related_name="active_rounds")
  community_cards = models.ManyToManyField(Card)
  betting_round = models.CharField(max_length=20)
  winners = models.ManyToManyField(Player, related_name="winning_rounds")

  def __str__(self):
    active_player_names = ', '.join(player.name for player in self.active_players.all())
    community_card_names = ', '.join(card.__str__() for card in self.community_cards.all())
    winner_names = ', '.join(player.name for player in self.winners.all())

    return (
      f"Round {self.number} "
      f"(Betting Round: {self.betting_round}, Active Players: {active_player_names}, "
      f"Community Cards: {community_card_names}, Winners: {winner_names})")


class Bet(models.Model):
  player = models.ForeignKey(Player, on_delete=models.CASCADE)
  amount = models.IntegerField()
  bet_type = models.CharField(max_length=10)

  def __str__(self):
    return f"{self.player.name} - {self.amount} ({self.bet_type})"


class Deck(models.Model):
  cards = models.ManyToManyField(Card, related_name="decks_containing")
  shuffled = models.BooleanField()
  drawn_cards = models.ManyToManyField(Card, related_name="decks_drawn_from")

  def __str__(self):
        return f"Deck (Shuffled: {self.shuffled}, Cards: {self.cards.count()}, Drawn: {self.drawn_cards.count()})"


