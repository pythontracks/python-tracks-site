from django.shortcuts import render
from django.views import View


class IndexView(View):

	template = 'tracks/index.html'
	context = {}

	def get(self, request):
		return render(
			request,
			self.template,
			self.context
		)
