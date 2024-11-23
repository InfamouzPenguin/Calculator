from django.shortcuts import render
from django.http import JsonResponse
from .forms import CalculatorForm

def calculator_view(request):
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            number1 = form.cleaned_data['number1']
            number2 = form.cleaned_data['number2']
            operation = form.cleaned_data['operation']
            error = None
            result = None

            try:
                if operation == 'add':
                    result = number1 + number2
                elif operation == 'subtract':
                    result = number1 - number2
                elif operation == 'multiply':
                    result = number1 * number2
                elif operation == 'divide':
                    if number2 != 0:
                        result = number1 / number2
                    else:
                        error = "Cannot divide by zero."
                elif operation == 'exponent':
                    result = number1 ** number2
                elif operation == 'modulus':
                    result = number1 % number2
                else:
                    error = "Invalid operation."
            except Exception as e:
                error = str(e)

            # Manage calculation history
            history = request.session.get('history', [])
            if result is not None:
                history.append(f"{number1} {operation} {number2} = {result}")
            elif error:
                history.append(f"Error: {error}")
            request.session['history'] = history[-5:]  # Keep last 5 entries

            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                if error:
                    return JsonResponse({'error': error})
                else:
                    return JsonResponse({'result': result})
            else:
                context = {
                    'form': form,
                    'result': result,
                    'error': error,
                    'history': request.session.get('history', []),
                }
                return render(request, 'calculator.html', context)
        else:
            error = 'Invalid input. Please enter numeric values.'
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'error': error})
            else:
                context = {
                    'form': form,
                    'error': error,
                    'history': request.session.get('history', []),
                }
                return render(request, 'calculator.html', context)
    else:
        form = CalculatorForm()
        context = {
            'form': form,
            'history': request.session.get('history', []),
        }
        return render(request, 'calculator.html', context)
