from django.shortcuts import render, redirect
from . import forms
import pandas as pd
from . models import Recidivism
import joblib
from sklearn.preprocessing import MinMaxScaler
# Initialize the MinMaxScaler
scaler = MinMaxScaler()



# import sklearn.external.joblib as extjoblib
# model = joblib.load('D:/djangoProjects/djangoProject/Recidivism_web/recidivism/model.joblib')
# scaler = joblib.load('D:/djangoProjects/djangoProject/Recidivism_web/recidivism/scaler2.joblib')

model = joblib.load('../Recidivism_web/recidivism/model.joblib')
scaler = joblib.load('../Recidivism_web/recidivism/scaler2.joblib')

# Create your views here.
def home(request):
    form = None
    if request.method == 'POST':
        print('hello')
        form = forms.Recidivism_form(request.POST)
        print(form.is_valid())
        print()
        if form.is_valid():
            # form.save()
            list(request.POST.values())
          #   df = pd.DataFrame(list(Recidivism.objects.all().order_by('-id').values()[1]))
          #   print('dd',[list(Recidivism.objects.all().order_by('-id').values()[1])])
            X_test_scaled_oversampling = scaler.transform([list(request.POST.values())[1:]])
            pred = model.predict(X_test_scaled_oversampling)
            print(pred)
          #   print(df)
            print('new hello')
            return render(request, 'recidivism/home.html', {'form': form, 'mode': 1, 'value': pred[0]})
    form = forms.Recidivism_form()
    return render(request, 'recidivism/home.html', {'form': form,'mode':0,'value':0})

