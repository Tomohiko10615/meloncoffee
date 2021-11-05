# accounts/views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

"""
def showform(request):
    form= FormContactForm(request.POST or None)
    if form.is_valid():
        form.save()
  
    context= {'form': form }
        
    return render(request, 'registration/signup.html', context)
"""

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    failed = False

    def get_context_data(self, **kwargs):
        context = super(SignUpView, self).get_context_data(**kwargs)
        context['failed'] = self.failed
        return context

"""
def signup(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        email = request.POST["email"]
        password = request.POST["password"]
        phone = request.POST["phone"]
        birthday = request.POST["birthday"]

        user = CustomUser()

        user.nombre = request.POST.get('nombre')
        user.apellido = request.POST.get('apellido')
        user.email = request.POST.get('email')
        user.password = request.POST.get('password')
        user.phone = request.POST.get('phone')
        user.birthday = request.POST.get('birthday')
        user.save()

    return render(request, 'registration/signup.html') 
"""