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
            info['spotify_id'] = album['id']
            info['title'] = album['name']
            info['artist'] = album['artists'][0]['name']

            obj, created = Album.objects.get_or_create(
                spotify_id=info['spotify_id'],
                defaults={
                    'title': info['title'],
                    'artist': info['artist']
                }
            )

            info['id'] = obj.id

            results.append(info)

        context = {
            'searched': searched,
            'results': results
        }

        return render(request, 'spotify/search.html', context)

    return render(request, 'spotify/search.html')
