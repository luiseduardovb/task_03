from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
        'my_list': [
            {
            "restaurant_name": "Mais alghanim",
            "food_type": "Lebanese"
            },
            {
            "restaurant_name": "Gia",
            "food_type": "Healthy"
            },
            {
            "restaurant_name": "Joa",
            "food_type": "Japanese"
            },
            ]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
        'my_object': 
            {
            "restaurant_name": "Ebn Amy",
            "food_type": "Shawarma"
            }
            
    }
    return render(request, 'detail.html', context)
