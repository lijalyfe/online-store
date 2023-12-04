from django.shortcuts import render

def home(request):
    return render(request, 'catalog/home.html')

def contact(request):
    # Обработка сбора обратной связи (дополнительное задание)
    if request.method == 'POST':
        # Обработка данных формы обратной связи
        pass

    return render(request, 'catalog/contact.html')
