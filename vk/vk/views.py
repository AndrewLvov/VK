from django.template import RequestContext
from django.shortcuts import render_to_response

APP_ID = "3805230"

def home(request):
  app_id = APP_ID 
  settings = "friends"
  context = {
    'app_id': app_id,
    'settings': settings,
  }
  return render_to_response(
    "index.html",
    context,
    context_instance = RequestContext(request))