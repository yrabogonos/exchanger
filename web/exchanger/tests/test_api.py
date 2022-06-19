from rest_framework import status
from rest_framework.test import APITestCase
from exchanger.models import Currency
from exchanger.serializers import CurrencySerializer


class ExchangerApiTestCase(APITestCase):
    def test_get(self):
        print("-----------------Test Getting----------------")
        test_currency = Currency.objects.create(name="test", sign="test", uah=0, countries="test")
        url = 'http://127.0.0.1:8000/api/v1/currency'
        print(url)
        response = self.client.get(url)
        ser_data = CurrencySerializer(test_currency).data
        print(ser_data)
        """reformatting response.data to dict"""


        r = response.data["data"]
        response_dict = {'name': r[0]['name'], 'sign': r[0]['sign'], 'uah': r[0]['uah'], 'countries': r[0]['countries']}


        print(response_dict)
        self.assertEqual(ser_data, response_dict)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_post(self):
        print("-----------------Test Posting----------------")
        url = 'http://127.0.0.1:8000/api/v1/currency'
        data = {
            'name': 'test',
            'sign': 'test',
            'uah': 0,
            'countries': 'test'}

        response = self.client.post(url, data=data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        data_to_compare = self.client.get(url)

        """reformatting response.data to dict"""

        r = data_to_compare.data["data"]

        response_dict_compare = {'name': r[0]['name'], 'sign': r[0]['sign'], 'uah': r[0]['uah'], 'countries': r[0]['countries']}
        print(response_dict_compare)
        print(response.data["posted"])
        self.assertEqual(response_dict_compare, response.data["posted"])

    def test_delete(self):
        print("-----------------Test Deleting----------------")
        url = 'http://127.0.0.1:8000/api/v1/currency'

        url_to_del = 'http://127.0.0.1:8000/api/v1/currency/testdel/'
        data = {
            'name': 'testdel',
            'sign': 'testdel',
            'uah': 0,
            'countries': 'testdel'}
        test_currency = self.client.post(url, data=data)
        name = test_currency.data["posted"]["name"]
        obj = Currency.objects.get(name=name)
        del_obj = obj.delete()
        self.assertFalse(Currency.objects.filter(name=name).exists())
        self.assertEqual(status.HTTP_200_OK, test_currency.status_code)






