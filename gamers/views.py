from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import json
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from .models import Player, Game, Winners
from .forms import GameForm, PlayerForm, WinnersForm, LoginForm
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def index(request):
    upcomingGames = Game.objects.filter(played=False).order_by('-pub_date')
    gameList = []
    gameDetail = {}
    gameList2 = []
    gameDetail2 = {}
    games = Game.objects.filter(played=True).order_by('-pub_date')
    winners = Winners.objects.all()
    for game in games:
        gameDetail["id"] = game.id
        gameDetail["name"] = game.name
        gameDetail["pub_date"] = game.pub_date
        gameDetail['image'] = game.image
        gameDetail['host'] =  game.host
        gameDetail["players"] = [player for player in game.player.all()]
        gameDetail["winners"] = winners.filter(game=game.id)
        gameDetail["played"] = game.played
        gameList.append(gameDetail)
        gameDetail={}
        
    for game in gameList:
        gameDetail2["id"] = game["id"]
        gameDetail2["name"] = game["name"]
        gameDetail2["pub_date"] = game["pub_date"]
        gameDetail2['host'] =  game["host"]
        gameDetail2['players'] = [g.discordId for g in game["players"]]
        gameDetail2['winners']=[[w.game.name, w.player.discordId, w.position] for w in game['winners'].filter(game=gameDetail2['id'])]
        gameDetail2["played"] = game["played"]
        gameList2.append(gameDetail2)
        gameDetail2={}
        
    gameForm = GameForm()
    playerForm = PlayerForm()
    winnersForm = WinnersForm()
    gameList2 = json.dumps(gameList2, sort_keys=True, indent=1, cls=DjangoJSONEncoder)
    context = {
        'upcomingGames': upcomingGames,
        'gameList': gameList,
        'gameList2': gameList2,
        'gameForm': gameForm,
        'playerForm': playerForm,
        'winnersForm': winnersForm,
    }
    return render(request, 'index.html', context)

@login_required
def adminpanel(request):
    gameList = []
    gameDetail = {}
    games = Game.objects.all().order_by('-pub_date')
    winners = Winners.objects.all()
    players = Player.objects.all()
    for game in games:
        gameDetail["id"] = game.id
        gameDetail["name"] = game.name
        gameDetail["pub_date"] = game.pub_date
        gameDetail['image'] = game.image
        gameDetail['host'] =  game.host
        gameDetail["players"] = [player for player in game.player.all()]
        gameDetail["winners"] = winners.filter(game=game.id)
        gameDetail["played"] = game.played
        gameList.append(gameDetail)
        gameDetail={}
    gameForm = GameForm()
    playerForm = PlayerForm()
    winnersForm = WinnersForm()
    context = {
        'gameList': gameList,
        'players': players,
        'games': games,
        'gameForm': gameForm,
        'playerForm': playerForm,
        'winnersForm': winnersForm,
    }
    return render(request, 'adminpanel.html', context)

@login_required
def addplayer(request):
    if request.method == 'POST':
        playerForm = PlayerForm(request.POST)
        player = playerForm["discordId"].value()
        try:
            check = Player.objects.get(discordId=player)
            if check:
                return JsonResponse({"error": "failed"}, status=400)
        except ObjectDoesNotExist:
            if playerForm.is_valid():
                playerForm.save()
                return JsonResponse({"status": True}, status=200)
            else:
                error = playerForm.errors
                return JsonResponse({"error": error}, status=400)

@login_required
def addwinners(request):
    if request.method == 'POST':
        winnersForm = WinnersForm(request.POST)
        game=winnersForm['game'].value()
        player = winnersForm['player'].value()
        try:
            check = Winners.objects.get(game=game, player=player)
            if check:
                return JsonResponse({"error":"failed"}, status=400)
        except ObjectDoesNotExist:
            if winnersForm.is_valid():
                winnersForm.save()
                return JsonResponse({"status": True}, status=200)
            else:
                error = winnersForm.errors
                return JsonResponse({"error": error}, status=400)

@login_required    
def addgame(request):
    if is_ajax(request=request) and request.method == 'POST':
        gameForm = GameForm(request.POST, request.FILES)
        if gameForm.is_valid():
            gameForm.save()
            return JsonResponse({"success": True}, status=200)
        else:
            error = gameForm.errors
            return JsonResponse({"error": error}, status=400)
        
    return HttpResponse('error adding game')

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

@login_required
def togglestatus(request):
    if is_ajax(request=request) and request.method == 'POST':
        gameid = request.POST.get('gameid')
        game = Game.objects.get(id=gameid)
        if game.played == False:
            game.played = True
        else:
            game.played = False
        game.save()
        return JsonResponse({"data": game.played}, status = 200)

@login_required 
def playerstogame(request):
    if is_ajax(request=request) and request.method == 'POST':
        gameid = request.POST.get('gameid')
        players = request.POST.get('players')
        listofplayer = players.replace(',', ' ').split(" ")
        game = Game.objects.get(id=gameid)
        for player in listofplayer:
            p = Player.objects.get(id = player)
            game.player.add(p)
        game.save()
        return JsonResponse({"success": True}, status=200)