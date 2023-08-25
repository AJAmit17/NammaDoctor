from django.shortcuts import render
'''import openai'''
from django.http import JsonResponse
from .models import Chat
import os
# Create your views here.

from django.utils import timezone


'''openai_api_key = os.environ.get('OPENAI_KEY')
openai.api_key = openai_api_key

def ask_openai(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an helpful assistant."},
            {"role": "user", "content": message},
        ]
    )
    
    answer = response.choices[0].message.content.strip()
    return answer'''

# Create your views here.
def chatbot(request):
    chats = Chat.objects.filter(user=request.user)
    if request.method == 'POST':
        message = request.POST.get('message')
        response = 'hii this is my response'
        chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
        chat.save()
        return JsonResponse({
            'message': message,
            'response': response
            })
    return render(request, 'chatbot/chatbot.html', {
        'title': 'AI DocBot'
        })