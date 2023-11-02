from django.shortcuts import render
from django.http import HttpResponse

def indexPageView(request):
    return render(request, 'pages/index.html')

def accountPageView(request, kidName):
    meter_value = request.session.get('meter_value', 0)
    goal_amount = request.session.get('goal_amount', 0)
    not_enough_cash = False

    if request.method == 'POST':
        if 'add_ten_dollar' in request.POST:
            # Add 10 dollar to the meter value
            meter_value += 10
        elif 'add_five_dollar' in request.POST:
            # Add 5 dollar to the meter value
            meter_value += 5
        elif 'add_dollar' in request.POST:
            # Add 1 dollar to the meter value
            meter_value += 1
        elif 'add_quarter' in request.POST:
            # Add 0.25 dollars (25 cents) to the meter value
            meter_value += 0.25
        elif 'subtract_ten_dollar' in request.POST:
            if meter_value >= 10:
                meter_value -= 10
            else:
                not_enough_cash = True  # Set the flag if not enough cash
        elif 'subtract_five_dollar' in request.POST:
            if meter_value >= 5:
                meter_value -= 5
            else:
                not_enough_cash = True  # Set the flag if not enough cash
        elif 'subtract_dollar' in request.POST:
            if meter_value >= 1:
                meter_value -= 1
            else:
                not_enough_cash = True  # Set the flag if not enough cash
        elif 'subtract_quarter' in request.POST:
            if meter_value >= 0.25:
                meter_value -= 0.25
            else:
                not_enough_cash = True  # Set the flag if not enough cash
        elif 'reset_meter' in request.POST:
            # Reset the meter value to 0
            meter_value = 0

        # Update the session data
        request.session['meter_value'] = meter_value

        new_goal_amount = request.POST.get('goal_amount')
        if new_goal_amount:
            goal_amount = float(new_goal_amount)
            request.session['goal_amount'] = goal_amount

    # Calculate the progress bar percentage
    if goal_amount > 0:
        progress_percentage = (meter_value / goal_amount) * 100
    else:
        progress_percentage = 0

    formatted_percentage = "{:.2f}".format(progress_percentage)

    context = {
        'kidName':kidName,
        'meter_value':meter_value,
        'goal_amount':goal_amount,
        'progress_percentage':formatted_percentage,
        'not_enough_cash':not_enough_cash
    }

    return render(request, 'pages/account.html', context)