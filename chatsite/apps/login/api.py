from django.http import HttpResponse, JsonResponse

from .models import LoginSession, CaptchaSession
from chatsite.models.user import User

import random
import hashlib
import time
import json


def login_api_rand(request):
    if not request.body:
        return HttpResponse("No JSON body")

    data = json.loads(request.body)

    if "data" not in data:
        return HttpResponse("No data in JSON")
    data = data["data"]

    if "user-id" not in data:
        return HttpResponse("user-id value was not included")

    try:
        login = LoginSession.objects.get(user_id=data["user_id"])
        rand = login.rand
    except LoginSession.DoesNotExist:
        try:
            user = User.objects.get(user_id=data["user_id"])
        except User.DoesNotExist:
            return HttpResponse("Invalid user id")

        rand = '%030x' % random.randrange(16**30)
        login = LoginSession(
            user_id=data["user-id"],
            rand=rand,
            valid_resp=hashlib.sha256((user.hash + rand).encode("utf-8")).hexdigest()
        )
        login.save()

    resp = HttpResponse("Initiated login session")
    resp["rand"] = rand
    return resp


def login_api_verify(request):
    if not request.body:
        return HttpResponse("No JSON body")

    data = json.loads(request.body)

    if "data" not in data:
        return HttpResponse("No data in JSON")
    data = data["data"]

    if "user-id" not in data:
        return HttpResponse("user-id value was not included")

    if "result" not in data:
        return HttpResponse("result value was not included")

    try:
        login = LoginSession.objects.get(user_id=data["user-id"])
    except LoginSession.DoesNotExist:
        return HttpResponse("Invalid login session")

    try:
        user = User.objects.get(user_id=data["user-id"])
    except User.DoesNotExist:
        return HttpResponse("Invalid user")

    if login.valid_resp == data["result"]:
        user.verified = True
        user.verification_expiration = time.time() + (data["expiration"] if "expiration" in data else 60 * 60)
        login.delete()
        return HttpResponse("Verified")
    else:
        return HttpResponse("Invalid result")

directory = "chatsite/apps/login/"
SENTENCES = open(directory + "sentences.txt").read().split("\n")
WORDS = open(directory + "words.txt").read().split("\n")


def generate_sentence():
    sentence = random.choice(SENTENCES).split(" ")
    index = random.randint(0, len(sentence) - 1)
    sentence[index] = random.choice(WORDS)
    return " ".join(sentence), index


def captcha_api_init(request):
    if not request.body:
        return HttpResponse("No JSON body")

    data = json.loads(request.body)

    if "data" not in data:
        return HttpResponse("No data in JSON")
    data = data["data"]

    if "reg-id" not in data:
        return HttpResponse("user-id value was not included")

    if len(CaptchaSession.filter(reg_id=data["reg-id"])) != 0:
        return JsonResponse(
            {"sentence": CaptchaSession.get(reg_id=data["reg-id"]).sentence}
        )
    else:
        sentence, index = generate_sentence()
        session = CaptchaSession(
            user_id=data["reg-id"],
            sentence=sentence,
            index=index,
            verified=False
        )
        session.save()
        return JsonResponse({"sentence": sentence})


def captcha_api_verify(request):
    if not request.body:
        return HttpResponse("No JSON body")

    data = json.loads(request.body)

    if "data" not in data:
        return HttpResponse("No data in JSON")
    data = data["data"]

    if "reg-id" not in data:
        return HttpResponse("reg-id value was not included")

    if "result" not in data:
        return HttpResponse("result value was not included")

    try:
        session = CaptchaSession.get(reg_id=data["reg-id"])
    except CaptchaSession.DoesNotExist:
        return HttpResponse("Invalid reg id")

    if data["result"] != session.index:
        return HttpResponse("result was incorrect")

    session.verified = True
    session.save()

    return JsonResponse({"verified": True})


def register_api_id_gen(request):
    return JsonResponse({"id": random.randint(10**9)})


def register_api(request):
    print(request.is_secure())
    if not request.body:
        return HttpResponse("No JSON body")

    data = json.loads(request.body)

    if "data" not in data:
        return HttpResponse("data value is not in JSON")
    data = data["data"]

    if not request.is_secure():
        return HttpResponse("Connection not secure. Use https:// to safely register a password")

    if "reg-id" not in data:
        return HttpResponse("reg-id value was not included")

    if "username" not in data:
        return HttpResponse("username value was not included")

    if "pw-hash" not in data:
        return HttpResponse("pw-hash value was not included")

    try:
        captcha = CaptchaSession.get(reg_id=data["reg-id"])
    except CaptchaSession.DoesNotExist:
        return HttpResponse("Invalid reg-id")

    if not captcha.verified:
        return HttpResponse("Captcha not verified")



