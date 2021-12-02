from django.contrib.auth.forms import UserCreationForm

class TodaymovieUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True