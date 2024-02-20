from django.shortcuts import render, redirect
import csv
from .models import Employee, ExcelFile
from io import TextIOWrapper

# Create your views here.
from io import TextIOWrapper
import pandas as pd
from django.http import JsonResponse
from django.conf import settings


def export_data_to_excel(request):
    objs = Employee.objects.all()
    data = []
    for obj in objs:
        data.append({"name": obj.name, "age": obj.age})
    pd.DataFrame(data).to_excel("output.xlsx")
    return JsonResponse({"status": 200})


def home(request):
    if request.method == "POST":
        file = request.FILES["file"]
        text_file = TextIOWrapper(
            file,
        )
        data = csv.DictReader(text_file)
        print("dataaaa", data)
        for row in data:
            name = row["name"]
            print("name", name)
        #     age = row["age"]
        #     employee = Employee(name=name, age=age)
        #     employee.save()

    return render(request, "index.html")


def import_data_to_db(request):
    if request.method == "POST":
        file = request.FILES["file"]
        obj = ExcelFile.objects.create(file=file)
        path = file.file
        print(f"{settings.BASE_DIR}/{path}")
        df = pd.read_excel(path)
        for d in df.values:
            print("ggggggggggggggg", d[0])
            name = d[0]
            print(name)
            if not Employee.objects.filter(name=name).exists():
                Employee.objects.create(name=d[0], age=d[1])
            else:
                print("duplicate entry")
    return render(request, "index.html")
