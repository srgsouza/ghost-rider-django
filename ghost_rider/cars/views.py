# Create your views here.
from django.shortcuts import render, redirect

from .models import Car, Comment
from .forms import CarForm, CommentForm

## API-related imports
from rest_framework import generics
from .serializers import CarSerializer, CommentSerializer

# Decorator.  Gets called before a function that has '@login_required' preceeding it.  
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
# To integrate built-in users
from django.contrib.auth.models import User
from cars.serializers import UserSerializer
from rest_framework import permissions, status
from cars.permissions import IsOwnerOrReadOnly

from django.middleware.csrf import get_token
from django.http import JsonResponse

###
class UserCreate(generics.ListCreateAPIView):
    """ 
    Creates the user. 
    """

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            print('serializer is valid!!')
            user = serializer.save()
            if user:
                return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_201_CREATED)
####

def get_csrf(request):
  token = get_token(request)
  return JsonResponse({'token': token})

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CarList(generics.ListCreateAPIView):
  # queryset = Car.objects.all().prefetch_related('user')
  queryset = Car.objects.all()
  serializer_class = CarSerializer
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
  # permission_classes = (permissions.AllowAny,)
  
  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

class CarDetail(generics.RetrieveUpdateDestroyAPIView):
  # queryset = Car.objects.all().prefetch_related('user')
  queryset = Car.objects.all()
  serializer_class = CarSerializer
  permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly) 
  # permission_classes = (permissions.AllowAny,)

class CommentList(generics.ListCreateAPIView):
  queryset = Comment.objects.all().prefetch_related('car')
  serializer_class = CommentSerializer
  permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly) 
  # permission_classes = (permissions.AllowAny,)
  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Comment.objects.all().prefetch_related('car')
  serializer_class = CommentSerializer
  permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly) 
  # permission_classes = (permissions.AllowAny,)

############################### CAR ###############################

# # @login_required
# def car_list(request):
#   cars = Car.objects.all()
#   return render(request, 'tunr/car_list.html', {'cars': cars})

# # Car Show
# # @login_required
# def car_detail(request, pk):
#   car = Car.objects.get(id=pk)
#   return render(request, 'tunr/car_detail.html', {'car': car})

# # Car Create
# # @login_required
# def car_create(request):
#   if request.method == 'POST':
#     form = CarForm(request.POST)
#     if form.is_valid():
#       car = form.save()
#       return redirect('car_detail', pk=car.pk)
#   else:
#     form = CarForm()
#   return render(request, 'tunr/car_form.html', {'form': form})

# # Car Edit

# def car_edit(request, pk):
#   car = Car.objects.get(pk=pk)
#   if request.method == 'POST':
#     form = CarForm(request.POST, instance=car)
#     if form.is_valid():
#       car = form.save()
#       return redirect('car_detail', pk=car.pk)
#   else:
#     form = CarForm(instance=car)
#   return render(request, 'tunr/car_form.html', {'form': form})

# # Car Delete

# def car_delete(request, pk):
#   Car.objects.get(id=pk).delete()
#   return redirect('car_list')

# ############################### COMMENT ###############################

# def comment_list(request):
#   comments = Comment.objects.all()
#   return render(request, 'tunr/comment_list.html', {'comments': comments})

# def comment_detail(request, id):
#   comment = Comment.objects.get(id=id)
#   return render(request, 'tunr/comment_detail.html', {'comment': comment})

# # Comment Create
# def comment_create(request):
#   if request.method == 'POST':
#     form = CommentForm(request.POST)
#     if form.is_valid():
#       comment = form.save()
#       return redirect('comment_detail', id=comment.id)
#   else:
#     form = CommentForm()
#   return render(request, 'tunr/comment_form.html', {'form': form})

#   # Comment Edit
# def comment_edit(request, id):
#   comment = Comment.objects.get(id=id)
#   if request.method == 'POST':
#     form = CommentForm(request.POST, instance=comment)
#     if form.is_valid():
#       comment = form.save()
#       return redirect('comment_detail', id=comment.id)
#   else:
#     form = CommentForm(instance=comment)
#   return render(request, 'tunr/comment_form.html', {'form': form})

# # Comment Delete
# def comment_delete(request, id):
#   Comment.objects.get(id=id).delete()
#   return redirect('comment_list')
