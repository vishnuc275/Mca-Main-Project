from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login as auth_login
from django.urls import path
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from getin.models import Userreg, Login, Fb, Images, Staffreg
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse



def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')

def reg(request):
    if request.method == 'POST':

        Role = request.POST.get('Role')
        Exp = request.POST.get('Exp')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        housename = request.POST.get('housename')
        street = request.POST.get('street')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        zip = request.POST.get('zip')
        district = request.POST.get('district')


        savecard = Userreg()
        savecard.Role = request.POST.get('Role')
        savecard.Exp = request.POST.get('Exp')
        savecard.firstname = request.POST.get('firstname')
        savecard.lastname = request.POST.get('lastname')
        savecard.housename = request.POST.get('housename')
        savecard.phone = request.POST.get('phone')
        savecard.district = request.POST.get('district')
        savecard.street = request.POST.get('street')
        savecard.zip = request.POST.get('zip')
        savecard.email = request.POST.get('email')
        if Userreg.objects.filter(email=email).exists():
            return HttpResponse("<script>alert('user already exists');window.location='/reg';</script>")
            return redirect('getin:reg')
        else:
            savecard.save()

        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        Role = request.POST.get('Role')
        status = request.POST.get('status')
        login = Login()
        login.email = request.POST.get('email')
        login.password1 = request.POST.get('password1')
        login.status = 'approved'
        login.Role = request.POST.get('Role')
        login.save()

        return HttpResponse("<script>alert('registered succesfully');window.location='/login';</script>")
        return render(request, 'login.html')
    else:
        return render(request,'reg.html')


def login1(request):
    if request.method == 'POST':
        try:

            userdetail = Login.objects.get(email=request.POST['email'], password1=request.POST['password1'])
            request.session['email'] = userdetail.email
            if userdetail.Role == 'Photographer':
                return render(request, "photohome.html")
            if userdetail.Role == 'staff' :
                    if userdetail.status == 'pending':
                        return HttpResponse("<script>alert('request pending');window.location='/login';</script>")
                    else:
                        return render(request, "snakehome.html")
            if userdetail.Role == 'User':
                return render(request, "userhome.html")
            if userdetail.Role == 'admin':
                return render(request, "adminhome.html")
        except ObjectDoesNotExist:
            return HttpResponse("<script>alert('invalid credentials');window.location='/login';</script>")
    return render(request, 'login.html')

def staffreg(request):
    if request.method == 'POST':
        license = request.FILES.get('license')
        Exp = request.POST.get('Exp')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        dob = request.POST.get('dob')
        housename = request.POST.get('housename')
        street = request.POST.get('street')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        zip = request.POST.get('zip')
        district = request.POST.get('district')

        staff = Staffreg(license=license, Exp=Exp, firstname=firstname, lastname=lastname, dob=dob, housename=housename, phone=phone, district=district, street=street, zip=zip, email=email)

        if Staffreg.objects.filter(email=email).exists():
            return HttpResponse("<script>alert('user already exists');window.location='/staffreg';</script>")
            return redirect('getin:staffreg')
        else:
            staff.save()

            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            login = Login()
            login.email = request.POST.get('email')
            login.password1 = request.POST.get('password1')
            login.status = 'pending'
            login.Role = 'staff'
            login.save()


            return HttpResponse("<script>alert('staff registered succesfully');window.location='/login';</script>")
    return render(request, 'staffreg.html')



def logout(request):
    try:
      del request.session['email']
    except:
        return render(request, 'login.html')
    return render(request, 'login.html')



def userhome(request):
    return render(request, 'userhome.html')


def photohome(request):
    return render(request, 'photohome.html')

#--------------------------------photographer---------------------------------------------------------------------------------------#

