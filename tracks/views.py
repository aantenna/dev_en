from django.shortcuts import render

def сategories(request):
    context = {
        'title': 'Home - Категории',
        'tracks': [
            {'image': 'deps/images/tracks/melody.jpg',
             'title': 'MELODY',
             'artist': 'ASH ISLAND',
             'album': 'ISLAND',
             'score': 5.00},

            {'image': 'deps/images/tracks/friends.jpg',
             'title': 'FRI(END)S',
             'artist': 'V',
             'album': 'FRI(END)S - Single',
             'score': 5.00},

            {'image': 'deps/images/tracks/mejdynami.jpg',
             'title': 'Между Нами',
             'artist': 'Lizer',
             'album': 'Не Ангел',
             'score': 4.00},

            {'image': 'deps/images/tracks/musicgromche.jpg',
             'title': 'Музыка громче',
             'artist': 'BUSHIDO ZHO',
             'album': 'WESTGOTHS',
             'score': 3.00},

            {'image': 'deps/images/tracks/slowdancing.jpg',
             'title': 'Slow Dancing',
             'artist': 'V',
             'album': 'Layover',
             'score': 5.00},

            {'image': 'deps/images/tracks/ciao.jpg',
             'title': 'Ciao',
             'artist': 'kirkiimad',
             'album': 'Ciao - Single',
             'score': 4},

            {'image': 'deps/images/tracks/dday.jpg',
             'title': 'D-DAY',
             'artist': 'Agust D',
             'album': 'D-Day',
             'score': 4.90},

            {'image': 'deps/images/tracks/shosse.jpg',
             'title': 'ШОССЕ',
             'artist': 'f0lk',
             'album': 'EVERYTHING DIES',
             'score': 3.90},

            {'image': 'deps/images/tracks/night.jpg',
             'title': 'ночь',
             'artist': 'MAYOT',
             'album': 'ОБА',
             'score': 4.00},

            {'image': 'deps/images/tracks/dosihpor.jpg',
             'title': 'до сих пор',
             'artist': 'MAYOT',
             'album': 'ОБА',
             'score': 4.00},

            {'image': 'deps/images/tracks/svet.jpg',
             'title': 'Замигает свет',
             'artist': 'KENTUKKI',
             'album': 'Замигает свет - Single',
             'score': 5.00},

            {'image': 'deps/images/tracks/doobeda.jpg',
             'title': 'ДО ОБЕДА',
             'artist': '104',
             'album': 'КИНО БЕЗ СИГАРЕТ',
             'score': 4.00},
        ],
    }
    return render(request, 'tracks/categories.html', context)


def track(request):
    return render(request, 'tracks/track.html')
