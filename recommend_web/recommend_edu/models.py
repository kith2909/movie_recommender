from django.db import models


class Profile(models.Model):
    '''
    Profile based on testing and prediction
    '''
    user_id = models.TextField()
    skills = models.TextField(default='')  # Based on test results
    goal = models.TextField(default='')  # Based on prediction
    goal_extra = models.TextField(default='')  # Based on prediction
    age = models.IntegerField(default=0)
    hobbies = models.TextField(default='')  # Based on test results
    location = models.TextField(default='')  # Based on test results
    language = models.TextField(default='')  # Based on test results
    img = models.TextField(default='')  # Based on prediction
    advice = models.BooleanField(default=False)  # Based on chat_ai
    advice_text = models.TextField(default='')  # Based on chat_ai

    def __str__(self):
        return f'{self.user_id} {self.skills} {self.goal} {self.language}'


class ChatMessage(models.Model):
    '''
    Context prompt for LLM model
    '''
    user_id = models.TextField()
    user_message = models.TextField()
    bot_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user_id} {self.user_message} {self.bot_response} {self.timestamp}'


class Answer(models.Model):
    '''
    First testing results
    '''
    profile_id = models.IntegerField(default='')
    hobbies = models.TextField(default='')
    mean_age = models.IntegerField(default=100)
    work_in_team = models.BooleanField(default=False)
    stubbornness_rate = models.IntegerField(default=0)
    location = models.TextField(default='Berlin, Germany')
    subjects = models.TextField(default='')
    feedback = models.TextField(default='')
    lang = models.TextField(default='')
    responsible = models.TextField(default='')
    logic_1 = models.IntegerField(default=0)
    logic_2 = models.IntegerField(default=0)
    tech_1 = models.IntegerField(default=0)
    tech_2 = models.IntegerField(default=0)


def __str__(self):
    return f'{self.profile_id} {self.mean_age} {self.feedback} {self.subjects}'


class Job(models.Model):
    '''
    Next step analysis
    '''
    company = models.CharField(max_length=300)
    title = models.CharField(max_length=300)
    category = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    responsibilities = models.TextField()
    minimum_qualifications = models.TextField()
    preferred_qualifications = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        out_str = f'{self.company} {self.title} {self.category} {self.location} {self.responsibilities} ' \
                  f'{self.minimum_qualifications} {self.preferred_qualifications} {self.salary}'
        return out_str
