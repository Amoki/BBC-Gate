import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.db.models import Q
from gate.models import Code, Rfid
import utils.door as door


def index(request):
    return render(request, "index.html", {"domain": request.get_host()})


@csrf_exempt
def open(request):
    if request.method != "POST":
        return HttpResponse("method not allowed", status=405)
    if request.META.get("CONTENT_TYPE") == "application/json":
        json_data = json.loads(request.body.decode("utf-8"))
        try:
            code = json_data["code"]
        except KeyError:
            return HttpResponse('Missing key "code"', status=400)
    else:
        code = request.POST.get("code")
    try:
        Code.objects.get(
            Q(expires_at__lte=timezone.now()) | Q(expires_at__isnull=True), code=code
        )
    except Code.DoesNotExist:
        return HttpResponse("Unauthorized", status=401)
    door.open()
    return HttpResponse("OK", status=200)


@csrf_exempt
def rfid(request):
    if request.method != "POST":
        return HttpResponse("method not allowed", status=405)
    try:
        json_data = json.loads(request.body.decode("utf-8"))
    except BaseException:
        return HttpResponse("body must be a json", status=400)

    try:
        rfid_id = json_data["rfid_id"]
    except KeyError:
        return HttpResponse('Missing key "rfid_id"', status=400)
    try:
        Rfid.objects.get(rfid_id=rfid_id)
    except Rfid.DoesNotExist:
        return HttpResponse("Unauthorized", status=401)
    door.open()
    return HttpResponse("OK", status=200)
