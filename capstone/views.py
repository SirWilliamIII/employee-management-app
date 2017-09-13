from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from .forms import EmployeeAdmin
from .models import Employee
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView
import datetime


def my_profile(request, pk):
    profile = get_object_or_404(Employee, pk=pk)
    if request.method.upper() == 'POST':
        form = EmployeeAdmin(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('my_profile_detail.html', {'form': form})


def index(request):
    if request.method.upper == 'GET':
        return render(request, 'index.html', {})


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return html


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {})

    def post(self, request, *args, **kwargs):
        return render(request, 'index.html', {})


class IndexGenericView(TemplateView):
    template_name = 'index.html'


class ProfileView(View):
    form_class = EmployeeAdmin

    template_name = 'my_profile_detail.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(instance=self.get_context_data().get('profile'))
        return render(request, self.get_template_name(), {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=self.get_object())
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')
        return render(request, self.template_name, {'form': form})

    def get_template_name(self):
        return self.template_name


    def get_context_data(self):
        """Returns the data passed to the template"""
        return {
            'profile': self.get_object(),
        }

    def get_object(self):
        return get_object_or_404(Employee, pk=self.kwargs.get('pk'))


class ProfileListView(ListView):
    model = Employee
    template_name = 'profile_list.html'
    paginate_by = 100

    def get_queryset(self):
        order_by_field = self.request.GET.get('order_by') or '-hire_date'
        queryset = super(ProfileListView, self).get_queryset()
        return queryset.order_by(order_by_field)


class ProfileDetailView(DetailView):
    template_name = 'profile_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        context['salary_entries'] = Salary.object.filter(emp_no__exact=self.object.emp_no)


class ProfileCreateView(CreateView):
    template_name = 'profile_create.html'
    success_url = reverse_lazy('profile_list')

    def get_initial(self):
        inital = super(ProfileCreateView, self).get_initial()
        initial['emp_no'] = generate_next_emp_no
        return inital


class ProfileDeleteView(DeleteView):
    model = Employee
    success_url = reverse_lazy('profile_list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class ProfileUpdateView(UpdateView):
    template_name = 'profile_update.html'
    model = Employee
    success_url = reverse_lazy('profile_list')
