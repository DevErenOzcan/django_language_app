import json
import random
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from language_app.forms import WordsForm
from .models import UserWords, Words, QuestionCount


@login_required(login_url=reverse_lazy("login"))
def home_view(request):
    if request.method == "POST":
        pass
    else:
        return render(request, "home.html")


@login_required(login_url=reverse_lazy("login"))
def quiz_view(request):
    if request.method == "POST":
        now = datetime.now()
        one_day_ago = now - timedelta(days=1)
        one_week_ago = now - timedelta(days=7)
        one_month_ago = now - timedelta(days=30)
        tree_month_ago = now - timedelta(days=90)
        six_month_ago = now - timedelta(days=180)
        one_year_ago = now - timedelta(days=365)

        user = request.user
        words = []
        word_count = 0
        question_count = QuestionCount.objects.get(id=user.id)
        unique_words = set()  # Using a set to keep track of unique words

        userwords = []
        all_userwords = list(UserWords.objects.filter(user_id=user.id, is_learned=0))  # Fetch all words from the database
        for all_userword in all_userwords:
            if all_userword.corect_count == 0:
                userwords.append(Words.objects.get(id=all_userword.word_id))
            if all_userword.corect_count == 1 and all_userword.updated_date < one_day_ago:
                userwords.append(Words.objects.get(id=all_userword.word_id))
            if all_userword.corect_count == 2 and all_userword.updated_date < one_week_ago:
                userwords.append(Words.objects.get(id=all_userword.word_id))
            if all_userword.corect_count == 3 and all_userword.updated_date < one_month_ago:
                userwords.append(Words.objects.get(id=all_userword.word_id))
            if all_userword.corect_count == 4 and all_userword.updated_date < tree_month_ago:
                userwords.append(Words.objects.get(id=all_userword.word_id))
            if all_userword.corect_count == 5 and all_userword.updated_date < six_month_ago:
                userwords.append(Words.objects.get(id=all_userword.word_id))
            if all_userword.corect_count == 6 and all_userword.updated_date < one_year_ago:
                userwords.append(Words.objects.get(id=all_userword.word_id))

        while word_count < question_count.ask_count and len(unique_words) < len(userwords):
            random_word = random.choice(userwords)
            if random_word.english not in unique_words:
                word_count += 1
                unique_words.add(random_word.english)
                choises = [random_word.turkish]
                selected_choises = random.sample(userwords, 4)
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
