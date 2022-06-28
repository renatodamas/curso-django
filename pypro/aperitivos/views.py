from django.shortcuts import render

# Create your views here.


def video(request, slug):
    video = {
        'titulo': 'Video Aperitivo: Motivação',
        'id': '2aYplgJrPDU'
    }
    return render(request, 'aperitivos/video.html', context={'video': video})
