from django.contrib.auth.models import User
from rest_framework import serializers

from profiles.models import Profile


class ProfileSerializer(serializers.ModelSerializer):

	class Meta:
		model = Profile
		fields = [
			'id',
			'location',
			'number',
			'user'
		]
