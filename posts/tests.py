from django.test import TestCase
from django.urls import reverse

from .models import Post


class PostModelTest(TestCase):
    def setUp(self) -> None:
        Post.objects.create(text='jast a test')

    def test_text_content(self) -> None:
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'jast a test')


class HomePageViewTest(TestCase):
    def setUp(self) -> None:
        Post.objects.create(text='this is another test')

    def test_view_url_exist_at_proper_location(self) -> None:
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self)-> None:
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self)->None:
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
