from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
from .myform import EmpForm
from . import models
from django.core.exceptions import ValidationError
# Create your views here.


def add_emp(request):
    if request.method == "GET":
        form = EmpForm()
        return render(request, "add_emp.html", {"form": form})
    else:
        form = EmpForm(request.POST)
        if form.is_valid():  # 进行数据校验
            # 校验成功
            data = form.cleaned_data  # 校验成功的值，会放在cleaned_data里。
            data.pop('r_salary')
            print(data)

            models.Emp.objects.create(**data)
            return HttpResponse(
                'ok'
            )
            # return render(request, "add_emp.html", {"form": form})
        else:
            print(form.errors)    # 打印错误信息
            clean_errors = form.errors.get("__all__")
            print(222, clean_errors)
        return render(request, "add_emp.html", {"form": form, "clean_errors": clean_errors})