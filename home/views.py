from django.shortcuts import render,HttpResponse
from django.shortcuts import render
from home.forms  import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from home.models import UserScore,Videos

def index(request):
    return render(request,'home/index.html')


@login_required
def special(request):
    
    return HttpResponse("You are logged in!")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
    #return render(request,'home/login.html')
@login_required
def third_page(request):
    attend="False"
    score=0
    video = Videos.objects.get(name="Introduction")
    
        #print "not valid object"
    if request.method == "POST":
        username = request.POST.get('username')
        score = request.POST.get('score')
        attended = request.POST.get('attended')
        try:
            user = UserScore(username=username,score1=score,attended1 = attended)
            s = int(user.totalScore)
            s += int(score)
            user.totalScore = s
            user.save()

        except:
            user = UserScore.objects.get(username=username)
            user.score1=score
            user.attended1=attended
            s = int(user.totalScore)
            s += int(score)
            user.totalScore = s
            user.save()

        attend = user.attended1
    elif request.method == "GET":
        username = request.session['username']
        try:
            user = UserScore.objects.get(username=username)
            attend = user.attended1
            score = user.score1
            print attend
        except:
            print "helo"  
    return render(request,'home/third.html',{'attended':attend,'score':score,'video_url':video.video.url})
def fourth_page(request):
    attend="False"
    score=0
    video = Videos.objects.get(name="Datatypes")
    
        #print "not valid object"
    if request.method == "POST":
        username = request.POST.get('username')
        score = request.POST.get('score')
        attended = request.POST.get('attended')
        try:
            user = UserScore(username=username,score2=score,attended2 = attended)
            s = int(user.totalScore)
            s += int(score)
            user.totalScore = s
            user.save()
        except:
            user = UserScore.objects.get(username=username)
            user.score2=score
            user.attended2=attended
            s = int(user.totalScore)
            s += int(score)
            user.totalScore = s
            user.save()
        attend = user.attended2
    elif request.method == "GET":
        username = request.session['username']
        try:
            user = UserScore.objects.get(username=username)
            attend = user.attended2
            score = user.score2
            print attend
        except:
            print "helo"  
    return render(request,'home/fourth.html',{'attended':attend,'score':score,'video_url':video.video.url})
def fifth_page(request):
    attend="False"
    score=0
    video = Videos.objects.get(name="ControlStructure")
    
        #print "not valid object"
    if request.method == "POST":
        username = request.POST.get('username')
        score = request.POST.get('score')
        attended = request.POST.get('attended')
        try:
            user = UserScore(username=username,score3=score,attended3 = attended)
            s = int(user.totalScore)
            s += int(score)
            user.totalScore = s
            user.save()
        except:
            user = UserScore.objects.get(username=username)
            user.score3=score
            user.attended3=attended
            s = int(user.totalScore)
            s += int(score)
            user.totalScore = s
            user.save()
        attend = user.attended3
    elif request.method == "GET":
        username = request.session['username']
        try:
            user = UserScore.objects.get(username=username)
            attend = user.attended3
            score = user.score3
            print attend
        except:
            print "helo"  
    return render(request,'home/fifth.html',{'attended':attend,'score':score,'video_url':video.video.url})
def sixth_page(request):
    attend="False"
    score=0
    video = Videos.objects.get(name="Class&Object")
    
        #print "not valid object"
    if request.method == "POST":
        username = request.POST.get('username')
        score = request.POST.get('score')
        attended = request.POST.get('attended')
        try:
            user = UserScore(username=username,score4=score,attended4 = attended)
            s = int(user.totalScore)
            s += int(score)
            user.totalScore = s
            user.save()
        except:
            user = UserScore.objects.get(username=username)
            user.score4=score
            user.attended4=attended
            s = int(user.totalScore)
            s += int(score)
            user.totalScore = s
            user.save()
        attend = user.attended4
    elif request.method == "GET":
        username = request.session['username']
        try:
            user = UserScore.objects.get(username=username)
            attend = user.attended4
            score = user.score4
            print attend
        except:
            print "helo"  
    return render(request,'home/sixth.html',{'attended':attend,'score':score,'video_url':video.video.url})
