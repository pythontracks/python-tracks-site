from django.shortcuts import render
from django.views import View
from .settings import app_config


class IndexView(View):

	template = 'core/index.html'
	context = {
		'config': app_config,
	}

	def get(self, request):
		return render(
			request,
			self.template,
			self.context
		)
