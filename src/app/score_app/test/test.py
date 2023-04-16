from django.test import TestCase, Client
from django.urls import reverse
from score_app.models import Score

class ScoreAppTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.score1 = Score.objects.create(name='Alice', score=5)
        self.score2 = Score.objects.create(id=100, name='Bob', score=8)

    def test_get_score(self):
        url = reverse("get_score") + "?input=5"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['score'], 6)

    def test_create_user(self):
        url = reverse("create_user")
        data = {'name': 'Charlie', 'score': '7'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Score.objects.count(), 3)

    def test_get_all_users(self):
        url = reverse("get_all_users")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def test_get_user_by_id(self):
        url = reverse("get_user_by_id", args=[100])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_get_user_by_invalid_id(self):
        url = reverse("get_user_by_id", args=[999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()['message'], 'User not found')
