from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ExampleForm(forms.Form):
    machine_vehicle_purchase = forms.TypedChoiceField(
        label = "Machine / Vehicle purchase ?",
        choices = ((1, "Yes"), (0, "No")),
        coerce = lambda x: bool(int(x)),
        widget = forms.RadioSelect,
        initial = '1',
        required = True,
    )

    trading_years = forms.CharField(
        label = "How many years of trading?",
        max_length = 80,
        required = True,
    )

    annual_turnover_in_thousand = forms.CharField(
        label = "What is your annual turnover in thousand?",
        max_length = 80,
        required = True,
    )

    mobile_number = forms.IntegerField(
        label = "Mobile number",
        required = True,
    )

    def __init__(self, *args, **kwargs):
        super(ExampleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'

        self.helper.add_input(Submit('submit', 'Submit'))