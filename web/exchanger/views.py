# Create your views here.
from rest_framework.response import Response

from exchanger.models import Currency
from exchanger.serializers import CurrencySerializer
from rest_framework.views import APIView
import logging


logger = logging.getLogger(__name__)


class CurrencyView(APIView):
    def get(self, request):
        logger.info("Get request working!")
        obj = Currency.objects.all()
        return Response({'data': CurrencySerializer(obj, many=True).data})

    def post(self, request):
        logger.info("Post request working!")
        serializer = CurrencySerializer(data=request.data)
        if not serializer.is_valid(): logger.error("Data doesn`t match serializer`s requirements")
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'posted': serializer.data})

    def put(self, request, *args, **kwargs):
        logger.info("Put request working!")
        pk = kwargs.get("pk", None)
        if not pk:
            logger.error("Method PUT is not allowed")
            return Response({"Error": "Method PUT is not allowed"})

        try:
            instance = Currency.objects.get(name=pk)
        except:
            logger.error("Object doesn`t exist")
            return Response({"Error": "Object doesn`t exist"})

        serializer = CurrencySerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"updated": serializer.data})

    def delete(self, request, *args, **kwargs):
        logger.info("Delete request working!")
        pk = kwargs.get("pk", None)
        if not pk:
            logger.error("Method DELETE is not allowed")
            return Response({"Error": "Method DELETE is not allowed"})
        try:
            currency_to_delete = Currency.objects.get(name=pk)
        except:
            logger.error("Object doesn`t exist")
            return Response({"Error": "Object doesn`t exist"})

        serializer = CurrencySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        currency_to_delete.delete()
        return Response({'deleted': serializer.data})


class ClientRequestView(APIView):
    def get(self, request):
        logger.info("Exchanging request working!")
        try:
            name = request.query_params["give"]
            amount = request.query_params["amount"]
            wanted = request.query_params["get"]
        except:
            logger.error("Error in arguments. Expecting 3 arguments")
        obj = Currency.objects.get(name=name)
        obj2 = Currency.objects.get(name=wanted)
        information = Currency.objects.filter(name=wanted)
        temp = obj.uah * float(amount)
        result = temp / obj2.uah
        return Response({'Converted value in ' + obj2.sign: round(result, 2), 'information': CurrencySerializer(information, many=True).data})
