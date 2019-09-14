
from rest_framework import serializers
from .models import City, Country, Rbl


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"

class RblSerializer(serializers.ModelSerializer):
    # id = models.IntegerField(db_column='jobdep_id', primary_key=True)
    class Meta:
        model = Rbl
        fields = ('id', 'balance', 'balance_date')

class CountrySerializer(serializers.ModelSerializer):
    # id = serializers.ModelField(model_field=FactDaily._meta.get_fields(include_hidden=True))
    # position = FactDaily(default=None)
    # dependent_value = serializers.IntegerField(default=get_default_value)  # don't put paranthesis [ie, "()"] for the function

    class Meta:
        model = Country
        fields = "__all__"
