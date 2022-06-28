from django.shortcuts import render

# Create your views here.

videos = [
    {'slug': 'motivacao', 'titulo': 'Video Aperitivo: Motivação', 'youtube_id': '2aYplgJrPDU'},
    {'slug': 'instalacao-windows', 'titulo': 'Instalação Windows', 'youtube_id': 'htg7WHSbR00'}
]

video_dct = {dct['slug']: dct for dct in videos}


def video(request, slug):
    video = video_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})
