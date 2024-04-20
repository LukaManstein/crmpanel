from django.shortcuts import render, redirect


def index(request):
	return render(request,'login/login.html')

class LoginUser(DataMixin, LoginView):
	form_class = AuthenticationForm
	template_name = 'login/login.html'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		c_def = self.get_user_context(title="Autorithation")
		return dict(list(context.items()) + list(c_def.items()))
		x
