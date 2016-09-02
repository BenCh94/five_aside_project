from django.test import TestCase
from views import create_teams

# Create your tests here.


class TeamCreateTests(TestCase):

    def test_status_code(self):
        teams = self.client.get('/create_teams/')
        self.assertEquals(teams.status_code, 200)


