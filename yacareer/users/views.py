from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView

from users.forms import (
    CreateProfileForm,
    ProfileLinksForm,
    ProfileMediaForm,
    UpdateProfileForm,
)
from users.models import Profile, ProfileLinks, ProfileMedia


class SignUpView(FormView):
    template_name = 'users/signup.html'
    model = Profile
    form_class = CreateProfileForm
    success_url = reverse_lazy('users:profile')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class UserDetailView(DetailView):
    template_name = 'users/user_detail.html'
    model = Profile
    context_object_name = 'user'


class ProfileView(LoginRequiredMixin, FormView):
    template_name = 'users/profile.html'
    form_class = UpdateProfileForm
    model = Profile
    success_url = reverse_lazy('users:profile')

    def get_context_data(self, **kwargs):
        profile_form = self.form_class(
            initial=self.initial,
            instance=self.request.user,
        )
        media_form = ProfileMediaForm()
        links_form = ProfileLinksForm()
        return {
            'profileform': profile_form,
            'mediaform': media_form,
            'linksform': links_form,
        }

    def post(self, request):
        if request.FILES.get('file', False):
            self.media_form(request)
        elif 'email' in request.POST:
            self.profile_form(request)
        else:
            self.link_form(request)
        return redirect('users:profile')

    def link_form(self, request):
        form = ProfileLinksForm(
            request.POST or None,
            instance=request.user,
        )
        if form.is_valid():
            ProfileLinks.objects.create(
                profile_id=request.user.id,
                **form.cleaned_data,
            )

    def media_form(self, request):
        form = ProfileMediaForm(
            *(request.POST, request.FILES) or None,
            instance=request.user,
        )
        if form.is_valid():
            file = form.cleaned_data['file']
            if file:
                fs = FileSystemStorage('media/files')
                form.cleaned_data['file'] = f'files/{file.name}'
                fs.save(file.name, file)
            form.save()

    def profile_form(self, request):
        form = self.form_class(
            *(request.POST, request.FILES) or None,
            instance=request.user,
        )
        if form.is_valid():
            file = form.cleaned_data['photo']
            if str(file) != 'False':
                fs = FileSystemStorage('media/images')
                form.cleaned_data['photo'] = f'images/{file.name}'
                fs.save(file.name, file)
            self.model.objects.filter(id=request.user.id).update(
                **form.cleaned_data,
            )


class DeleteLinkView(LoginRequiredMixin, DetailView):
    model = ProfileLinks

    def get(self, request, pk):
        self.model.objects.get(
            pk=pk,
            profile_id=request.user.id,
        ).delete()
        return redirect('users:profile')


class DeleteMediaView(LoginRequiredMixin, DetailView):
    model = ProfileMedia

    def get(self, request, pk):
        self.model.objects.get(
            pk=pk,
            profile_id=request.user.id,
        ).delete()
        return redirect('users:profile')
