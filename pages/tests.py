from django.test import TestCase
from django.urls import reverse


class PagesTests(TestCase):
    def test_home_page(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/home.html")
        self.assertContains(response, "Ласкаво просимо")

    def test_about_page(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/about.html")
        self.assertContains(response, "Про проєкт")

    def test_contact_page(self):
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/contact.html")
        self.assertContains(response, "Контакти")

    def test_health_endpoint(self):
        response = self.client.get(reverse("health"))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {"status": "ok"})

    def test_unknown_page_returns_404(self):
        response = self.client.get("/this-page-does-not-exist/")
        self.assertEqual(response.status_code, 404)

    def test_navigation_links_present(self):
        response = self.client.get(reverse("home"))
        for name in ("home", "about", "contact"):
            self.assertContains(response, f'href="{reverse(name)}"')
