from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Game
from .forms import gameForm, PostSearchForm
from django.views.generic.edit import FormView
from django.db.models import Q 

# Create your views here.

def gamehome(request):
    game = Game.objects.all()
    gameList = Game.objects.all()
    paginator = Paginator(gameList, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'gamehome.html',{'game' : game, 'posts' : posts})

def gamedetail(request, game_id):
    game_detail = get_object_or_404(Game, pk = game_id)
    return render(request, 'gamedetail.html' ,{'game' : game_detail})

def gamenew(request):
    if request.method == 'POST': #폼 다채우고 저장버튼 눌렀을 때
        form = gameForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.created_at = timezone.now()
            post.save()
            return redirect('gamedetail', post.id)
        return redirect('gamehome')
    else:  #글을 쓰기위해 들어갔을 때
        form = gameForm()
        return render(request,'gamenew.html', {'form':form})


def gameedit(request, game_id):
    post = get_object_or_404(Game, pk = game_id)
    if request.method == 'GET':  #수정하려고 들어갔을 때
        form = gameForm(instance = post)
        return render(request, 'gameedit.html', {'form' : form})
    else:   #수정 끝나고 수정 버튼을 눌렀을 때
        form = gameForm(request.POST, request.FILES, instance = post)
        if form.is_valid():
            post = form.save(commit = False)
            post.created_at = timezone.now()
            post.save()
            return redirect('/gameboard/gamedetail/' + str(game_id))
        return redirect('gamehome')

def gamedelete(request, game_id):
    deletegame =  Game.objects.get(id = game_id)
    deletegame.delete()
    return redirect('gamehome')

def gamesearch(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        searched_posts = Game.objects.filter(Q(title__icontains=searched) | Q(content__icontains=searched))
        return render(request, 'gamesearch.html', {'searched':searched, 'searched_posts':searched_posts})

    else:
        return render(request, 'gamesearch.html', {}) 