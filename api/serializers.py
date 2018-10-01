from rest_framework import serializers
from projectplace.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    category = TagsSerializer(read_only=True)
    owner_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Post
        fields = ('title', 'body', 'reated_at',
                  'author', 'owner_id')

