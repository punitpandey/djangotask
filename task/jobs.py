from task.models import teacher,schedule
import time
import requests
import json
from time import strftime
from apscheduler.schedulers.background import BackgroundScheduler
from django.core.mail import send_mail
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")

def send_push_notification(target,notification_msg):
    """to send push notification to specific target"""
    header = {
                "Content-Type": "application/json; charset=utf-8",
                "Authorization": "Basic OWIyYWUyZGEtODhiMS00M2EwLWFiNzItZTJkODI0YmRjYjMz"
            }
    payload = {
                "app_id": "e9af5911-ad44-4157-bd6c-6cfabf2374de",
                "include_player_ids": [target],
                "contents": {"en": notification_msg}
            } 
    req = requests.post(
                            "https://onesignal.com/api/v1/notifications",
                            headers=header,
                            data=json.dumps(payload)
                        )
    print(req.status_code, req.reason)

@register_job(scheduler, "interval", seconds=60, replace_existing=True)
def test_job():
    """task to be checked repeatedly in order to fetch teacher's schedule and notify"""
    currTime=str(strftime("%H:%M",time.localtime(time.time()+300)))
    # before class start
    s_query=schedule.objects.all().filter(classFrom__startswith=currTime)
    for schedules in s_query:    
        # data=str("teacher:"+schedules.teacher+" & subject:"+schedules.subject+" & startFrom:"+schedules.classFrom+" & endAt:"+schedules.classTo)
        t_query=teacher.objects.all().filter(id=schedules.teacher_id)
        for teachers in t_query:
            try:
                msg = "Hello Mr. "\
                            +teachers.name\
                            +", Its time for the class of subject "\
                            +schedules.subject\
                            +" from "+str(schedules.classFrom)\
                            +" to "+str(schedules.classTo)+"."
                # send mail
                if teachers.email!="":
                    send_mail("Schedule Alert", msg, "user@gmail.com", 
                                [teachers.email],fail_silently=False)
                else:
                    print("no email provided")
                # send push notification
                if teachers.notify_id!="":
                    send_push_notification(teachers.notify_id,msg)
                else:
                    print("no active system")
            except Exception as e:
                print(str(e))
            data=str(teachers.name+":"+schedules.subject)
            print(currTime," ->",data)
    else:
        print(currTime,": no task")
    # before class end

    s_query=schedule.objects.all().filter(classTo__startswith=currTime)
    for schedules in s_query:    
        # data=str("teacher:"+schedules.teacher+" & subject:"+schedules.subject+" & startFrom:"+schedules.classFrom+" & endAt:"+schedules.classTo)
        t_query=teacher.objects.all().filter(id=schedules.teacher_id)
        for teachers in t_query:
            try:
                msg = "Hello Mr. "\
                            +teachers.name\
                            +", Its time to wrap up class as this class will end on: "\
                            +str(schedules.classTo)+"."
                # send mail
                if teachers.email!="":
                    send_mail("Schedule Alert", msg, "user@gmail.com", 
                                [teachers.email],fail_silently=False)
                else:
                    print("no email provided")
                # send push notification
                if teachers.notify_id!="":
                    send_push_notification(teachers.notify_id,msg)
                else:
                    print("no active system")
            except Exception as e:
                print(str(e))
            data=str(teachers.name+":"+schedules.subject)
            print(currTime," ->",data)
    else:
        print(currTime,": no task")
    


register_events(scheduler)

scheduler.start()
print("Scheduler started!")