def photoprofile(request):
        cm = request.session['email']
        profilesuser = Userreg.objects.all()
        profilesuser = Userreg.objects.filter(email=cm)

        if request.method == 'POST':
            firstname = request.POST.get('firstname')
            secondname = request.POST.get('secondname')
            address = request.POST.get('address')
            pincode = request.POST.get('pincode')
            phone = request.POST.get('phone')
            email = request.POST.get('email')

            savecardupdate = Userreg()

            savecardupdate.firstname = request.POST.get('firstname')
            savecardupdate.lastname = request.POST.get('lastname')
            savecardupdate.address = request.POST.get('address')
            savecardupdate.phone = request.POST.get('phone')
            savecardupdate.pincode = request.POST.get('pincode')
            savecardupdate.email = request.POST.get('email')
            Userreg.objects.filter(email=cm).update(firstname=firstname, lastname=lastname, address=address,
                                                    pincode=pincode, phone=phone, email=email)

            return redirect('photographer:photoprofile')

        return render(request, 'photographer/photoprofile.html', {'profiles': photoprofile})

def photofb(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        type = request.POST.get('type')
        feedback = request.POST.get('feedback')

        fbcard = Fb()
        fbcard.name = request.POST.get('name')
        fbcard.email = request.POST.get('email')
        fbcard.type = request.POST.get('type')
        fbcard.feedback = request.POST.get('feedback')
        fbcard.save()
        return HttpResponse("<script>alert('feedback sended');window.location='/photofb';</script>")
    return render(request, 'photographer/photofb.html')

def photopayment(request):
    return render(request, 'user/photopayment.html')

def photoadd(request):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = request.POST.get('amount')
        image = request.FILES.get('image')
        data = Images(name=name,amount=amount,image=image)
        data.save()
        return HttpResponse("<script>alert('image uploaded');window.location='/photoadd';</script>")
    return render(request, 'photographer/photoadd.html')


#--------------------------------user---------------------------------------------------------------------------------------

def caseregister(request):
    return render(request, 'user/caseregister.html')

def userfb(request):
    return render(request, 'user/userfb.html')

def wildgallery(request):
    cursor = connection.cursor()
    cursor.execute("select * from image")
    pin = cursor.fetchall()
    return render(request,"User/wildgallery.html",{'data':pin})


#--------------------------------admin---------------------------------------------------------------------------------------


def adminhome(request):
    return render(request, 'adminhome.html')

def staffreq(request):
    cursor = connection.cursor()
    cursor.execute("select * from staffreg where status='pending' ")
    pin = cursor.fetchall()
    return render(request, "admin/staffreq.html", {'data': pin})

def approvestaffreq(request,email):
    cursor = connection.cursor()
    cursor.execute("update login set status='Approved' where email='" + str(email) + "'")
    cursor.execute("update staffreg set status='Approved' where email='" + str(email) + "'")
    return redirect("/staffreq")

def staff(request):
    cursor = connection.cursor()
    cursor.execute("select * from staffreg")
    pin = cursor.fetchall()
    return render(request, 'admin/staff.html', {'data': pin})

def deletestaff(request,email):
    cursor = connection.cursor()
    cursor.execute("delete from login where email='"+str(email)+"')")
    cursor.execute("delete from staffreg where email='"+str(email)+"')")
    return redirect("/staff")

def blockstaff(request,email):
    cursor = connection.cursor()
    cursor.execute("update login set status='blocked' where email='" + str(email) + "'")
    cursor.execute("update staffreg set status='blocked' where email='" + str(email) + "'")
    return redirect("/staff")

def approvestaff(request,email):
    cursor = connection.cursor()
    cursor.execute("update login set status='Approved' where email='" + str(email) + "'")
    cursor.execute("update staffreg set status='Approved' where email='" + str(email) + "'")
    return redirect("/staff")

def viewfeedback(request):
    cursor = connection.cursor()
    cursor.execute("select * from fb")
    pin = cursor.fetchall()
    return render(request, 'admin/viewfeedback.html', {'data': pin})


#--------------------------------staff---------------------------------------------------------------------------------------

def snakehome(request):
    return render(request, 'snakehome.html')

