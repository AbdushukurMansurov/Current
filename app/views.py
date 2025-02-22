from django.shortcuts import render,redirect
import requests

def index_function(request):
    if request.method == 'POST':
        try:
            # Formadan kelayotgan ma'lumotlarni oling
            amount = float(request.POST.get('amount'))
            from_current = request.POST.get('from')
            base_currency = from_current.split(' - ')[0]  # Masalan, "USD"
            to_current = request.POST.get('to')
            quote_currency = to_current.split(' - ')[0]  # Masalan, "EUR"

            # Open ER API orqali konvertatsiya ma'lumotlarini olish
            url = f"https://open.er-api.com/v6/latest/{base_currency}"
            response = requests.get(url)
            data = response.json()

            if data.get('result') == 'success':
                rates = data.get('rates', {})
                if quote_currency in rates:
                    conversion_rate = rates[quote_currency]
                    result = amount * conversion_rate
                    formatted_result = "{:,.2f}".format(result)
                    output = f"{formatted_result} {quote_currency}"
                else:
                    output = f"Xatolik: {quote_currency} kurslari topilmadi."
            else:
                output = "Xatolik: API chaqirig'i muvaffaqiyatsiz bo'ldi."
        except Exception as e:
            output = f"Xatolik: {e}"

        return render(request, 'index.html', {'output': output})
    else:
        return render(request, 'index.html')
    

def chatgpt(request):
    if request.method == 'POST':
        chat = request.POST.get('chat')

        url = "https://chatgpt-42.p.rapidapi.com/gpt4"

        payload = {
            "messages": [
                {
                    "role": "user",
                    "content": f"{chat}"
                }
            ],
            "web_access": False
        }
        headers = {
            "x-rapidapi-key": "122602994amshd8ba1d1b38eddeep1fe793jsn69ac1be6da9f",
            "x-rapidapi-host": "chatgpt-42.p.rapidapi.com",
            "Content-Type": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers)

        result = response.json()['result']
        return render(request,'chatgpt.html',{'result':result})
    else:
        return render(request,'chatgpt.html')