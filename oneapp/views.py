
from .models import City, Country, Rbl
from .serializers import CitySerializer, CountrySerializer, RblSerializer

from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Car


@registry.register_document
class CarDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'cars'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Car # The model associated with this Document

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'name',
            'color',
            'description',
            'type',
        ]


class shivangi(APIView):
    def get(self, request):
        articles = City.objects.all()
        return Response({"articles": articles})

    def post(self, request):
        query = "SELECT * FROM phoenix.cus_tbl"
        queryset = City.objects.raw(query)
        print(request.data, 'shshshsh')
        serializer = CitySerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

def get_users(request):
    print(request.method, 'hello')
    query="SELECT * FROM phoenix.cus_tbl"
    queryset=City.objects.raw(query)
    print(queryset,'shshshsh')
    serializer = CitySerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False)

def dictfetchall(cursor):
    # Returns all rows from a cursor as a dict
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]
def get_city(request):
    query="SELECT * phoenix.cus_tbl"

    # cursor = connection.cursor()
    # cursor.execute(query)

    # queryset = Rbl.objects.raw(query)
    # for p in queryset:
    #     print('djd')
    # serializer = RblSerializer(query, many=True)
    return JsonResponse('dhdh', safe=False)



def balance_trend(request):
    # query = "SELECT * FROM phoenix.fact_daily where source!='Revenue' and account_no=013108032"
    query="SELECT balance_date ,sum(icy_balance) as balance FROM phoenix.fact_daily where source!='Revenue' and account_no='013108032' group by balance_date"
    queryset = Country.objects.raw(query)
    serializer = CountrySerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False)


def get_trends(request):
    print(request.method, request)
    query = "SELECT * FROM world.city"
    queryset = City.objects.raw(query)
    print(queryset,'shshshsh')
    serializer = CitySerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False)

