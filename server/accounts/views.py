from django.shortcuts import render
from django.views.generic import View

from .forms import ProfileForm


class ProfileView(View):

    def get(self, request):
        profile_form = ProfileForm(instance=request.user.profile)
        return render(request, 'account/profile.html',
                      {'profile_form': profile_form})

    def post(self, request):
        success = False
        form = ProfileForm(request.POST,
                           instance=request.user.profile)
        if form.is_valid():
            form.save()
            success = True
            return render(request,
                          'account/profile.html', {'profile_form': form,
                                                   'success': success})

profile_view = ProfileView.as_view()
