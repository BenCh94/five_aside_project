from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from random import randint
from models import Player
from forms import NewPlayerForm
# Create your views here.


def get_index(request):
    return render(request, 'index.html')


@login_required(login_url='/login/')
def new_player(request):
    # log.info("Handling new player %s request", request.method)
    if request.method == "POST":
        form = NewPlayerForm(request.POST, request.FILES)
        if form.is_valid():
            player = form.save(commit=False)
            player.user_id = request.user
            player.date_added = timezone.now()
            player.save()
            return redirect(player_details, player.pk)
    else:
        form = NewPlayerForm()
    return render(request, 'newPlayerForm.html', {'form': form})


def player_details(request, id):
    # log.info("Handling post_details %s request", request.method)
    player = get_object_or_404(Player, pk=id)
    return render(request, "playerdetail.html", {'player': player})


def delete_player(request, id):
    player = get_object_or_404(Player, pk=id)
    if player.user_id == request.user:
        player.delete()
        return render(request, 'profile.html', {'player': player})
    else:
        return render(request, 'playerdetail.html', {'player': player})


@login_required(login_url='/login/')
def new_match(request):
    players = Player.objects.filter(user_id_id=request.user.id)
    return render(request, 'newMatch.html', {'players': players})


@login_required(login_url='/login/')
def create_teams(request):
    if request.method == "POST":
        #empty lists to add to
        team1 = []
        team2 = []
        unselected = []
        #Filter players by those selected in checkbox
        selected_players = request.POST.getlist('player-check')
        playing = Player.objects.filter(user_id_id=request.user.id, id__in=selected_players)


        # Assign playing players to team1 or team2
        while len(team1) < 5:
            x = randint(0, len(playing) - 1)
            if playing[x] not in team1:
                team1.append(playing[x])
        for player in playing:
            if player not in team1:
                unselected.append(player)
        while len(team2) < 5:
            y = randint(0, len(unselected) - 1)
            if unselected[y] not in team2:
                team2.append(unselected[y])

    return render(request, 'teams.html', {'team1': team1, 'team2': team2})

@csrf_exempt
def gen_teams(request):
    if request.method == "POST":
        #empty lists to add to
        team1 = []
        team2 = []
        unselected = []
        #Filter players by those selected in checkbox
        selected_players = request.POST.getlist('player-check')
        playing = Player.objects.filter(user_id_id=request.user.id, id__in=selected_players)


        # Assign playing players to team1 or team2
        while len(team1) < 5:
            x = randint(0, len(playing) - 1)
            if playing[x] not in team1:
                team1.append(playing[x])
        for player in playing:
            if player not in team1:
                unselected.append(player)
        while len(team2) < 5:
            y = randint(0, len(unselected) - 1)
            if unselected[y] not in team2:
                team2.append(unselected[y])

    return HttpResponse('ajaxTeams.html',{'team1': team1, 'team2': team2})
