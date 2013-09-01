from django.template import RequestContext
from django.shortcuts import render_to_response
import vkontakte
from settings import APP_ID, APP2_ID, APP2_KEY, APP2_TOKEN, USER1_ID, USER2_ID

vk = vkontakte.API(APP_ID, token=APP2_TOKEN, timeout=5)

def home(request):
  app_id = APP2_ID  
  settings = "friends"
  my_friends = set(vk.friends.get(uid=USER1_ID))
  my_requests = set(vk.friends.getRequests(uid=USER1_ID, out=1))
  sempo_friends = set(vk.friends.get(uid=USER2_ID))
  missing_friends = sempo_friends - (my_friends | my_requests)
  print "Friends: %d" % len(my_friends)
  print "Requests: %d" % len(my_requests)
  print "Sempo friends: %d" % len(sempo_friends)
  print "Common: %d" % len(missing_friends)

  context = {
    'app_id': app_id,
    'settings': settings,
    'friends': missing_friends,
  }

  return render_to_response(
    "index.html",
    context,
    context_instance = RequestContext(request))