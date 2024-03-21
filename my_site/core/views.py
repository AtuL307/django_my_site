from datetime import date
from django.shortcuts import render

# Create your views here.
all_posts = [
    {
        'slug': 'hike-in-the-mountains',
        'image': 'mountain.jpg',
        'author': 'Maximilian',
        'date': date(2021, 7, 21),
        'title': 'Mountain Hiking',
        'excerpt': "There's nothing like the views you get when hiking in the mountains! \
                    And I wasn't even prepared for what happen whilst I was enjoying the view!",
        'contain': """Lorem ipsum dolor sit amet, consectetur adipisicing elit, 
                    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
                    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in 
                    voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
                    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui 
                    officia deserunt mollit anim id est laborum.
                    
                    Ea natus officiis soluta adipisci vel? Temporibus mollitia 
                    similique deserunt, molestiae iste incidunt eum, quae 
                    voluptas accusamus iure ullam cum non nemo quos est, 
                    aliquid laudantium labore illum sed pariatur quod, excepturi 
                    nulla tenetur veritatis nemo id cumque? Quam sapiente reprehenderit
                    ex?
                    
                    """,
    },
    {
        'slug': 'into-the-woods',
        'image': 'forest.jpeg',
        'author': 'Maximilian',
        'date': date(2024, 7, 6),
        'title': 'Nature At Its Best',
        'excerpt': "There's nothing like the views you get when hiking in the mountains! \
                    And I wasn't even prepared for what happen whilst I was enjoying the view!",
        'contain': """Lorem ipsum dolor sit amet, consectetur adipisicing elit, 
                    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
                    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in 
                    voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
                    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui 
                    officia deserunt mollit anim id est laborum.
                    
                    Ea natus officiis soluta adipisci vel? Temporibus mollitia 
                    similique deserunt, molestiae iste incidunt eum, quae 
                    voluptas accusamus iure ullam cum non nemo quos est, 
                    aliquid laudantium labore illum sed pariatur quod, excepturi 
                    nulla tenetur veritatis nemo id cumque? Quam sapiente reprehenderit
                    ex?
                    
                    """,
    },
    {
        'slug': 'programing-is-fun',
        'image': 'coding.png',
        'author': 'Maximilian',
        'date': date(2020, 5, 6),
        'title': 'I love coding',
        'excerpt': "There's nothing like the views you get when hiking in the mountains! \
                    And I wasn't even prepared for what happen whilst I was enjoying the view!",
        'contain': """Lorem ipsum dolor sit amet, consectetur adipisicing elit, 
                    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
                    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in 
                    voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
                    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui 
                    officia deserunt mollit anim id est laborum.
                    
                    Ea natus officiis soluta adipisci vel? Temporibus mollitia 
                    similique deserunt, molestiae iste incidunt eum, quae 
                    voluptas accusamus iure ullam cum non nemo quos est, 
                    aliquid laudantium labore illum sed pariatur quod, excepturi 
                    nulla tenetur veritatis nemo id cumque? Quam sapiente reprehenderit
                    ex?
                    
                    """,
    },
]


def get_date(post):
    return post['date']

def index(req):
    sorted_post = sorted(all_posts,key= get_date)
    latest_posts = sorted_post[-3:]
    return render (req, 'core/index.html', {'posts': latest_posts})