from django.db.models import Q
from rest_framework import viewsets, generics

from .serializers import ProfileSerializer
from profiles.models import Profile


class ProfileViewSet(viewsets.ModelViewSet):
	"""
	A simple ViewSet for viewing and editing seller profiles.
	"""
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer
	# permission_classes = [IsAccountAdminOrReadOnly]


class ProfileAPIView(generics.RetrieveAPIView):
	# lookup_field = 'pk'
	serializer_class = ProfileSerializer

	def get_queryset(self):
		qs = Profile.objects.all()
		query = self.request.GET.get("q")
		print(query)
		if query is not None:
			qs = qs.filter(
				Q(number__icontains=query)
			).distinct()
		return qs

