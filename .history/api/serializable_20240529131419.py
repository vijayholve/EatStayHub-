from rest_framework.serializers import ModelSerializer
from base.models import restaurants,dish

class serializer_restaurant(ModelSerializer):
    class Meta:
        model=restaurants
        fields="__all__"
class serializer_dish(ModelSerializer):
    class Meta:
        model=dish
        fields="__all__"

class serialize_restaurant_dish(ModelSerializer)
