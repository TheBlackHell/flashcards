from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import FlashcardSetForm, FlashcardForm, EditFlashcardSetForm, SearchFlashcardSetForm
from .models import FlashcardSet, Flashcard
import random as rn
import string as st
import hashlib as hl

def main(response):
    return render(response, 'main.html', {})


def create_flashcardset(request):
    if request.method == "POST":
        form = FlashcardSetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data["setname"] + form.cleaned_data["ersteller"] + form.cleaned_data["passwort"]
            m = hl.sha256()
            m.update(data.encode())
            identifier = m.hexdigest()
            flashcard_set = FlashcardSet(name=form.cleaned_data["setname"], 
                                         creator=form.cleaned_data["ersteller"],
                                         password=form.cleaned_data["passwort"],
                                         description=form.cleaned_data["beschreibung"], 
                                         identifier=identifier) 
            flashcard_set.save()
            return HttpResponseRedirect(f"/create/{identifier}")
    else: 
        form = FlashcardSetForm()
    return render(request, 'create_flashcardset.html', {"form": form})


def create_flashcards(request, id):
    try:
        ls = FlashcardSet.objects.get(identifier=id)
    except FlashcardSet.DoesNotExist:
        return edit_flashcardset(request, ["Karteikartenset existiert nicht!"])
        

    if request.method == "POST":
        form = FlashcardForm(request.POST)
        if form.is_valid():
            identifier = ''
            characters = st.ascii_letters + st.digits
            data = [x for x in characters]
            for item in rn.choices(data, k=50): 
                identifier += str(item)
            identifier += ls.identifier
            flashcard = Flashcard(value_a=form.cleaned_data["value_a"], 
                                  value_b=form.cleaned_data["value_b"], 
                                  flashcardset=ls,
                                  identifier=identifier) 
            flashcard.save()
            return HttpResponseRedirect(f"/create/{id}")
    else: 
        form = FlashcardForm()

    return render(request, 'create_flashcard.html', {"ls": ls, "form": form})


def view_flashcards(response, id):
    ls = FlashcardSet.objects.get(identifier=id)
    fc = Flashcard.objects.filter(flashcardset=FlashcardSet.objects.get(identifier=id))
    return render(response, 'view_flashcards.html', {"ls": ls, "fc": fc})


def delete_flashcards(response, id, del_id):
    fc_del = Flashcard.objects.get(identifier=del_id)
    fc_del.delete()
    ls = FlashcardSet.objects.get(identifier=id)
    fc = Flashcard.objects.filter(flashcardset=FlashcardSet.objects.get(identifier=id))
    return render(response, 'view_flashcards.html', {"ls": ls, "fc": fc})

def delete_flashcardset(response, id):
    fs_del = FlashcardSet.objects.get(identifier=id)
    fs_del.delete()
    return HttpResponseRedirect(f"/edit")


def edit_flashcardset(request, error= None):
    if request.method == "POST":
        form = EditFlashcardSetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data["setname"] + form.cleaned_data["ersteller"] + form.cleaned_data["passwort"]
            m = hl.sha256()
            m.update(data.encode())
            identifier = m.hexdigest()
            return HttpResponseRedirect(f"/create/{identifier}")
    else: 
        form = EditFlashcardSetForm()
    return render(request, 'edit_flashcardset.html', {"form": form, "error": error})
        
    
def select_flashcardset(request, id:str, error= None):
    fc = []
    identifiers = id.split(sep='id=')

    for item in identifiers: 
        if item != '' and item != '-':
            fc.append(FlashcardSet.objects.get(identifier=item))
    
    if request.method == "POST":
        form = SearchFlashcardSetForm(request.POST)
        if form.is_valid():
            try:
                set = FlashcardSet.objects.get(name=form.cleaned_data["setname"] ,creator=form.cleaned_data["ersteller"])
            except FlashcardSet.DoesNotExist:
                request.method = "GET"
                return select_flashcardset(request, id=id, error=["Karteikartenset existiert nicht!"])
            return HttpResponseRedirect(f"/select/{id}id={set.identifier}")
    else: 
        form = SearchFlashcardSetForm()
    return render(request, 'flashcardset_selection.html', {"form": form, "fc": fc, "error": error})


def learn(response, id, type):
    fc = []
    identifiers = id.split(sep='id=')

    for item in identifiers: 
        if item != '' and item != '-':
            for flashcard in Flashcard.objects.filter(flashcardset=FlashcardSet.objects.get(identifier=item)).order_by('?'):
                fc.append(flashcard)

    rn.shuffle(fc)
    
    learning_type = type[-1:]

    if (type[:-1] == "norev") and (learning_type == '2'):
        learning_type = '1'
        

    if learning_type == "1":
        item = fc[0]
        return render(response, 'learning_types/learn_1.html', {"item": item})
    
    if learning_type == "2":
        item = fc[0]
        return render(response, 'learning_types/learn_2.html', {"item": item})
    
    if learning_type == "3":
        if len(fc) > 1:
            answer = 0
            statement_a = fc[0]
            statement_b = fc[rn.randint(0, 1)]
            if statement_a == statement_b:
                answer = 1
            return render(response, 'learning_types/learn_3.html', {"s_a": statement_a, "s_b": statement_b, "answer": answer})
        else:
            item = fc[0]
            return render(response, 'learning_types/learn_1.html', {"item": item})
        
    if learning_type == "4":
        if len(fc) > 3:
            answer = 0
            statement = fc[0]
            statements = [fc[x] for x in range(4)]
            rn.shuffle(statements)
            for index, item in enumerate(statements):
                if statement == item:
                    answer = index
            statements = list(zip(statements, range(4)))
            return render(response, 'learning_types/learn_4.html', {"s": statement, "sl": statements, "answer": answer})
        else:
            item = fc[0]
            return render(response, 'learning_types/learn_1.html', {"item": item})
