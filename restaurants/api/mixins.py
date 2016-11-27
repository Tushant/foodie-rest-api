from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

class AuthRequireMixin(object):
	def dispatch(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return redirect('/admin/')
		return super(AuthRequireMixin, self).dispatch(request, *args, **kwargs)

class UserRestaurantMixin(AuthRequireMixin):
	def dispatch(self, request, *args, **kwargs):
		print('self.object', self.get_object())
		if request.user.is_authenticated() and request.user.id is not self.get_object().owner.id:
			raise PermissionDenied
		return super(UserRestaurantMixin, self).dispatch(request, *args, **kwargs)