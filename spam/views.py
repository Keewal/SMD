from django.shortcuts import render
from django.http import HttpResponse
import joblib
import os

BASE_DIR = os.path.dirname(__file__)
model1 = joblib.load(os.path.join(BASE_DIR, "myModel1.pkl"))
model2 = joblib.load(os.path.join(BASE_DIR, "mySVCModel.pkl"))

def index(request):
    return render(request, 'index.html')


def checkspam(request):
    if request.method == "POST":
        algo = request.POST.get("algo")
        rawData = request.POST.get("rawData")
        finalAns = ""

        print(f"Selected Algo: {algo}")
        print(f"Input Data: {rawData}")

        # Run prediction based on selected algorithm
        if algo == "algo-1":
            finalAns = model1.predict([rawData])[0]
        elif algo == "algo-2":
            finalAns = model2.predict([rawData])[0]
        else:
            finalAns = "Invalid algorithm selected"

        param = {"answer": finalAns}
        return render(request, 'output.html', param)

    return render(request, 'index.html')