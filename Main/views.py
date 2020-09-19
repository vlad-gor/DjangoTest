from django.shortcuts import render
from django.conf import settings
import redis
from Main import tasks

# Connect to our Redis instance
redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                   port=settings.REDIS_PORT, db=0)

# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")

        redis_instance.set('name', name)
        redis_instance.set('age', age)
        task_type = age
        task = tasks.create_task.delay(int(task_type))

    return render(request, 'index.html')