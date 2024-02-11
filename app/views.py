from django.shortcuts import render

# Create your views here.
from app.models import *
def equijoins(request):
    EMPOBJECTS=Emp.objects.select_related('deptno').all()
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=2024)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno=30)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=2023)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dname='ACCOUNTING')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=2022)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__isnull=True)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__isnull=False)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno=10)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(sal__gt=2500)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno=20)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(sal__lt=2500)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__gt=200)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(sal__lt=2050)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dname='RESEARCH')
    d={'EMPOBJECTS':EMPOBJECTS}
    return render(request,'equijoins.html',d)





def selfjoins(request):
    empmgrobjects=Emp.objects.select_related('mgr').all()
    empmgrobjects=Emp.objects.select_related('mgr').filter(deptno__deptno=20)
    empmgrobjects=Emp.objects.select_related('mgr').filter(sal__gt=2500)
    empmgrobjects=Emp.objects.select_related('mgr').filter(comm__gt=100)
    empmgrobjects=Emp.objects.select_related('mgr').all()
    empmgrobjects=Emp.objects.select_related('mgr').filter(deptno__dlocation='NEWYORK')
    empmgrobjects=Emp.objects.select_related('mgr').filter(sal__lt=2500)
    empmgrobjects=Emp.objects.select_related('mgr').filter(deptno__deptno=10)
    empmgrobjects=Emp.objects.select_related('mgr').filter(deptno__deptno=30)
    empmgrobjects=Emp.objects.select_related('mgr').filter(deptno__dname='SALES')
    empmgrobjects=Emp.objects.select_related('mgr').filter(deptno__dname='ACCOUNTING')
    empmgrobjects=Emp.objects.select_related('mgr').all()
    empmgrobjects=Emp.objects.select_related('mgr').filter(deptno__dname='RESEARCH')
    empmgrobjects=Emp.objects.select_related('mgr').filter(comm__lt=0)
    empmgrobjects=Emp.objects.select_related('mgr').filter(sal__lt=3000)
    empmgrobjects=Emp.objects.select_related('mgr').filter(job='MANAGER')
    d={'empmgrobjects':empmgrobjects}
    return render(request,'selfjoins.html',d)


def emp_mgr_dept(request):
    emd=Emp.objects.select_related('deptno','mgr').all()
    emd=Emp.objects.select_related('deptno','mgr').filter()
    d={'emd':emd}
    return render(request,'emp_mgr_dept.html',d)


def emp_salgrade(request):
    #EO=Emp.objects.all()
    #SO=SalGrade.objects.all()
    # Retrieving the data of employess who belongs to grade 4
    #SO=SalGrade.objects.filter(grade=4)#[grade4 SalgradeObjects]

    #EO=Emp.objects.filter(sal__range=(SO[0].losal,SO[0].hisal))
    # Retrieving the data of employess who belongs to grade 3,4
    SO=SalGrade.objects.filter(grade__in=(3,4))

    EO=Emp.objects.none()
    for sgo in SO:
        EO=EO|Emp.objects.filter(sal__range=(sgo.losal,sgo.hisal))
    d={'EO':EO,'SO':SO}
    return render(request,'emp_salgrade.html',d)