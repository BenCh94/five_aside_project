from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
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


def new_match(request):
    return render(request, 'newMatch.html')