from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Project,Profile
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm,ProfileForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user
    projects = Project.get_all()
    return render(request,'index.html',{'projects':projects})

def project(request,project_id):
    try:
        project = Project.objects.get(id = project_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,'project-detail.html',{'project':project})

@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.profile = current_user
            project.save()
        return redirect('indexPage')

    else:
        form = ProjectForm()
    return render(request, 'new_project.html', {"form": form})

def profile(request):
    current_user = request.user
    projects = Project.objects.filter(profile=current_user)

    print(current_user)


    #
    # try:
    #     profile = Profile.objects.get(profile = current_user)
    # except ObjectDoesNotExist:
    #     return redirect('create-profile')
    return render(request, 'profile.html',{'projects':projects,'profile':profile})

def create_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.project = current_user
            profile.save()
        return redirect('Profile')
    else:
        form = ProfileForm()
    return render(request,'create_profile.html',{'form':form})

def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def search_project(request,project_id):
    try :
        project = Project.objects.get(id = project_id)

    except ObjectDoesNotExist:
        raise Http404()
        # return render(request, 'no_project.html')

    return render(request, 'project-detail.html', {'project':project})