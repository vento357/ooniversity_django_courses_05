# -*- coding: utf-8 -*-
from django import forms
from feedbacks.models import Feedback


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        exclude = ['create_date', ]