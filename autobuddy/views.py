from django.shortcuts import render
from django.db.models import Sum
from .models import RepairCost
from django.http.response import HttpResponseRedirect
# Create your views here.
def index(request):
    return render(request, "home2.html")

def costfinder(request):
    carYear = request.GET.get('carYearsCostFinder')
    print(carYear)
    carMake = request.GET.get('carMakeInput')
    carModel = request.GET.get('carModelInput')
    repair = request.GET.get('repair')

    if isinstance(carYear,str) and isinstance(carMake,str) and isinstance(carModel,str) and isinstance(repair,str):
        cost_sum = RepairCost.objects.filter(car_year=carYear, car_make=carMake, car_model=carModel, repair_name=repair).aggregate(Sum('repair_cost'))['repair_cost__sum']
        cost_num_of_rows = RepairCost.objects.filter(car_year=carYear, car_make=carMake, car_model=carModel, repair_name=repair).count()
        
        average = cost_sum / cost_num_of_rows

        average = '$' + str(average)
        context = {"average_cost" : average}  

    return render(request, "costFinder.html", context)

def isitfair(request):
    carYearFair = request.GET.get('carYearsFairTool')
    carMakeFair = request.GET.get('carMakeFairInput')
    carModelFair = request.GET.get('carModelFairInput')
    repairFair = request.GET.get('repairFairInput')
    quoteFair = request.GET.get('quoteInput')

    if isinstance(carYearFair,str) and isinstance(carMakeFair,str) and isinstance(carModelFair,str) and isinstance(repairFair,str) and isinstance(quoteFair, str):
        cost_sum = RepairCost.objects.filter(car_year=carYearFair, car_make=carMakeFair, car_model=carModelFair, repair_name=repairFair).aggregate(Sum('repair_cost'))['repair_cost__sum']
        cost_num_of_rows = RepairCost.objects.filter(car_year=carYearFair, car_make=carMakeFair, car_model=carModelFair, repair_name=repairFair).count()
        average = cost_sum / cost_num_of_rows

        below_average = (cost_sum / cost_num_of_rows) * .75
        above_average = (cost_sum / cost_num_of_rows) * 1.35
        
        average_str = "${:0.2f}".format(average)
        below_average_str = "${:0.2f}".format(below_average)
        above_average_str = "${:0.2f}".format(above_average)
        
        quoteFair = int(quoteFair)
        
        if (quoteFair <= below_average):
            deal_status = "Very Good"
        elif (below_average < quoteFair <= average):
            deal_status = "Good"
        elif (average < quoteFair <= above_average):
            deal_status = "Okay"
        elif (above_average < quoteFair):
            deal_status = "Bad"
        quoteStr = str(quoteFair)
        context = {"average_cost2" : average_str, "below_average":below_average_str, "above_average":above_average_str, "your_price":quoteStr, "deal_status":deal_status}  

    return render(request, "isitfair.html", context)

def addtoautobuddy(request):
    carYearAdd = request.GET.get('carYearsAddTool')
    carMakeAdd = request.GET.get('carMakeAddInput')
    carModelAdd = request.GET.get('carModelAddInput')
    repairAdd = request.GET.get('repairAddInput')
    price = request.GET.get('priceInput')

    if isinstance(carYearAdd,str) and isinstance(carMakeAdd,str) and isinstance(carModelAdd,str) and isinstance(repairAdd,str) and price != '':
       repair_instance = RepairCost.objects.create(car_year=carYearAdd, car_make=carMakeAdd, car_model=carModelAdd, repair_name=repairAdd, repair_cost=price)

    return render(request, "addtoAutoBuddy.html")