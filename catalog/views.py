from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import Note, Comment
from django.contrib.auth.mixins import LoginRequiredMixin


"""
Class-based views:

View         = Generic View
ListView     = get a list of records
DetailView   = get a single (detail) record
CreateView   = create a new record
DeleteView   = remove a record
UpdateView   = modify an existing record
LoginView    = LogIn

"""

# Create your views here.

class NoteList(ListView):
    model = Note
    template_name = "catalog/list.html"


#class NoteDetails(LoginRequiredMixin, DetailView):
class NoteDetails(DetailView):
    model = Note
    template_name = "catalog/details.html"

    # getting the data
    def get_context_data(self, **kwargs):
        # this is the base functionality
        context = super().get_context_data(**kwargs)

        # also read the comments
        current_note = self.object
        comments = Comment.objects.filter(note=current_note)
        context["comments"] = comments

        return context 



# expects a POST request
def create_comment(request):
    # get the data
    note_id = request.POST.get("note_id")
    content = request.POST.get("content")
    user = request.user

    # read the Note based on note_id
    note = Note.objects.get(id=note_id)

    # create the comment
    comment = Comment.objects.create(
        author = user,
        content = content,
        note = note
    )
    comment.save()

    return redirect("note_details", note_id)