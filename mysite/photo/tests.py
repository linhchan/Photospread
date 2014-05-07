from django.test import TestCase
from django.test import TransactionTestCase
from django.contrib.auth.models import User
from photo.models import Album, Image

FIXTURE = 'photo_test_fixture.json'

class AlbumTestCase(TransactionTestCase):
    fixtures = [FIXTURE, ]

    def setUp(self):
        self.user = User.objects.get(pk=1)
        self.albums = Album.objects.all()

    def test_unicode(self):
    	for e in ['Test', 'Work','Nature', 'Vacation']:
    		expected = e
    		p1 = Album(title=expected)
    		actual = unicode(p1)
    		self.assertEqual(expected, actual)