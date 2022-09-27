from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from brands.models import Brand
from model.models import Model, Series


def model_details(request, id):
    brand = Brand.objects.get(id=id)
    models = Model.objects.filter(brand=brand)
    data = {
        'brand': brand,
        "models": models,
    }
    return render(request, "detail.html", context=data)


def series_detail(request, model_id, brand_id):
    model = Model.objects.get(id=model_id)
    brand = Brand.objects.get(id=brand_id)
    series = Series.objects.filter(model=model)
    data = {
        "model": model,
        "series": series,
        'brand': brand,
    }
    return render(request, "series.html", context=data)


