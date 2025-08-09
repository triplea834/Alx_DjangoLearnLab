# api/test_views.py
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token

# Import the models from your app (adjust the import path if needed)
from api.models import Author, Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        # API client
        self.client = APIClient()

        # Create a user and token for authenticated tests
        self.user = User.objects.create_user(username="tester", password="testpass123")
        self.token = Token.objects.create(user=self.user)

        # Create an author and a couple of books
        self.author = Author.objects.create(name="Author One")
        self.book1 = Book.objects.create(title="First Book", publication_year=2000, author=self.author)
        self.book2 = Book.objects.create(title="Second Book", publication_year=2010, author=self.author)

        # Endpoint URLs (adjust if your URL prefix is different)
        self.list_url = "/api/books/"
        self.detail_url = lambda pk: f"/api/books/{pk}/"

    def _results_from_response(self, resp):
        """Helper: return list of results whether paginated or not."""
        data = resp.data
        if isinstance(data, dict) and "results" in data:
            return data["results"]
        return data

    def test_list_books_returns_200_and_correct_count(self):
        resp = self.client.get(self.list_url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        results = self._results_from_response(resp)
        # should contain at least the two created books
        self.assertGreaterEqual(len(results), 2)

    def test_retrieve_book_detail(self):
        resp = self.client.get(self.detail_url(self.book1.id))
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data.get("title"), self.book1.title)
        self.assertEqual(int(resp.data.get("publication_year")), self.book1.publication_year)

    def test_create_book_requires_authentication(self):
        payload = {"title": "New Book", "publication_year": 2022, "author": self.author.id}
        resp = self.client.post(self.list_url, payload, format="json")
        # either UNAUTH or FORBIDDEN depending on configuration
        self.assertIn(resp.status_code, (status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN))

    def test_create_book_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")
        payload = {"title": "New Book", "publication_year": 2022, "author": self.author.id}
        resp = self.client.post(self.list_url, payload, format="json")
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        # ensure new book exists
        self.assertTrue(Book.objects.filter(title="New Book").exists())

    def test_update_book_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")
        payload = {"title": "First Book (Updated)"}
        resp = self.client.patch(self.detail_url(self.book1.id), payload, format="json")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "First Book (Updated)")

    def test_delete_book_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")
        resp = self.client.delete(self.detail_url(self.book2.id))
        self.assertIn(resp.status_code, (status.HTTP_204_NO_CONTENT, status.HTTP_200_OK))
        self.assertFalse(Book.objects.filter(pk=self.book2.id).exists())

    def test_search_filtering(self):
        # assume SearchFilter is enabled on title/author
        resp = self.client.get(self.list_url + "?search=First")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        results = self._results_from_response(resp)
        # expect at least 1 matching book
        self.assertTrue(any("First" in r.get("title", "") for r in results))

    def test_ordering(self):
        # check ordering by publication_year descending
        resp = self.client.get(self.list_url + "?ordering=-publication_year")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        results = self._results_from_response(resp)
        years = [int(item.get("publication_year")) for item in results]
        # years should be in descending order
        self.assertEqual(years, sorted(years, reverse=True))

