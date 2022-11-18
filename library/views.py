from django.http import JsonResponse
from rest_framework.generics import ListAPIView

from library.models import Book
from library.serializers import BookSerializer


class InfoViews(ListAPIView):
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        queryset = Book.objects.filter(owner_id=self.kwargs['pk'])
        response = []
        for ad in queryset:
            if not any(ad.owner.id == x['id'] for x in response):
                dict_ret={
                'id': ad.owner.id,
                'name': ad.owner.name,
                'books': [],
                }
                dict_ret['books'].append({'id': ad.id, 'name': ad.name_book})
                response.append(dict_ret)
            else:
                for i in response:
                    if ad.owner.id == i['id']:
                        i['books'].append({'id': ad.id, 'name': ad.name_book})

        return JsonResponse(response, safe=False)
