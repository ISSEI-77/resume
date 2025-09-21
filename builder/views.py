from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def resume1(request):
    if request.method == "POST":
        data = request.POST.dict()

        skills = [s.strip() for s in data.get("skills", "").split(",") if s.strip()]
        experience = [exp.strip() for exp in data.get("experience", "").split("\n") if exp.strip()]
        education = [edu.strip() for edu in data.get("education", "").split("\n") if edu.strip()]

        return render(request, "resume1.html", {
            "data": data,
            "skills": skills,
            "experience": experience,
            "education": education
        })
    return render(request, "index.html")

def resume2(request):
    if request.method == "POST":
        data = request.POST.dict()

        skills = [s.strip() for s in data.get("skills", "").split(",") if s.strip()]
        experience = [exp.strip() for exp in data.get("experience", "").split("\n") if exp.strip()]
        education = [edu.strip() for edu in data.get("education", "").split("\n") if edu.strip()]

        return render(request, "resume2.html", {
            "data": data,
            "skills": skills,
            "experience": experience,
            "education": education
        })
    return render(request, "index.html")
