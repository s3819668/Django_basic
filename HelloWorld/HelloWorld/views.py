from django.shortcuts import render
def index(request):
    context={}
    context["name"]="Salmon"

    skill_list=["python","mysql","js"]
    context["skill_list"]=skill_list

    skill_dict={"python":"familar","mysql":"medium","js":"beinger"}
    context["skill_dict"]=skill_dict

    age=24
    context["age"]=age
    empty=[]
    context["empty"]=empty

    score=80
    context["score"]=score

    return render(request,"index.html",context)
def index1(request):
    context={}
    context["name"]="TORO"
    return render(request,"index1.html",context)