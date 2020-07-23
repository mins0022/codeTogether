import json
import os
from django.shortcuts import render
from .models import Board
from django.http import HttpResponse, JsonResponse
from django.views import View
from sign.models import Accounts

def write(request):
  return render(request, 'board/upload.html')

# Create your views here.
def writeBoard(request):
  user_id = request.session['user_id']
  title = request.POST.get('title')  
  content= request.POST.get('content')
  img = request.FILES['img']
  content_type = request.session['user_type']
  # account_id랑 content_type은 게시글 작성 버튼 누를 때 함께 넘겨야 함
  
  account = Accounts.objects.get(user_id=user_id)
  Board(
    user_id = account,
    title = title,
    content = content,
    img = img,
    content_type = content_type
  ).save()

  # 

  return HttpResponse(status= 200)
  # except Exception as e:
  #   return JsonResponse({"message": "오류 발생"}, status = 400)

def boardView(request) :
  b_list = Board.objects.order_by('-content_id')
  return render(request, 'board/board.html', {
    'b_list': b_list,
  })

def q_stu(request):
  return render(request, 'board/q_stu.html')
 
def save_session(request, user_id, user_type):
  request.session['user_id'] = user_id
  request.session['user_type'] = user_type