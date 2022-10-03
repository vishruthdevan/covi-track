from users.models import UserProfile
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
import random

def run():
    for i in range(100):
        username = 'user' + str(i)
        email = username + '@bruh.com'
        user = User.objects.create_user(username, email, 'helloVD@234')
        user.save()
        up = UserProfile.objects.get(user=user)
        up.covidaffected = random.choice(['T', 'F', 'R'])
        up.vaccinated = random.choice(['0','1','2'])
        up.contact_number = '6969696969'
        up.email = 'sixmorenines@gmail.com'
        up.address = '50 C Woodlands Cottage'
        up.town = 'Nowhere'
        up.state = 'Nowhere again'
        up.post_code = '420420'
        up.country = 'India'
        up.latitude = round(random.uniform(8, 32), 6)
        up.longitude = round(random.uniform(72, 88), 6)
        up.save()
        print(i)