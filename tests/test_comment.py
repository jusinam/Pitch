import unittest
from app.models import Comment


class CommentModelTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the Comment class
    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.content= Content(content = 'pitching')


    def tearDown(self):
        Content.query.delete()


    def test_instance(self):
        self.assertTrue(isinstance(self.content, Content))


    def test_check_instance_variables(self):
        self.assertEquals(self.content.content,'pitchin')
