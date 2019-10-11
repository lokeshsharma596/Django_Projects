from django.shortcuts import render, redirect
# Create your views here.

info=[{
        'name':'Lokesh Sharma',
        'age':'26',
        'work':'python developer'
    },
        {
            'name': 'sandeep',
            'age': '25',
            'work': 'C developer'
        }
    ]



def home(request):
    return render(request,'testapp/home.html')

def about(request):
    content={
        'person':info
    }
    return render(request,'testapp/about.html',content)

