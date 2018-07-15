from rest_framework.exceptions import NotFound


class GetObjectMixin(object):
    @staticmethod
    def get_object_by_model(model, pk):
        try:
            obj = model.objects.get(pk=pk)
        except model.DoesNotExist:
            raise NotFound(f'Object not found with params {pk} on model {model.__name__}')
        return obj
