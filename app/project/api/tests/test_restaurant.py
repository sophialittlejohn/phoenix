from rest_framework import status

from project.api.tests.master_tests import MasterTestWrapper
from project.feed.models import Restaurant, Category


class ListAllRestaurantsTests(MasterTestWrapper.BasicMasterTests):
    endpoint = 'api:restaurants:all'
    methods = ['GET']

    def setUp(self):
        super().setUp()
        for i in range(5):
            Restaurant.objects.create(
                user=self.user,
                name=f'Restaurant {i}',
                country='CH',
                street='Strasse',
                city='Zurich',
                phone_number='+1234567890',
                opening_hours='24/7',
                price_level='HIGH',
            )

    def test_all_restaurants_length(self):
        self.authorize()
        response = self.client.get(self.get_url())
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data), 5)


class NewRestaurantTests(MasterTestWrapper.MasterTests):
    endpoint = 'api:restaurants:new_restaurant'
    methods = ['POST']

    def setUp(self):
        super().setUp()

    def test_create_restaurant(self):
        self.authorize()
        response = self.client.post(self.get_url(), {'name': 'new restaurant',
                                                     'country': 'CH',
                                                     'street': 'Strasse',
                                                     'city': 'Zurich',
                                                     'phone_number': '+1234567890',
                                                     'opening_hours': '24/7',
                                                     'price_level': 'HIGH',
                                                     'user': self.user,
                                                     })
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(response.data.get('name'), 'new restaurant')
        self.assertEquals(Restaurant.objects.first().name, 'new restaurant')


class RestaurantGetUpdateDelete(MasterTestWrapper.BasicMasterTests):
    endpoint = 'api:restaurants:get_update_delete_restaurant'
    methods = ['GET', 'POST', 'DELETE']

    def get_kwargs(self):
        return {
            'pk': self.restaurant.id
        }

    def setUp(self):
        super().setUp()

        self.restaurant = Restaurant.objects.create(
            user=self.user,
            name='Restaurant 1',
            country='CH',
            street='Strasse',
            city='Zurich',
            phone_number='+1234567890',
            opening_hours='24/7',
            price_level='HIGH',
        )

    def test_get_restaurant(self):
        self.authorize()
        response = self.client.get(self.get_url(**self.kwargs))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(Restaurant.objects.first().name, 'Restaurant 1')
        self.assertEquals(Restaurant.objects.first().user, self.user)

    # def test_update_restaurant(self):
    #     self.authorize()
    #     response = self.client.post(self.get_url(**self.kwargs), {'name': 'updated restaurant'})
    #     self.assertEquals(response.status_code, status.HTTP_200_OK)
    #     # self.assertEquals(Restaurant.objects.filter(id=self.restaurant.id).count(), 0)

    # def test_update_not_owner_restaurant(self):
    #     self.authorize(self.other_user)
    #     response = self.client.delete(self.get_url(**self.kwargs))
    #     self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)
    #     self.assertIsNotNone(Restaurant.objects.get(id=self.restaurant.id))

    def test_delete_restaurant(self):
        self.authorize()
        response = self.client.delete(self.get_url(**self.kwargs))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(Restaurant.objects.filter(id=self.restaurant.id).count(), 0)

    def test_delete_not_owner_restaurant(self):
        self.authorize(self.other_user)
        response = self.client.delete(self.get_url(**self.kwargs))
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertIsNotNone(Restaurant.objects.get(id=self.restaurant.id))


class CategoryRestaurantsTests(MasterTestWrapper.BasicMasterTests):
    endpoint = 'api:restaurants:category_restaurants'
    methods = ['GET']

    def get_kwargs(self):
        return {
            'pk': self.category.id
        }

    def setUp(self):
        super().setUp()
        self.category = Category.objects.create(name='swiss')
        for i in range(5):
            Restaurant.objects.create(
                user=self.user,
                name=f'Restaurant {i}',
                country='CH',
                street='Strasse',
                city='Zurich',
                phone_number='+1234567890',
                opening_hours='24/7',
                price_level='HIGH',
                category=self.category
            )

    def test_category_restaurants(self):
        self.authorize()
        response = self.client.get(self.get_url(**self.kwargs))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data), 5)
        self.assertEquals(Restaurant.objects.first().category.name, 'swiss')


class UserRestaurantsTests(MasterTestWrapper.BasicMasterTests):
    endpoint = 'api:restaurants:user_restaurants'
    methods = ['GET']

    def get_kwargs(self):
        return {
            'pk': self.user.id
        }

    def setUp(self):
        super().setUp()
        for i in range(5):
            Restaurant.objects.create(
                user=self.user,
                name=f'Restaurant {i}',
                country='CH',
                street='Strasse',
                city='Zurich',
                phone_number='+1234567890',
                opening_hours='24/7',
                price_level='HIGH',
            )

    def test_user_restaurants(self):
        self.authorize()
        response = self.client.get(self.get_url(**self.kwargs))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data), 5)
        self.assertEquals(Restaurant.objects.first().name, 'Restaurant 0')
        self.assertEquals(Restaurant.objects.first().user, self.user)
