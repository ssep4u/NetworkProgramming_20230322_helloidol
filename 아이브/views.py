from django.shortcuts import render


def show_원영(request):
    context = {
        'name': '장원영',
        'img_src': 'https://images.khan.co.kr/article/2023/02/09/news-p.v1.20230209.b6b89ecfb36e41dc945fd92e9114751b_P1.jpg',
    }
    return render(request, '아이브/멤버.html', context=context)


def show_유진(request):
    context = {
        'name': '안유진',
        'img_src': 'https://img.sbs.co.kr/newsnet/etv/upload/2022/08/01/30000780359_1280.jpg',
    }
    return render(request, '아이브/멤버.html', context=context)
