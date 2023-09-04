from django.http import JsonResponse
from .models import Card
from .models import Player
from .serializers import Midnight_aceSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def card_list(request, format=None):
  if request.method == 'GET':
    cards = Card.objects.all()
    serializer = Midnight_aceSerializer(cards, many=True)
    return Response(serializer.data)
    # serializer = Midnight_aceSerializer(cards, many=True)
    # return JsonResponse({"cards": serializer.data}, )

  if request.method == 'POST':
    serializer = Midnight_aceSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def card_detail(request, suit, format=None):
  try:
    cards = Card.objects.get(pk=suit)
  except Card.DoesnotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = Midnight_aceSerializer(cards)
    return Response(serializer.data)


  elif request.method == 'PUT':
    serializer = Midnight_aceSerializer(cards, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
    cards.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# player

@api_view(['GET', 'POST'])
def player_list(request, format=None):
  if request.method == 'GET':
    players = Player.objects.all()
    serializer = Midnight_aceSerializer(players, many=True)
    return Response(serializer.data)
    # serializer = Midnight_aceSerializer(cards, many=True)
    # return JsonResponse({"cards": serializer.data}, )

  if request.method == 'POST':
    serializer = Midnight_aceSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def player_detail(request, score, format=None):
  try:
    players = Player.objects.get(pk=score)
  except Player.DoesnotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = Midnight_aceSerializer(players)
    return Response(serializer.data)


  elif request.method == 'PUT':
    serializer = Midnight_aceSerializer(players, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
    players.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# game
@api_view(['GET', 'POST'])
def game_list(request, format=None):
  if request.method == 'GET':
    games = Game.objects.all()
    serializer = Midnight_aceSerializer(games, many=True)
    return Response(serializer.data)
    # serializer = Midnight_aceSerializer(cards, many=True)
    # return JsonResponse({"cards": serializer.data}, )

  if request.method == 'POST':
    serializer = Midnight_aceSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def game_detail(request, players, format=None):
  try:
    games = Game.objects.get(pk=players)
  except Game.DoesnotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = Midnight_aceSerializer(games)
    return Response(serializer.data)


  elif request.method == 'PUT':
    serializer = Midnight_aceSerializer(games, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
    games.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# round
@api_view(['GET', 'POST'])
def round_list(request, format=None):
  if request.method == 'GET':
    rounds = Round.objects.all()
    serializer = Midnight_aceSerializer(rounds, many=True)
    return Response(serializer.data)
    # serializer = Midnight_aceSerializer(cards, many=True)
    # return JsonResponse({"cards": serializer.data}, )

  if request.method == 'POST':
    serializer = Midnight_aceSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def round_detail(request, number, format=None):
  try:
    rounds = Round.objects.get(pk=number)
  except Round.DoesnotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = Midnight_aceSerializer(cards)
    return Response(serializer.data)


  elif request.method == 'PUT':
    serializer = Midnight_aceSerializer(rounds, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
    rounds.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# bet

@api_view(['GET', 'POST'])
def bet_list(request, format=None):
  if request.method == 'GET':
    bets = Bet.objects.all()
    serializer = Midnight_aceSerializer(bets, many=True)
    return Response(serializer.data)
    # serializer = Midnight_aceSerializer(cards, many=True)
    # return JsonResponse({"cards": serializer.data}, )

  if request.method == 'POST':
    serializer = Midnight_aceSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def bet_detail(request, player, format=None):
  try:
    bet_detail = Bet.objects.get(pk=player)
  except Bet.DoesnotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = Midnight_aceSerializer(bet_detail)
    return Response(serializer.data)


  elif request.method == 'PUT':
    serializer = Midnight_aceSerializer(bets, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
    bets.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# deck
  @api_view(['GET', 'POST'])
  def deck_list(request, format=None):
    if request.method == 'GET':
      decks = Deck.objects.all()
      serializer = Midnight_aceSerializer(cards, many=True)
      return Response(serializer.data)
      # serializer = Midnight_aceSerializer(cards, many=True)
      # return JsonResponse({"cards": serializer.data}, )

    if request.method == 'POST':
      serializer = Midnight_aceSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

  @api_view(['GET', 'PUT', 'DELETE'])
  def deck_detail(request, cards, format=None):
    try:
      decks = Deck.objects.get(pk=cards)
    except Deck.DoesnotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
      serializer = Midnight_aceSerializer(cards)
      return Response(serializer.data)


    elif request.method == 'PUT':
      serializer = Midnight_aceSerializer(decks, data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
      decks.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)



