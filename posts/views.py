from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


posts = [
    {
        "id": 1,
        "title": "Let's explore Python",
        "content": "Python is an interpreted, high-level programming language, widely used in machine learning and one of the top three coding languages."
    },
    {
        "id": 2,
        "title": "Web Development with Django",
        "content": "Django is a powerful web framework that makes it easy to build secure and scalable applications using Python."
    },
    {
        "id": 3,
        "title": "Understanding APIs",
        "content": "APIs allow applications to communicate with each other efficiently, enabling data exchange and integrations across different platforms."
    },
    {
        "id": 4,
        "title": "Database Management with PostgreSQL",
        "content": "PostgreSQL is a highly efficient, open-source relational database system known for its advanced features and reliability."
    },
]


# Create your views here.



def home(request):
   # print(reverse('home', args = ['zach']))
    html = ""
    for post in posts:
        html += f'''
<div>
<a href = "/post/{post['id']}/">
<h1>{post['id']} - {post['title']}</h1></a>
<p>{post['content']}</p>
</div>

'''
    return render(request, 'posts/home.html', {'posts': posts, 'username': 'zachary'})

def post(request, id):
    valid_id = False
    for post in posts:
        if post['id']==id:
            post_dict = post
            valid_id = True
            break

    if valid_id:
       
        return render(request, "posts/post.html", {'post_dict':post_dict})

    else: 
        return HttpResponseNotFound("Not Available :(")


def google(request, id):
    url = reverse("post", args= [id])

    return HttpResponseRedirect(url)

