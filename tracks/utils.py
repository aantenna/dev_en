from django.db.models import Q
from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank,
    SearchHeadline,
)

from tracks.models import Tracks


# Полнотекстовый поиск
def q_search(query):

    if query.isdigit() and len(query) <= 5:
        return Tracks.objects.filter(id=int(query))

    vector = SearchVector("title", "genre__name") # , "artist"
    query = SearchQuery(query)

    result = (
        Tracks.objects.annotate(rank=SearchRank(vector, query))
        .filter(rank__gt=0)
        .order_by("-rank")
    )

    result = result.annotate(
        headline=SearchHeadline(
            "title",
            query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel="</span>",
        )
    )


    return result

    # result = result.annotate(
    #     bodyline=SearchHeadline(
    #         "description",
    #         query,
    #         start_sel='<span style="background-color: yellow;">',
    #         stop_sel="</span>",
    #     )
    # )


    # keywords = [word for word in query.split() if len(word) > 2]

    # q_objects = Q()

    # for token in keywords:
    #     q_objects |= Q(description__icontains=token)
    #     q_objects |= Q(name__icontains=token)

    # return Products.objects.filter(q_objects)
