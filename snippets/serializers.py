from rest_framework import serializers
from snippets.models import Snippet
from snippets.models import Snippet, Snippet2


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ("id", "title", "code")


class SnippetSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Snippet2
        fields = ("id", "username", "password", "email")
