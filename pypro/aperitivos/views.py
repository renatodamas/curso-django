from django.shortcuts import render

# Create your views here.


class Video:
    def __init__(self, slug: str, titulo: str, youtube_id: str):
        self.slug = slug
        self.titulo = titulo
        self.youtube_id = youtube_id


videos = [
    Video('motivacao', 'Video Aperitivo: Motivação', '2aYplgJrPDU'),
    Video('instalacao-windows', 'Instalação Windows', 'htg7WHSbR00')
]

video_dct = {v.slug: v for v in videos}


def video(request, slug):
    video = video_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})