def seventh_page(request):
    attend="False"
    score=0
    video = Videos.objects.get(name="Constants&Satic")
    
        #print "not valid object"
    if request.method == "POST":
        username = request.POST.get('username')
        score = request.POST.get('score')
        attended = request.POST.get('attended')
        try:
            user = UserScore(username=username,score5=score,attended5 = attended)
            s = int(user.totalScore)
            s += int(score)
            user.totalScore = s
            user.save()
        except:
            user = UserScore.objects.get(username=username)
            user.score5=score
            user.attended5=attended
            s = int(user.totalScore)
            s += int(score)
            user.totalScore = s
            user.save()
        attend = user.attended5
    elif request.method == "GET":
        username = request.session['username']
        try:
            user = UserScore.objects.get(username=username)
            attend = user.attended5
            score = user.score5
            print attend
        except:
            print "helo"  
    return render(request,'home/seventh.html',{'attended':attend,'score':score,'video_url':video.video.url})
def eighth_page(request):
    attend="False"
    score=0
    video = Videos.objects.get(name="ScannerClass")
    
        #print "not valid object"
    if request.method == "POST":
        username = request.POST.get('username')
        score = request.POST.get('score')
        attended = request.POST.get('attended')
        try:
            user = UserScore(username=username,score6=score,attended6 = attended)
            s = int(user.totalScore)
            s += int(score)
            user.totalScore = s
            user.save()
        except:
            user = UserScore.objects.get(username=username)
            user.score6=score
            user.attended6=attended
            s = int(user.totalScore)
            s += int(score)
            user.totalScore = s
            user.save()
        attend = user.attended6
    elif request.method == "GET":
        username = request.session['username']
        try:
            user = UserScore.objects.get(username=username)
            attend = user.attended6
            score = user.score6
            print attend
        except:
            print "helo"  
    return render(request,'home/eighth.html',{'attended':attend,'score':score,'video_url':video.video.url})

def ninth_page(request):
    attend="False"
    score=0
    video = Videos.objects.get(name="inheritance")
    
        #print "not valid object"
    if request.method == "POST":
        username = request.POST.get('username')
        score = request.POST.get('score')
        attended = request.POST.get('attended')
        try:
            user = UserScore(username=username,score7=score,attended7 = attended)
            s = int(user.totalScore)
            s += int(score)
            user.totalScore = s
            user.save()
        except:
            user = UserScore.objects.get(username=username)
            user.score7=score
            user.attended7=attended
            s = int(user.totalScore)
            s += int(score)
            user.totalScore = s
            user.save()
        attend = user.attended7
    elif request.method == "GET":
        username = request.session['username']
        try:
            user = UserScore.objects.get(username=username)
            attend = user.attended7
            score = user.score7
            print attend
        except:
            print "helo"  
    return render(request,'home/ninth.html',{'attended':attend,'score':score,'video_url':video.video.url})
def tenth_page(request):
    attend="False"
    score=0
    video = Videos.objects.get(name="Introduction")
    
        #print "not valid object"
    if request.method == "POST":
        username = request.POST.get('username')
        score = request.POST.get('score')
        attended = request.POST.get('attended')
        try:
            user = UserScore(username=username,score8=score,attended8 = attended)
            s = int(user.totalScore)
            s += int(score)
            user.totalScore = s
            user.save()
        except:
            user = UserScore.objects.get(username=username)
            user.score8=score
            user.attended8=attended
            s = int(user.totalScore)
            s += int(score)
            user.totalScore = s
            user.save()
        attend = user.attended8
    elif request.method == "GET":
        username = request.session['username']
        try:
            user = UserScore.objects.get(username=username)
            attend = user.attended8
            score = user.score8
            print attend
        except:
            print "helo"  
    return render(request,'home/tenth.html',{'attended':attend,'score':score,'video_url':video.video.url})
def eleventh_page(request):
    attend="False"
    score=0
    video = Videos.objects.get(name="Introduction")
    
        #print "not valid object"
    if request.method == "POST":
        username = request.POST.get('username')
        score = request.POST.get('score')
        attended = request.POST.get('attended')
        try:
            user = UserScore(username=username,score9=score,attended9 = attended)
            s = int(user.totalScore)
            s += int(score)
            user.totalScore = s
            user.save()
        except:
            user = UserScore.objects.get(username=username)
            user.score9=score
            user.attended9=attended
            s = int(user.totalScore)
            s += int(score)
            user.totalScore = s
            user.save()
        attend = user.attended9
    elif request.method == "GET":
        username = request.session['username']
        try:
            user = UserScore.objects.get(username=username)
            attend = user.attended9
            score = user.score9
            print attend
        except:
            print "helo"  
    return render(request,'home/eleventh.html',{'attended':attend,'score':score,'video_url':video.video.url})
