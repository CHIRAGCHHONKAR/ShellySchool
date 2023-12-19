from django.shortcuts import render,redirect
from Classes.models import classes
from Teachers.models import teacher
from django.core.mail import send_mail
from .forms import contactform,commentform,ClassEnquiry
from Contact_Enquiry.models import contact
from Comments_Data.models import comment
from Classes_Enquiry.models import ClassesEnquiry
from django.core.paginator import Paginator
from Events.models import Event

def homepage(request):
    form3 = ClassEnquiry(request.POST)
    classdata=classes.objects.all()
    teacherdata=teacher.objects.all()[:4]
    if request.method=="GET":
        cn=request.GET.get("classname") #(classname) name give to search feild 
        if cn!=None:
            classdata=classes.objects.filter(classtitle__icontains=cn)  #__icontains for search by single alphabhet
            return render(request,"searchclass.html",{'classdata':classdata})  
    data = {
        'form3': form3,
        'classdata':classdata,
        'teacherdata':teacherdata,
    }
    return render(request,"index.html",data)

def aboutpage(request):
    form3 = ClassEnquiry(request.POST)
    data = {
        'form3': form3,
    }
    return render(request,"about.html",data)

def classpage(request):
    classdata=classes.objects.all()
    form3 = ClassEnquiry(request.POST)
    # paginator
    paginator=Paginator(classdata,8)
    page_num=request.GET.get('page')
    page_call=paginator.get_page(page_num)
    totalpage=page_call.paginator.num_pages
    
    data={
        'classdata':page_call,
        'form3': form3,
        'totalpagelist':{n+1 for n in range(totalpage)}
    }
    return render(request,"Class.html",data)

def teacherpage(request):
    teacherdata = teacher.objects.all()
    form3 = ClassEnquiry(request.POST)
    # paginator
    paginator2 = Paginator(teacherdata, 8)
    page_num2 = request.GET.get('page')
    page_call2 = paginator2.get_page(page_num2)
    totalpage2 = paginator2.num_pages
    
    data = {
        'teacherdata': page_call2,
        'form3': form3,
        'totalpagelist2':{t+1 for t in range(totalpage2)}
    }
    return render(request, "teacher.html", data)

def blogpage(request):
    form3 = ClassEnquiry(request.POST)
    data = {
        'form3': form3,
    }
    return render(request,"blog.html",data)

def contactpage(request):
    form = contactform(request.POST)
    form3 = ClassEnquiry(request.POST)
    data={
        'form':form,
        'form3': form3,
    }
    return render(request, "contact.html",data)

def Contact_Data(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        
        #saving data in database
        cd=contact(name=name,email=email,message=message)
        cd.save()
        
        #sending email
        subject="New Contact Enquiry"
        email_content = f"Name: {name}<br>Email: {email}<br>Message:{message}"
        # Set the email addresses
        from_email = 'example@gmail.com'
        recipient_list = ['example@gmail.com']
        send_mail(subject, "", from_email, recipient_list, html_message=email_content)
        
    return render(request,"contactthank.html")    

def eventspage(request):
    eventdata=Event.objects.all()
    form3 = ClassEnquiry(request.POST)
    paginator3=Paginator(eventdata,6)
    page_num3=request.GET.get('page')
    page_call3=paginator3.get_page(page_num3)
    totalpage3=paginator3.num_pages
    data = {
        'eventdata':page_call3,
        'form3': form3,
        'totalpagelist3':{e+1 for e in range(totalpage3) }
    }
    return render(request,"events.html",data)

def eventsinglepage(request):
    form3 = ClassEnquiry(request.POST)
    data = {
        'form3': form3,
    }
    return render(request,"eventsingle.html",data)

def notfoundpage(request):
    return render(request,"404.html")

def classespage(request):
    form3 = ClassEnquiry(request.POST)
    data = {
        'form3': form3,
    }
    return render(request,"classes.html",data)

def singleteacherpage(request):
    form3 = ClassEnquiry(request.POST)
    data = {
        'form3': form3,
    }
    return render(request,"singleteacher.html",data)

def singleblogpage(request):
    form2 = commentform(request.POST)
    form3 = ClassEnquiry(request.POST)
    recent_comment = comment.objects.latest('id')
    data = {
        'form2': form2,
        'form3': form3,
        'recent_comment':recent_comment
    }
    
    return render(request, "singleblog.html", data)

def commentsdata(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        website = request.POST.get('website')
        message = request.POST.get('message')
    
        md = comment(name=name, email=email, website=website, message=message)
        md.save()

    return redirect(singleblogpage)

def contactthank(request):
    return render(request,"contactthank.html")


def classesenquerydata(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        Classes = request.POST.get('Classes')  # This line was changed to use `get` instead of `post`
        message = request.POST.get('message')
        ce = ClassesEnquiry(name=name, email=email, Classes=Classes, message=message)
        ce.save()
        
        # sending email to staff
        subject="New Class Enquery"
        email_content=f"Name: {name}<br>Email: {email}<br>Class: {Classes}<br>Message: {message}"
    
        # set email address
        from_email='example@gmail.com'
        recipient_list=['example@gmail.com']
        # send email
        send_mail(subject,'',from_email,recipient_list,html_message=email_content)
        return render(request, "contactthank.html")
    else:
        return redirect('404.html')
    

    
def searchclass(request):
    form3 = ClassEnquiry(request.POST)
    data = {
        'form3': form3,
    }
    return render(request,"searchclass.html",data)    