# Create your views here.
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, reverse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.parsers import JSONParser
from .models import User
from .models import FreemiumUser
from .serializers import UserSerializer
from django.db.models.query_utils import Q
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.csrf import csrf_exempt 


@csrf_exempt
@api_view(['POST'])
def register(request):
	user_data = JSONParser().parse(request)
	print(user_data)
	user_serializer = UserSerializer(data=user_data)
	if user_serializer.is_valid():
		user = User.objects.create(user_name = user_data['user_name'],first_name = user_data['first_name'],last_name = user_data['last_name'],email = user_data['email'],password = make_password(user_data['password']),phone_number = user_data['phone_number'],dob = user_data['dob'],last_login = datetime.now())
		user.save()
		send_mail(subject='Food Court Registration',message='Thank you for Registering',from_email=settings.EMAIL_HOST_USER,recipient_list=[user_data['email']])
		return HttpResponse("success",status=status.HTTP_201_CREATED)
	return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""	 
def id_generator(size=11, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

@csrf_exempt
@api_view(['GET'])
def forgotPassword(request):
		email = request.query_params.get('email')
		try:
			pass_code = id_generator()
			print("pass", pass_code)
			User.objects.filter(email=email).update(forget_pass_code=pass_code)
		except User.DoesNotExist:
			return HttpResponse("user not registered",status=status.HTTP_404_NOT_FOUND)
		subject = 'Food Court Change Password'
		html_message="<h1>Forgot your password?</h1><p>Please use the code "+pass_code+" to reset your password.</p>"
		from_email = settings.EMAIL_HOST_USER
		to = email
		send_mail(subject=subject, message='content', from_email = from_email , recipient_list=[to], html_message=html_message)
		return HttpResponse("success",status=status.HTTP_201_CREATED)


@csrf_exempt
@api_view(['POST'])
def changePassword(request):
		user_data = JSONParser().parse(request)
		try:
			user_pass = User.objects.filter(email=user_data['email']).first().forget_pass_code
			if(user_pass != user_data['pass_code'] or user_pass == ''):
				return HttpResponse("Link not valid",status=status.HTTP_404_NOT_FOUND)
			User.objects.filter(email=user_data['email']).update(password=make_password(user_data['password']), forget_pass_code='')
			return HttpResponse("password changed",status=status.HTTP_201_CREATED)
		except User.DoesNotExist:
			return HttpResponse("user not registered",status=status.HTTP_404_NOT_FOUND)

"""

@csrf_exempt
@api_view(['POST'])
def login(request):
	data = JSONParser().parse(request)
	try:
		user = User.objects.filter(email= data['email']).first()
		print(user)
		if(check_password(data['password'], user.password)):
			user.last_login = datetime.now()
			user.save()
			return HttpResponse('login success',status=200)
		else:
			return HttpResponse('login failure',status=401)
	except User.DoesNotExist:
		return HttpResponse("user not registered",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
@api_view(['POST'])
def password_reset_request(request):
	data = JSONParser().parse(request)
	email = data['email']
	allusers = User.objects.filter(Q(email=email))
	if allusers.exists():
		for user in allusers:
			email = user.email
			subject = 'Password Reset Requested'
			email_template_name = 'registration/password_reset_email.txt'
			c = {
			'email': email,
			'domain':'127.0.0.1:8000',
			'site_name': 'The Food Court',
			'uid': urlsafe_base64_encode(force_bytes(user.user_id)),
			'token': default_token_generator.make_token(user),
			'protocol': 'http',
			}
			emailstr = render_to_string(email_template_name, c)
			try:
				send_mail(subject, emailstr, settings.EMAIL_HOST_USER , [email], fail_silently=False)
			except BadHeaderError:
				return HttpResponse('Invalid header found.', status=400)
		return HttpResponse(status=200)

"""

@csrf_exempt
@api_view(['POST'])
def fetchPostsForSavedList(request):
		per_request = 30
		data = JSONParser().parse(request)
		email = data['email']
		try:
			user = User.objects.filter(email= data['email']).first()
		except User.DoesNotExist:
			return HttpResponse("user not registered",status=status.HTTP_404_NOT_FOUND)
		count = int(data['count']) * 30; 
		posts = Post.objects.filter(user_id = user).order_by('post_time')[count : count + per_request]
		scroll_serializer = ScrollDataSerializer(posts, many=True) 
		return HttpResponse(json.dumps(scroll_serializer.data), content_type="application/json")





@csrf_exempt
@api_view(['POST'])
def fetchPostsForRegularUser(request):
		per_request = 30
		data = JSONParser().parse(request)
		email = data['email']
		try:
			user = User.objects.filter(email= data['email']).first()
		except User.DoesNotExist:
			return HttpResponse("user not registered",status=status.HTTP_404_NOT_FOUND)
		count = int(data['count']) * 30; 
		posts = Post.objects.filter(user_id = user).order_by('post_time')[count : count + per_request]
		swipe_serializer = SwipeDataSerializer(posts, many=True) 
		return HttpResponse(json.dumps(swipe_serializer.data), content_type="application/json")




@csrf_exempt
@api_view(['POST'])
def RegisterAndFetchPostsForFreemiumUser(request):
	quota = 15
	data = JSONParser().parse(request)
	user=''
	try:
		user = FreemiumUser.objects.get(device_id = data['device_id'])
		print("user is there already", user.device_id)
	except:
		user = FreemiumUser.objects.create(device_id = data['device_id'])
		print("no user", user.device_id)
	print("user out ", user.device_id)
	if(user.quota_done == True):
		return HttpResponse("Your quota has finished, Please register to see more posts",status = status.HTTP_400_BAD_REQUEST)
	else:
		user.quota_done=True
		user.save()
		posts = Post.objects.all().order_by('post_time')[:quota]
		swipe_serializer = SwipeDataSerializer(posts, many=True) 
		return HttpResponse(json.dumps(swipe_serializer.data), content_type="application/json")


"""

