from django.shortcuts import render

def show_main(request):
    context = {
        'candies': [
            {'name': 'Gummy', 'price': '10.000', 'description': 'Tuti fruity chewy candy', 'sweetness': '9/10'},
            {'name': 'Chocolate', 'price': '15.000', 'description': 'Dark chocolate with almond', 'sweetness': '7/10'},
            {'name': 'Lollipop', 'price': '5.000', 'description': 'Sweet and sour candy', 'sweetness': '4/10'}
        ]
    }
    return render(request, "main.html", context)