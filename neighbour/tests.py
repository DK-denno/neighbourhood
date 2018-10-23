from django.test import TestCase
from django.contrib.auth.models import User
from .models import Neighbourhoods,Profile,Businesses,Message,Comments
# Create your tests here.



class UserTest(TestCase):
    def setUp(self):
        self.user=User(username='dk',first_name='d',last_name='k',email='dk@gmail.com')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.user,User))
    
    def test_data(self):
        self.assertTrue(self.user.username,"dk")
        self.assertTrue(self.user.first_name,"d")
        self.assertTrue(self.user.last_name,'k')
        self.assertTrue(self.user.email,'dk@gmail.com')
    
    def test_save(self):
        self.user.save()
        users = User.objects.all()
        self.assertTrue(len(users)>0)
    
    def test_delete(self):
        user = User.objects.filter(id=1)
        user.delete()
        users = User.objects.all()
        self.assertTrue(len(users)==0)

class ProfileTest(TestCase):
    def setUp(self):
        self.new_user=User(username='aa',first_name='a',last_name='a',email='a@gmail.com')
        self.new_user.save()
        self.new_profile=Profile(user=self.new_user,bio='wueh')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))
    
    def test_data(self):
        self.assertTrue(self.new_profile.bio,"wuehh")
        self.assertTrue(self.new_profile.user,self.new_user)

    def test_save(self):
        self.new_profile.save()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)
    
    def test_delete(self):
        profile = Profile.objects.filter(id=1)
        profile.delete()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)==0)

    
    def test_edit_profile(self):
        self.new_profile.save()
        self.update_profile = Profile.objects.filter(bio='wueh').update(bio = 'aaabbbcccddd')
        self.updated_profile = Profile.objects.get(bio='aaabbbcccddd')
        self.assertTrue(self.updated_profile.bio,'aaabbbcccddd')


class NeighbourhoodTest(TestCase):
    def setUp(self):
        self.user=User(username='dk',first_name='d',last_name='k',email='dk@gmail.com')
        self.user.save()
        self.admin=User(username='kd',first_name='d',last_name='k',email='dk@gmail.com')
        self.admin.save()
        self.neighbourhood = Neighbourhoods(user=self.user,admin=self.admin,name='ruiru',location='nyairofi')
    
    def test_instance(self):
        self.assertTrue(isinstance( self.neighbourhood,Neighbourhoods))

    def test_data(self):
        self.assertTrue(self.neighbourhood.name,"ruiru")

    def test_save(self):
        self.neighbourhood.save()
        neighbourhood = Neighbourhoods.objects.all()
        self.assertTrue(len(neighbourhood)>0)

    def test_delete(self):
        neighbourhood = Neighbourhoods.objects.filter(id=1)
        neighbourhood.delete()
        neighbourhoods = Neighbourhoods.objects.all()
        self.assertTrue(len(neighbourhoods)==0)

    def test_change_neighbourhood(self):
        self.neighbourhood.save()
        self.update_neighbourhood = Neighbourhoods.objects.filter(name='ruiru').update(name = 'aab')
        self.updated_post = Neighbourhoods.objects.get(name='aab')
        self.assertTrue(self.updated_post.name,'aab')

class postsTest(TestCase):
    def setUp(self):
        self.user=User(username='dk',first_name='d',last_name='k',email='dk@gmail.com')
        self.user.save()
        self.admin=User(username='kd',first_name='d',last_name='k',email='dk@gmail.com')
        self.admin.save()
        self.new_profile=Profile(user=self.user,bio='wueh')
        self.new_profile.save()
        self.neighbourhood = Neighbourhoods(user=self.user,admin=self.admin,name='ruiru',location='nyairofi')
        self.neighbourhood.save()
        self.new_post = Message(user=self.user,message="eating",neighbourhood=self.neighbourhood)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,Message))
    
    def test_data(self):
        self.assertTrue(self.new_post.message,"eating")
        
    def test_save(self):
        self.new_post.save()
        posts = Message.objects.all()
        self.assertTrue(len(posts)>0)
    
    def test_delete(self):
        post = Message.objects.filter(id=1)
        post.delete()
        posts = Message.objects.all()
        self.assertTrue(len(posts)==0)

    def test_update_post(self):
        self.new_post.save()
        self.update_post = Message.objects.filter(message='eating').update(message = 'aaabbbcccddd')
        self.updated_post = Message.objects.get(message='aaabbbcccddd')
        self.assertTrue(self.updated_post.message,'aaabbbcccddd')



class CommentTest(TestCase):
    def setUp(self):
        self.new_user=User(username='aa',first_name='a',last_name='a',email='a@gmail.com')
        self.new_user.save()
        self.admin=User(username='kd',first_name='d',last_name='k',email='dk@gmail.com')
        self.admin.save()
        self.neighbourhood = Neighbourhoods(user=self.new_user,admin=self.admin,name='ruiru',location='nyairofi')
        self.neighbourhood.save()
        self.new_post = Message(user=self.new_user,message="eating",neighbourhood=self.neighbourhood)
        self.new_post.save()
        self.comment=Comments(user=self.new_user,message=self.new_post,comment='good')

    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Comments))

    def test_data(self):
        self.assertTrue(self.comment.comment,"good")

    def test_comments(self):
        self.comment.save()
        comments=Comments.objects.all()
        self.assertTrue(len(comments)>0)

        



    