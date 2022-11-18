from django.http import JsonResponse
from rest_framework.generics import ListAPIView

from library.models import Book
from library.serializers import BookSerializer


class InfoViews(ListAPIView):
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        queryset = Book.objects.filter(author_id=self.kwargs['pk'])
        response = []
        for book in queryset:
            if not any(book.author.id == x['id'] for x in response):
                dict_author = {
                    'id': book.author.id,
                    'name': book.author.name,
                    'books': [],
                }
                dict_author['books'].append({'id': book.id, 'name': book.name})
                response.append(dict_author)
            else:
                for i in response:
                    if book.author.id == i['id']:
                        i['books'].append({'id': book.id, 'name': book.name})

        return JsonResponse(response, safe=False)
