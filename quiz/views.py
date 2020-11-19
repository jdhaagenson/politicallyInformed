from django.shortcuts import render

def create_question(request):
    return render(request, 'quiz.html')


def quiz_view(request):
    return render(request, 'quiz.html')


def save_answer(request):
    return render(request, 'quiz.html')


