from django.shortcuts import render, redirect

from .models import Contact, MlModel
from .utils import predict


def index(request):
    return render(request, 'main.html', )


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        c = Contact.objects.create(name=name, email=email, message=message)
        c.save()
    return redirect('MAIN')


def upload(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            return render(request, 'upload.html')
        if request.method == 'POST':
            user = request.user
            image = request.FILES['filename']
            m = MlModel.objects.create(user=user, image=image)  # get the file
            m.save()
            result: str = predict(m.image.path)
            pre_img = m.image.url.split('.')
            pre_img = pre_img[0] + "__pre." + pre_img[1]
            return render(request, 'upload.html', {'result': result, "uploaded_image": m.image, "pre_img": pre_img})
        # file upload predict result and output
    else:
        return redirect('REGISTER')
