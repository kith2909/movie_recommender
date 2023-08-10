from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from .models import ChatMessage, Answer, Profile, Job
from .forms import AnswerForm
from .chat_ai import get_bot_response
from .static.models.extra import images_print, model_preferred, model_responsibilities, s_killer
import imblearn  # Check if this is used, if not, remove
import uuid
import numpy as np  # Check if this is used, if not, remove

# Constant for cookie name
AI_COOK = 'chat_to_grow'


class AnswerView(generic.FormView):
    template_name = 'recommend_edu//results.html'
    form_class = AnswerForm

    def get(self, request):
        # Get or create a user profile based on the cookie
        user, created = Profile.objects.get_or_create(user_id=self.request.COOKIES.get(AI_COOK))
        if created:
            user.save()
        form = self.form_class(profile_id=user.id)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the votes page after a successful post
            return redirect('recommend_edu:votes')
        return render(request, self.template_name, {'form': form})


class VotesView(generic.ListView):
    template_name = 'recommend_edu//votes.html'

    def get(self, request):
        user_id = self.request.COOKIES.get(AI_COOK)
        # Get or create a user profile based on the cookie
        user, created = Profile.objects.get_or_create(user_id=user_id)
        if created:
            user.save()

        # Fetch the latest answer given by the user
        answer = Answer.objects.filter(profile_id=user.id).latest('id')

        # Update user attributes based on the answer
        user.age = answer.mean_age
        user.hobbies = answer.hobbies
        user.location = answer.location
        user.language = answer.lang

        # Compute skills for the user
        skills = s_killer(answer.feedback,
                          answer.subjects,
                          answer.work_in_team,
                          answer.logic_1,
                          answer.logic_2,
                          answer.tech_1,
                          answer.tech_2,
                          answer.responsible)

        # Update user skills and related attributes
        user.skills = skills
        user.goal = model_preferred.predict([skills])
        user.goal_extra = model_responsibilities.predict([skills])
        user.img = images_print[user.goal[0]]
        user.save()

        return render(request, self.template_name, {'profile': user})


class ChatView(generic.ListView):
    template_name = "recommend_edu//chat.html"
    context_object_name = "chat_history"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_id'] = self.request.COOKIES.get(AI_COOK)
        return context

    def get_queryset(self):
        user_id = self.request.COOKIES.get(AI_COOK)
        # Return the chat history in descending order of timestamp
        return ChatMessage.objects.filter(user_id=user_id).order_by('-timestamp')

    def post(self, request, *args, **kwargs):
        '''
        Analyze user profile using a pretrained OpenAI model.
        :return: bot-assistant response. For details, check chat_ai.py.
        '''
        user_message = request.POST.get('user_message')
        user_id = request.COOKIES.get(AI_COOK)
        user = Profile.objects.get(user_id=user_id)

        # Extract necessary attributes from user profile
        context = user.advice_text
        try:
            bot_response = get_bot_response(
                user_message,
                skills=user.skills,
                goal=user.goal,
                mean_age=user.age,
                location=user.location,
                lang=user.language,
                advice=user.advice,
                context=context
            )
        except Exception as e:
            print('Exception', e, user_id)
            # Get a generic bot response in case of exception
            bot_response = get_bot_response(user_message)

        # Check response length and update user's advice if needed
        if len(bot_response) > 500 and not user.advice:
            user.advice = True
            user.advice_text = bot_response
            user.save()

        # Create a new chat message entry
        ChatMessage.objects.create(user_id=user_id, user_message=user_message, bot_response=bot_response)
        response = self.get(request, *args, **kwargs)
        response.set_cookie(AI_COOK, user_id)
        return response


class IndexView(generic.TemplateView):
    template_name = "recommend_edu/index.html"
    context_object_name = "main_page"

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        unique_id = str(uuid.uuid4())  # Generate a unique UUID
        response.set_cookie(AI_COOK, unique_id)  # Set the cookie with UUID
        return response
