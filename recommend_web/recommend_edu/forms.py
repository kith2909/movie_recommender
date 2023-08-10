from django import forms
from .models import Answer, Profile

LOGIC_CHOICES = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4')
]


class AnswerForm(forms.ModelForm):
    profile_id = forms.IntegerField(widget=forms.HiddenInput)

    hobbies = forms.CharField(label='Enter your hobbies here',
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    mean_age = forms.IntegerField(label='Please write you age',
                                  widget=forms.NumberInput(attrs={'class': 'form-control'}))
    work_in_team = forms.BooleanField(label='Will you prefer work in team most of the time, than alone?',
                                      help_text='Check, if you prefer to work with people',
                                      required=False, widget=forms.CheckboxInput(attrs={'class': 'custom-checkbox'}))
    stubbornness_rate = forms.IntegerField(
        label='"People always more important, than goals". Rate 0, if you totally disagree'
              'and rate 5 if you totally agree with this frase',
        widget=forms.NumberInput(attrs={'class': 'select-control'}))
    location = forms.CharField(label='Location', help_text='Enter your location',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    subjects = forms.CharField(label='Write two favorite subjects in school or university',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    feedback = forms.CharField(
        label="For what skills you've got the best feedback from your colleagues or friends in last 3 years",
        help_text='Enter best feedback in few words',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    lang = forms.ChoiceField(
        label='What is your level for national language in country, that you want to  study or work?',
        choices=[(1, 'A1'), (2, 'A2'), (3, 'B1'), (4, 'B2'), (5, 'C1'), (6, 'Native')],
        widget=forms.Select(attrs={'class': 'form-control'}))
    responsible = forms.ChoiceField(
        label='If there is a less pleasant task, that I need to do:',
        help_text='1. I will still finish it because it is my responsibility</br>'
                  '2. Instead of stressing me out, I would better find someone else to do it,'
                  ' and then I just check.</br>'
                  '3. I have the right to protest to my boss</br>'
                  '4. I will try finish it even though it feels heavy, but do it as slow as possible</br>'
                  '5. I ask my co-workers to help solve it, but do it mostly myself',
        choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')],
        widget=forms.Select(attrs={'class': 'form-control'}))
    logic_1 = forms.ChoiceField(
        label='Sam was preparing for a final presentation and studied late into the night. '
              'The following morning, he overslept and realized he would be late for the '
              'final presentation. In his rush,  Sam did not notice his untied shoelaces, '
              'tripped, and sprained his ankle. He had to be taken to the hospital.  His '
              'group mates came to visit him, curious about what had caused Sams mishap. '
              'Which of the following conclusions is most correct?',
        help_text='1. Sam sprained his ankle because he did not have breakfast.</br>'
                  '2. Sam\'s group mates visited him at the hospital because they wanted '
                  'to understand why Sam was late for the final presentation.</br>'
                  '3. Sam did not notice his shoelaces because he overslept.</br>'
                  '4. Sam sprained his ankle because he studied late into the night.',

        choices=LOGIC_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}))
    logic_2 = forms.ChoiceField(
        label='Parvin likes Rakib. Who likes Rakib likes Carmine. Parvin likes only smart men. So: ',
        help_text='1. Carmine is not a smart man</br>'
                  '2. Carmine is a smart man</br>'
                  '3. Rakib and Carmine like Parvin</br>'
                  '4. Parvin does not like Rakib</br>',
        choices=LOGIC_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}))
    tech_1 = forms.ChoiceField(
        label='Abishek traveled from Japan to Indonesia. '
              'In Indonesia, he departed by plane from Cengkareng, '
              'Jakarta to Jayapura. The plane took off from Jakarta '
              'airport at 20.00 local time and landed at Jayapura '
              'airport at 06.00 local time. If during the flight the plane '
              'stops at Surabaya and Makassar airports for 30 minutes each, '
              'how long will the entire Danish journey take?',
        help_text='1. 9 hours</br>'
                  '2. 10 hours</br>'
                  '3. 7 hours</br>'
                  '4. 12 hours</br>',
        choices=LOGIC_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}))
    tech_2 = forms.ChoiceField(
        label='It takes 6 people for three days to upload HUGE '
              'amount of data and not to be '
              'blocked. How many people are needed if the Upload is to be '
              'completed in 1/2 day?',
        help_text='1. 72 people</br>'
                  '2. 36 people</br>'
                  '3. 18 people</br>'
                  '4. 9 people</br>',
        choices=LOGIC_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Answer
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        initial_profile_id = kwargs.pop('profile_id', None)
        super(AnswerForm, self).__init__(*args, **kwargs)
        if initial_profile_id:
            self.fields['profile_id'].initial = initial_profile_id
