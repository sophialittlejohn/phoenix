from rest_framework import status

from project.api.tests.master_tests import MasterTestWrapper
from project.feed.models import Restaurant, Category, Review


class NewReviewTests(MasterTestWrapper.MasterTests):
    endpoint = 'api:reviews:new_review'
    methods = ['POST']

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

    def test_create_review(self):
        self.authorize()
        response = self.client.post(self.get_url(**self.kwargs), {'content': 'new reviews',
                                                                  'rating': 2,
                                                                  })
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(response.data.get('content'), 'new reviews')
        self.assertEquals(Review.objects.first().content, 'new reviews')


class ReviewGetUpdateDelete(MasterTestWrapper.BasicMasterTests):
    endpoint = 'api:reviews:review_get_update_delete'
    methods = ['GET', 'POST', 'DELETE']

    def get_kwargs(self):
        return {
            'pk': self.review.id
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
        self.review = Review.objects.create(
            content='test reviews',
            rating=1,
            user=self.user,
            restaurant=self.restaurant
        )

    def test_get_review(self):
        self.authorize()
        response = self.client.get(self.get_url(**self.kwargs))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(Review.objects.first().content, 'test reviews')
        self.assertEquals(Review.objects.first().user, self.user)

    def test_update_review(self):
        self.authorize()
        response = self.client.post(self.get_url(**self.kwargs), {'content': 'updated reviews',
                                                                  'rating': 1})
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(Review.objects.filter(id=self.review.id).count(), 1)

    def test_update_not_owner_review(self):
        self.authorize(self.other_user)
        response = self.client.delete(self.get_url(**self.kwargs), {'content': 'updated reviews',
                                                                    'rating': 1})
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertIsNotNone(Review.objects.get(id=self.review.id))

    def test_delete_review(self):
        self.authorize()
        response = self.client.delete(self.get_url(**self.kwargs))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(Review.objects.filter(id=self.review.id).count(), 0)

    def test_delete_not_owner_review(self):
        self.authorize(self.other_user)
        response = self.client.delete(self.get_url(**self.kwargs))
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertIsNotNone(Review.objects.get(id=self.review.id))


class RestaurantReviewsTests(MasterTestWrapper.BasicMasterTests):
    endpoint = 'api:reviews:restaurant_reviews'
    methods = ['GET']

    def get_kwargs(self):
        return {
            'pk': self.restaurant.id
        }

    def setUp(self):
        super().setUp()
        self.restaurant = Restaurant.objects.create(
            user=self.user,
            name=f'Restaurant 1',
            country='CH',
            street='Strasse',
            city='Zurich',
            phone_number='+1234567890',
            opening_hours='24/7',
            price_level='HIGH',
        )
        Review.objects.create(
            content='test reviews',
            rating=1,
            user=self.other_user,
            restaurant=self.restaurant
        )

    def test_restaurant_reviews(self):
        self.authorize()
        response = self.client.get(self.get_url(**self.kwargs))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data), 1)
        self.assertEquals(Review.objects.first().content, 'test reviews')
        self.assertEquals(Review.objects.first().restaurant, self.restaurant)


class UserReviewsTests(MasterTestWrapper.BasicMasterTests):
    endpoint = 'api:reviews:user_reviews'
    methods = ['GET']

    def get_kwargs(self):
        return {
            'pk': self.user.id
        }

    def setUp(self):
        super().setUp()
        self.restaurant = Restaurant.objects.create(
            user=self.user,
            name=f'Restaurant 1',
            country='CH',
            street='Strasse',
            city='Zurich',
            phone_number='+1234567890',
            opening_hours='24/7',
            price_level='HIGH',
        )
        Review.objects.create(
            content='test reviews',
            rating=1,
            user=self.user,
            restaurant=self.restaurant
        )

    def test_user_reviews(self):
        self.authorize()
        response = self.client.get(self.get_url(**self.kwargs))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data), 1)
        self.assertEquals(Review.objects.first().content, 'test reviews')
        self.assertEquals(Review.objects.first().user, self.user)
