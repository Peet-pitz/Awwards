from django.test import TestCase
from .models import Profile, Project

# Create your tests here.

class ProfileTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.new_profile =Profile(photo="image.jpeg",bio="this is to test if it can work",contact = "0750995069")

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))

    #Testing Save Method
    def test_save_method(self):
        self.new_profile.save_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)>0)

    def test_delete_method(self):
        self.new_profile.save_profile()
        self.new_profile.delete_profile()

class ProjectTestClass(TestCase):


    def setUp(self):
        self.new_project=Project(title="Testing",image="image.jpeg",description="best social site",link="https://w3resource.com",design=4,usability=4,content=4)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_project,Project))


    def test_save_method(self):
        '''
        Function that tests whether an image is saved to database
        '''
        self.new_project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)

    def test_delete_method(self):
        '''
        Function that tests whether an image can be deleted from the database
        '''
        self.new_project.save_project()
        self.new_project.delete_project()