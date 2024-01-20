from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from dj_rest_auth.serializers import UserDetailsSerializer


class CurrentUserSerializer(UserDetailsSerializer):
    """
    Custom serializer to return the current user's dprofile id and profile image
    """
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id',
            'profile_image',
        )
