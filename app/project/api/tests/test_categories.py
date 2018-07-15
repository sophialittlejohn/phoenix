from rest_framework import status

from project.api.tests.master_tests import MasterTestWrapper
from project.feed.models import Category


class ListCategoriesTests(MasterTestWrapper.BasicMasterTests):
    endpoint = 'api:categories:categories_list'
    methods = ['GET']

    def setUp(self):
        super().setUp()
        for i in range(5):
            Category.objects.create(
                name=f'Category {i}',
            )

    def test_all_categories_length(self):
        self.authorize()
        response = self.client.get(self.get_url())
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data), 5)