def twelveth_page(request):
    attend="False"
    score=0
    video = Videos.objects.get(name="Introduction")
    
        #print "not valid object"
    if request.method == "POST":
        username = request.POST.get('username')
        score = request.POST.get('score')
        attended = request.POST.get('attended')
        try:
            user = UserScore(username=username,score10=score,attended10 = attended)
            s = int(user.totalScore)
            s += int(score)
            user.totalScore = s
            user.save()
        except:
            user = UserScore.objects.get(username=username)
            user.score10=score
            user.attended10=attended
            s = int(user.totalScore)
            s += int(score)
            user.totalScore = s
            user.save()
        attend = user.attended10
    elif request.method == "GET":
        username = request.session['username']
        try:
            user = UserScore.objects.get(username=username)
            attend = user.attended10
            score = user.score10
            print attend
        except:
            print "helo"  
    return render(request,'home/twelveth.html',{'attended':attend,'score':score,'video_url':video.video.url})
def thirteenth_page(request):
    attend="False"
    score=0
    video = Videos.objects.get(name="Introduction")
    
        #print "not valid object"
    if request.method == "POST":
        username = request.POST.get('username')
        score = request.POST.get('score')
        attended = request.POST.get('attended')
        try:
            user = UserScore(username=username,score11=score,attended11 = attended)
            s = int(user.totalScore)
            s += int(score)
            user.totalScore = s
            user.save()
        except:
            user = UserScore.objects.get(username=username)
            user.score11=score
            user.attended11=attended
            s = int(user.totalScore)
            s += int(score)
            user.totalScore = s
            user.save()
        attend = user.attended11
    elif request.method == "GET":
        username = request.session['username']
        try:
            user = UserScore.objects.get(username=username)
            attend = user.attended11
            score = user.score11
            print attend
        except:
            print "helo"  
    return render(request,'home/thirteenth.html',{'attended':attend,'score':score,'video_url':video.video.url})
def fourteenth_page(request):
    attend="False"
    score=0
    video = Videos.objects.get(name="Datatypes")
    
        #print "not valid object"
    if request.method == "POST":
        username = request.POST.get('username')
        score = request.POST.get('score')
        attended = request.POST.get('attended')
        try:
            user = UserScore(username=username,score12=score,attended12 = attended)
            s = int(user.totalScore)
            s += int(score)
            user.totalScore = s
            user.save()
        except:
            user = UserScore.objects.get(username=username)
            user.score12=score
            user.attended12=attended
            s = int(user.totalScore)
            s += int(score)
            user.totalScore = s
            user.save()
        attend = user.attended12
    elif request.method == "GET":
        username = request.session['username']
        try:
            user = UserScore.objects.get(username=username)
            attend = user.attended12
            score = user.score12
            print attend
        except:
            print "helo"  
    return render(request,'home/fourteenth.html',{'attended':attend,'score':score,'video_url':video.video.url})
def fifteenth_page(request):
    attend="False"
    score=0
    video = Videos.objects.get(name="ControlStructure")
    
        #print "not valid object"
    if request.method == "POST":
        username = request.POST.get('username')
        score = request.POST.get('score')
        attended = request.POST.get('attended')
        try:
            user = UserScore(username=username,score13=score,attended13 = attended)
            s = int(user.totalScore)
            s += int(score)
            user.totalScore = s
            user.save()
        except:
            user = UserScore.objects.get(username=username)
            user.score13=score
            user.attended13=attended
            s = int(user.totalScore)
            s += int(score)
            user.totalScore = s 
            user.save()
        attend = user.attended13
    elif request.method == "GET":
        username = request.session['username']
        try:
            user = UserScore.objects.get(username=username)
            attend = user.attended13
            score = user.score13
            print attend
        except:
            print "helo"  
    return render(request,'home/fifteenth.html',{'attended':attend,'score':score,'video_url':video.video.url})

@login_required  
def leaderboard(request):
    scores = UserScore.objects.order_by('-totalScore')
    #scores.sort(key=lambda x:x.score,reverse=True)
    #s = scores.score
    return render(request,'home/leaderboard.html',{'scores':scores})


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'home/registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})

def contactUs(request):
    return render(request,'home/contact.html')
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username,password = password)
        if user:
            if user.is_active:
                login(request,user)
                request.session['username'] = username
                return render(request,'home/sec.html')
                #return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive")
        else:
            print "Someone tried to login and failed"
            print "They used username: {} and password: {} ".format(username,password)
            return render(request,'home/failure.html',{})
    else:
        return render(request,'home/login.html',{})
