from django.shortcuts import render
from .spotify_api import search_album
from reviews.models import Album


def search(request):
    """
    View to search for albums.
    """
    if request.method == 'POST':
        searched = request.POST['searched']
        search_results = search_album(searched)
        results = []
        for i, album in enumerate(search_results):
            info = {}
            info['id'] = album['id']
            info['name'] = album['name']
            info['artist'] = album['artists'][0]['name']
            info['release_date'] = album['release_date']
            query_set = Album.objects.filter(spotify_id=info['id']).first()
            if not query_set:
                new_album = Album(
                    name=info['name'],
                    artist=info['artist'],
                    spotify_id=info['id']
                )
                new_album.save()
            else:
                info['album_id'] = query_set.id
            results.append(info)

        context = {
            'searched': searched,
            'results': results
        }

        return render(request, 'spotify/search.html', context)

    return render(request, 'spotify/search.html')
