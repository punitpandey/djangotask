from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from task.forms import teacherForm
import json
from task.models import teacher,schedule
# Create your views here.
def index(request):
    return render(request,'task/index.html')

def success(request):
    return render(request,'task/active.html')

@csrf_exempt
def registerNotification(request):
    """to register user for push notification"""
    if request.method=='POST':
        err=False
        errmsg=""
        user=str(request.POST.get('user'))
        notify_id=str(request.POST.get('notify_id'))
        try:
            user_query=teacher.objects.get(name=user)
            user_query.notify_id=notify_id
            user_query.save()
        except Exception as e:
            err=True
            errmsg=str(e)
        context={
            "err":err,
            "errmsg":errmsg,
            "user":user,
            "notify_id":notify_id
        }
        return JsonResponse(context)
        
    else:
        return HttpResponse("Wrong call"+request.method)