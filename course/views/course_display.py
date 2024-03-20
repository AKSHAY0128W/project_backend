from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..models import Course,Learning, Video

def course_create_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        slug = request.POST.get('slug')
        description = request.POST.get('description')
        price = request.POST.get('price')
        discount = request.POST.get('discount')
        thumbnail = request.FILES.get('thumbnail')
        resource = request.FILES.get('resource')
        learnings = request.POST.get('learnings')
        video_title = request.POST.get('video_title')
        video_serial = request.POST.get('video_serial')
        video_id = request.POST.get('video_id')
        video_preview = request.POST.get('video_preview') == 'true'


    
        course = Course( 
            name = name,
            slug = slug,
            description = description,
            price = price,
            discount = discount,
            thumbnail = thumbnail,
            resource = resource,
        )
        course.save()

        learningCount = int(request.POST.get('learning_count', 0))
        for i in range(1, learningCount + 1):
            learning = request.POST.get(f'learning_{i}')
            if learning:
                Learning.objects.create(
                    learning_description=learning,
                    course=course
                )

        learning = Learning(
            learning_description = learnings,
            course = course
        )
        learning.save()

        videoCount = int(request.POST.get('video_count', 0))
        for i in range(1, videoCount + 1):
            video_title = request.POST.get(f'video_title_{i}')
            video_serial = int(request.POST.get(f'video_serial_{i}'))
            video_id = request.POST.get(f'video_id_{i}')
            video_preview = request.POST.get(f'video_preview_{i}') == 'true'
            if video_title and video_serial and video_id:
                video = Video.objects.create(
                    title=video_title,
                    serial_number=video_serial,
                    video_id=video_id,
                    is_preview=video_preview,
                    course=course
                )

        # video = Video(
        #         title = video_title,
        #         serial_number = video_serial,
        #         video_id = video_id,
        #         is_preview = video_preview,
        #         course = course
        # )
        # video.save()
        print(video)
        
        return redirect('admin_course_create')

    return render(request, 'admin_course_create.html')

def course_list_view(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'admin_course_details.html', context)

def course_delete_view(request, id):
    Course.objects.filter(id=id).delete()
    return redirect('admin_course_details')


def course_update_view(request, id):
    course = Course.objects.get(id=id)
    if request.method == 'POST':
        course.name = request.POST.get('name')
        course.slug = request.POST.get('slug')
        course.description = request.POST.get('description')
        course.price = request.POST.get('price')
        course.discount = request.POST.get('discount')
        course.thumbnail = request.FILES.get('thumbnail')
        course.resource = request.FILES.get('resource')
        course.save()
        return redirect('admin_course_details')

    context = {
        'course': course
    }
    return render(request, 'admin_course_details.html', context)