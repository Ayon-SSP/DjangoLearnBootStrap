from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("<center><h1>Home 🏠 </h1></center>")
    # To send variables to the template, we use the render function
    context = {
        'Name' : 'Ayon Karmakar',
        'age' : 21,
        'hobbies' : ['Coding', 'Gaming', 'Sleeping', 'Eating', 'Watching Anime'],
        'profileImageUrl': 'https://avatars.githubusercontent.com/u/80549753?s=400&u=74659f0d3a599612e461950bd720e16345ebf4c8&v=4',
    }
    # return render(request, 'index.html', context)
    return render(request, 'bootstrapComp.html')
def docs(request):
    return HttpResponse("<center><h1>Docs 📚 </h1></center>")
def about(request):
    return HttpResponse("<center><h1>About 🅰️ </h1></center>")
    # return render(request, 'about.html')
def services(request):
    return HttpResponse("<center><h1>Services 🛠️ </h1></center>")
def contact(request):
    return HttpResponse("<center><h1>Contact 📞 </h1></center>")
def profile(request):
    # return HttpResponse("<center><h1>Profile 📝 </h1></center>")
    profileLinks = {
        'pL' : ['https://us.123rf.com/450wm/moremar/moremar1903/moremar190300013/moremar190300013.jpg?ver=6',
                'https://media.istockphoto.com/id/1193146236/vector/portrait-of-a-businessman-avatar-of-a-young-man-for-social-network.jpg?s=170667a&w=0&k=20&c=tzuR2fBVV1ThyKl3p-8DRPDj1yD4ttC5_myLku6CAT8=',
                'https://media.istockphoto.com/id/1190616457/vector/head-of-a-little-asian-girl-in-profile-the-face-of-a-child-on-the-side-portrait-avatar.jpg?s=612x612&w=0&k=20&c=P2MQJWGzhx86zrHnvjOL8jRc7IMtv7mu1AVYMHwyudw=',
                'https://media.istockphoto.com/id/1190616551/vector/head-of-a-little-asian-boy-in-profile-the-face-of-a-child-on-the-side-portrait-avatar.jpg?s=170667a&w=0&k=20&c=g24hXtlRXkXPCEGEtWijmxSV1Xu3TbPWY6oTRLNGTEI='
                ],
        'pL1' : 'https://media.istockphoto.com/id/1188460614/vector/portrait-of-a-young-beautiful-asian-fashion-woman-vector-flat-illustration-asian-cute-girl.jpg?s=612x612&w=0&k=20&c=1oOJoBKyyhS_VjqRGHoZ1p-zyfmnpAI7TYM_9y5DqzM=',
        'pL2' : 'https://media.istockphoto.com/id/1193146236/vector/portrait-of-a-businessman-avatar-of-a-young-man-for-social-network.jpg?s=170667a&w=0&k=20&c=tzuR2fBVV1ThyKl3p-8DRPDj1yD4ttC5_myLku6CAT8=',
        'pL3' : 'https://media.istockphoto.com/id/1190616457/vector/head-of-a-little-asian-girl-in-profile-the-face-of-a-child-on-the-side-portrait-avatar.jpg?s=612x612&w=0&k=20&c=P2MQJWGzhx86zrHnvjOL8jRc7IMtv7mu1AVYMHwyudw=',
        'pL4' : 'https://media.istockphoto.com/id/1190616551/vector/head-of-a-little-asian-boy-in-profile-the-face-of-a-child-on-the-side-portrait-avatar.jpg?s=170667a&w=0&k=20&c=g24hXtlRXkXPCEGEtWijmxSV1Xu3TbPWY6oTRLNGTEI='
    }
    return render(request, 'profiles.html',profileLinks)
def bsLearning(request):
    # return HttpResponse("<center><h1>Bootstrap Learning 📚 </h1></center>")
    return render(request, 'bootstrapComp.html')