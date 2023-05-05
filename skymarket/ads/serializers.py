from rest_framework import serializers

from ads.models import Ad, Comment


# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою

class CommentSerializer(serializers.ModelSerializer):
    author_id = serializers.IntegerField(source="author_id", read_only=True)
    ad_id = serializers.IntegerField(source="ad_id", read_only=True)
    author_first_name = serializers.CharField(source="author_first_name", read_only=True)
    author_last_name = serializers.CharField(source="author_last_name", read_only=True)
    author_image = serializers.ImageField(source="author_image", read_only=True)

    class Meta:
        model = Comment
        fields = ("pk", "text", "author_id", "ad_id", "author_first_name", "author_last_name", "author_image")


class AdSerializer(serializers.ModelSerializer):
    author_id = serializers.IntegerField(source="author.author_id", read_only=True)
    phone = serializers.CharField(source="author.phone", read_only=True)
    author_first_name = serializers.CharField(source="author.author_first_name", read_only=True)
    author_last_name = serializers.CharField(source="author.author_last_name", read_only=True)
    class Meta:
        model = Ad
        fields = ("pk",
                  "title",
                  "price",
                  "description",
                  "author_id",
                  "phone",
                  "image",
                  "author_first_name",
                  "author_last_name")


class AdDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ("pk", "title", "price", "description", "author", "created_at", "image")
