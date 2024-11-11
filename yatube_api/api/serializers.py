from posts.models import Comment, Post, Group, Follow
from rest_framework import serializers
from rest_framework.relations import StringRelatedField


class PostSerializer(serializers.ModelSerializer):
    author = StringRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    following = StringRelatedField(read_only=True)
    user = StringRelatedField(read_only=True)

    class Meta:
        fields = ('user', 'following')
        model = Follow
