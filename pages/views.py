from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render
from joblib import load

model = load("./savedModels/model.joblib")


class HomeView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy("login")
    redirect_field_name = "next"
    template_name = "home.html"


def classifier(request):
    if request.method == 'POST':
        try:
            # Convert input data to float
            sepal_length = float(request.POST.get('sepal_length'))
            sepal_width = float(request.POST.get('sepal_width'))
            petal_length = float(request.POST.get('petal_length'))
            petal_width = float(request.POST.get('petal_width'))

            # Make prediction
            prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
            predicted_class = prediction[0]

            # Map predicted class to target name
            target_names = ['Setosa', 'Versicolor', 'Virginica']
            predicted_class_name = target_names[predicted_class]

            return render(request, 'result.html', {'predicted_class': predicted_class_name})
        except Exception as e:
            # Handle errors
            return render(request, 'error.html', {'error_message': str(e)})
    else:
        # Handle GET requests
        return render(request, 'error.html', {'error_message': 'Method not allowed'})
