from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import STUDENT,PHONE,COURSE

# Create your views here.


def home(request):
        stu_data=STUDENT.objects.all()
        return render(request, 'home.html', {'stu_data':stu_data})

def insert_data(request):
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        qualification=request.POST['qualification']
        email_id=request.POST['email_id']
        duration=request.POST['duration']
        joining_date=request.POST['joining_date']
        paid_amount=request.POST['paid_amount']
        balance_amount=request.POST['balance_amount']
        data=STUDENT(
            name=name,
            age=age,
            qualification=qualification,
            mail_id=email_id,
            duration=duration,
            joining_date=joining_date,
            paid_amount=paid_amount,
            balance_amount=balance_amount

        )
        data.save()
        return render(request,'insert_form.html')

    return render(request,'insert_form.html')


def delete_view(request,id):
    data=STUDENT.objects.get(id=id)
    data.delete()
    return redirect('home_view')


def update_view(request,id):
    data = STUDENT.objects.get(id=id)
    if request.method=='POST':
        # data=STUDENT.objects.get(id=id)
        data.name=request.POST['name']
        data.age=request.POST['age']
        data.qualification=request.POST['qualification']
        data.mail_id=request.POST['email_id']
        data.duration=request.POST['duration']
        data.joining_date=request.POST['joining_date']
        data.paid_amount=request.POST['paid_amount']
        data.balance_amount=request.POST['balance_amount']
        data.save()
        return redirect('home_view')
    return render(request,'update_form.html',{'stu_data':data})


def add_phonr(request,id):
    if request.method=='POST':
        stu = STUDENT.objects.get(id=id)
        phone=PHONE(ph_number=request.POST['ph_number'],ph=stu)
        phone.save()
        p_id = stu.phone_set.all()
        return render(request,'add_phone.html',{'add_phone':stu,'mobile_number':p_id})
    else:
        stu=STUDENT.objects.get(id=id)
        p_id=stu.phone_set.all()
        return render(request, 'add_phone.html',{'add_phone':stu,'mobile_number':p_id})


def update_phone_view(request,id):
    if request.method=='POST':
        phone=PHONE.objects.get(id=id)
        phone.ph_number=request.POST['ph_number']
        phone.save()
        return redirect('home_view')
    else:
        phone=PHONE.objects.get(id=id)
        return render(request,'update_phone_number.html',{'mobile_number':phone})


def del_ph_num(request,id):
    phone=PHONE.objects.get(id=id)
    phone.delete()
    return redirect('home_view')


def Add_course(request):
    if request.method=='POST':
        course=request.POST['course_name']
        data=COURSE(course=course)
        data.save()
        dis_course=COURSE.objects.all()
        return render(request,'add_course.html',{'course_list':dis_course})
    else:
        dis_course = COURSE.objects.all()
        return render(request,'add_course.html',{'course_list':dis_course})


def user_course_view(request,id):
    if request.method=='GET':
        stu = STUDENT.objects.get(id=id)
        # cor=COURSE.objects.get(id=request.POST['user_course'])
        #
        # cor.number.add(stu)
        # cor.save()
        stu_course=stu.course_set.all()
        course_list = COURSE.objects.all()
        return render(request, 'user_course.html', {'student': stu, 'course_list': course_list,'user_course':stu_course})
    else:
        stu=STUDENT.objects.get(id=id)
        print('course id =',request.POST['course'])
        cor=COURSE.objects.get(id=request.POST['course'])
        cor.number.add(stu)
        cor.save()
        course_list=COURSE.objects.all()
        stu_course = stu.course_set.all()
        return render(request,'user_course.html',{'student':stu,'course_list':course_list,'user_course':stu_course})


def display_courses(request):
    if request.method=='GET':
        cou_lst = COURSE.objects.all()
        return render(request, 'display_courses.html', {'courses': cou_lst})
    else:
        cou=COURSE.objects.get(id=request.POST['course'])
        print('course_id =',cou)
        stu_list=cou.number.all()
        print('course_id =', stu_list)
        cou_lst = COURSE.objects.all()
        return render(request, 'display_courses.html', {'courses': cou_lst,'student_list':stu_list})


def delete_student_course(request,user_id,course_id):
    print('course_id =',course_id)
    cou=COURSE.objects.get(id=course_id)
    stu=STUDENT.objects.get(id=user_id)
    stu.course_set.remove(cou)
    return redirect('user_course',user_id)