from django.shortcuts import render, redirect
import datetime
from django.http import  HttpResponse
from .models import Person
from .process import im_pro , im_pro_side
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view,permission_classes,renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template import loader

@api_view(['GET'],)
@permission_classes([AllowAny],)
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
# Create your views here.

def home(request):
    # return HttpResponse("hello World")
     return render(request,"index.html")
 
def success(request):
    return HttpResponse('successfully uploaded')

def data(request):
            
            # p=Person(name='aaaa',image_after='images/IMG_8597_0WUwqjR.jpg')
            # p.save()
            # img=im_pro('media/images/4.png')
            # p=Person.objects.get(id=41)
            # p.image_after='media/images/'+img
            # p.save()
            data=Person.objects.all().values()
            template = loader.get_template('all-data.html')
            context = {
                'data':data
              }
            return HttpResponse(template.render(context, request))

def api(request):  
    
    if request.method == 'POST':
        # Get the string data from the POST request
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        type = request.POST.get('type')
        level = request.POST.get('level')
        date= datetime.datetime.now() 

        image_before = request.FILES.get('image_before')
       
        p=Person(name=name,image_before=image_before,phone=phone,gender=gender,type=type,level=level,date=date)
        p.save()
        # print(p.image_before)
        # print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        img=''
        if(type == 'Side'):
          img=im_pro_side('media/'+p.image_before.name,level)
        else:
            img=im_pro('media/'+p.image_before.name,level)



        
        # print(img)
        p.image_after=img
        # print('askjdlkasjdlkajslkdjasljdlasjdlajsdljasldj')
        # p.image_after= img
        p.save()


        image_file = request.FILES['image_before']
        username = request.POST['name']
 
        response_data = {
            'image': img,
            'id': p.id
        }

        # Convert the response data to JSON and return it as a response
        return JsonResponse(response_data)
       
    print('sdfsdfsdfsdfsdf')
    
    return JsonResponse({'message':'kljkljllkj'}, status=200)

def csrf_token_view(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrf_token': csrf_token})

def sendMail(request):
    id=request.GET['id']
    email=request.GET['email']
    print(id)
    p=Person.objects.get(id=id)
    p.email=email
    p.save()
    print(p.email)
    print(p.name)

   


    email = EmailMultiAlternatives(
    subject='Resault From Onda',
    body='Hello,'+p.name +' this is resault when come to Onda and use our services',
    from_email='test@tiacenter.com',
    to=[p.email]
    )
    print(p.image_after.path)
    # Get the path to the image file
    image_path = (p.image_after.name)

    # Read the image data from the file system
    with open(image_path, 'rb') as f:
        image_data = f.read()

    # Attach the image to the email message
    email.attach('image.jpg', image_data, 'image/jpeg')

    # Send the email
    email.send()


    res={
        'status':200,
        'data':'True'
    }
    return JsonResponse(res)
