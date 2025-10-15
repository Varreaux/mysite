import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

    def test_question_creation(self):
        """Test that we can create a Question with text and pub_date."""
        question_text = "What is your favorite color?"
        pub_date = timezone.now()
        question = Question(question_text=question_text, pub_date=pub_date)
        
        self.assertEqual(question.question_text, question_text)
        self.assertEqual(question.pub_date, pub_date)
        self.assertEqual(str(question), question_text)
