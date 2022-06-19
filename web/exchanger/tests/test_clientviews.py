from rest_framework import status
from rest_framework.test import APITestCase
from exchanger.models import Currency


class ClientRequestViewApiTestCase(APITestCase):
    def test_usd_to_uah(self):
        print("-----------------Test USD to UAH----------------")
        test_currency = Currency.objects.create(name="USD", sign="$", uah=29.25, countries="USA, American Samoa (US),British Virgin Islands (UK),Caribbean Netherlands (Netherlands),Guam (USA),Northern Mariana Islands (US),Puerto Rico (US),Turks and Caicos (UK),US Virgin Islands (US) Cambodia(Alongside the Cambodian Riel),East Timor, Ecuador")
        test_currency2 = Currency.objects.create(name="UAH", sign="₴", uah=1.0, countries="Ukraine")
        url = 'http://127.0.0.1:8000/api/v1/clientrequest?amount=25.5&get=UAH&give=USD'
        amount = 25.5
        response = self.client.get(url)
        proccesed_value = response.data["Converted value in ₴"]
        expected_value = round(amount * 29.25, 2)
        print({'expected value': expected_value,
               'processed value': proccesed_value})
        self.assertEqual(expected_value, proccesed_value)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_usd_to_eur(self):
        print("-----------------Test USD to EUR----------------")
        test_currency = Currency.objects.create(name="USD", sign="$", uah=29.25,
                                                countries="USA, American Samoa (US),British Virgin Islands (UK),Caribbean Netherlands (Netherlands),Guam (USA),Northern Mariana Islands (US),Puerto Rico (US),Turks and Caicos (UK),US Virgin Islands (US) Cambodia(Alongside the Cambodian Riel),East Timor, Ecuador")
        test_currency2 = Currency.objects.create(name="EUR", sign="€", uah=31.32, countries="Europian countries")
        url = 'http://127.0.0.1:8000/api/v1/clientrequest?amount=25.5&get=EUR&give=USD'
        amount = 25.5
        response = self.client.get(url)
        proccesed_value = response.data["Converted value in €"]
        temp = amount * 29.25
        expected_value = round(temp / 31.32, 2)
        print({'expected value': expected_value,
               'processed value': proccesed_value})
        self.assertEqual(expected_value, proccesed_value)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_uah_to_gbp(self):
        print("-----------------Test UAH to GBP----------------")
        test_currency = Currency.objects.create(name="UAH", sign="₴", uah=1.0, countries="Ukraine")
        test_currency2 = Currency.objects.create(name="GBP", sign="£", uah=36.89, countries="United Kingdom")
        url = 'http://127.0.0.1:8000/api/v1/clientrequest?amount=25.5&get=GBP&give=UAH'
        amount = 25.5
        response = self.client.get(url)
        proccesed_value = response.data["Converted value in £"]
        expected_value = round(amount / 36.89, 2)
        print({'expected value': expected_value,
               'processed value': proccesed_value})
        self.assertEqual(expected_value, proccesed_value)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

