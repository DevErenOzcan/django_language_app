import json
import random
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from language_app.forms import WordsForm
from .models import UserWords, Words


@login_required(login_url=reverse_lazy("login"))
def home_view(request):
    if request.method == "POST":
        pass
    else:
        return render(request, "home.html")


@login_required(login_url=reverse_lazy("login"))
def quiz_view(request):
    if request.method == "POST":
        words = []
        word_count = 0
        unique_words = set()  # Using a set to keep track of unique words
        all_words = list(Words.objects.all())  # Fetch all words from the database
        while word_count < 6 and len(unique_words) < len(all_words):
            random_word = random.choice(all_words)
            if random_word.english not in unique_words:
                word_count += 1
                unique_words.add(random_word.english)
                choises = [random_word.turkish]
                selected_choises = random.sample(all_words, 4)
                for selected_choise in selected_choises:
                    choises.append(selected_choise.turkish)

                random.shuffle(choises)
                question_data = {
                    'question': random_word.english,
                    # TODO: question resmi eklenecek
                    'choices0': choises[0],
                    'choices1': choises[1],
                    'choices2': choises[2],
                    'choices3': choises[3],
                    'choices4': choises[4],
                }
                words.append(question_data)
        return HttpResponse(json.dumps(words), content_type="application/json")
    else:
        return render(request, "quiz.html")


@login_required(login_url=reverse_lazy("login"))
def add_word_view(request):
    if request.method == 'POST':
        form = WordsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('word_list')
    else:
        form = WordsForm()
    return render(request, 'add_word.html', {'form': form})
