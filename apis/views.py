from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Book, Cart, IssuedBook, SavedBook
from .serializers import BookSerializer
from .serializers import UserRegistrationSerializer,LoginSerializer,CartSerializer,IssuedBookSerializer,SavedBookSerializer
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes,authentication_classes
from rest_framework.authentication import TokenAuthentication,BaseAuthentication
from .permissions import RoleAccessPermission


# Create your views here.
@api_view(["GET", "POST", "PUT", "PATCH"])
# @permission_classes([IsAuthenticated, RoleAccessPermission])
def book_request(request):

    #   Get all books api call
    if request.method == "GET":
        sort_by = request.data.get('sort_by', None)
        books = Book.objects.all()
        if sort_by == 'most_issued':
            books = books.order_by('-issued_count')
        elif sort_by == 'least_issued':
            books = books.order_by('issued_count')
        
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
       


    #   Create a new book api call / adding a new book
    elif request.method == "POST":
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
          
            print(data)
        
            return Response(serializer.data, status=201)
        print("######")
        return Response(serializer.errors, status=400)

    #    put method
    elif request.method == "PUT":
        book_id = request.data.get("id")
        book = Book.objects.get(id=book_id)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    # {
    #     'id': 1,
    #     "author": "New Author",
    #     "title": "New Title"
    # }
    # {
    #     'id' : 1,
    #     "author": "Updated Author",
    # }

    # Patch method partial update
    elif request.method == "PATCH":
        book_id = request.data.get("id")
        book = Book.objects.get(id=book_id)
        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([BaseAuthentication])
def delete_book(request):
  if request.method == "DELETE":  
    book_id = request.data.get("id")
    if not book_id:
        return Response({'error': 'Book ID is required'}, status=400)
    print("Book id to delete:", book_id)
    try:
        book = Book.objects.get(id=book_id)
        book.delete()
        return Response({'message': 'Book deleted successfully'}, status=200)
    except Book.DoesNotExist:
        return Response({'error': 'Book not found'}, status=404)
    
    
# User Registration API
@api_view(["POST"])
def register_user(request):
    if request.method == "POST":
        data = request.data
        serializer = UserRegistrationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(["POST"])
def login_user(request):
    if request.method == "POST":
        data = request.data
        serializer = LoginSerializer(data=data)
       
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        
        username= serializer.validated_data['username']
        password= serializer.validated_data['password']
        print(serializer.data)
        authuser = authenticate(username=username, password= password)
        print("auth user = ",authuser)
        # token = Token.objects.create(user=authuser)
        # print(token.key)
        
        if authuser is not None:
            token , _ = Token.objects.get_or_create(user=authuser)
            return Response({"message": "Login successful","token":token.key}, status=200)
        else:
            return Response({"error": "Invalid credentials"}, status=400)


@api_view(["POST"])        
def add_to_cart(request):
        data = request.data.copy()
        if request.user.is_authenticated :
            data['user'] = request.user.id

        serializer = CartSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    
    
@api_view(["POST"])    
@permission_classes([IsAuthenticated])
def check_out(request):
       
        cart_items = Cart.objects.filter(user=request.user)
        if not cart_items:
            return Response({'error': 'Cart is empty'}, status=400)

        issued_books = []
        total = 0
        for item in cart_items:
            issue = IssuedBook.objects.create(
                user=request.user,
                # user_id=user_id, # remove this line after authentication
                book=item.book,
                return_date=timezone.now() + timedelta(days=14),
                bill_amount=item.book.price
            )
            item.book.issued_count += 1
            item.book.save()
            issued_books.append(issue)
            total += item.book.price
            item.delete()

        serializer = IssuedBookSerializer(issued_books, many=True)
        return Response({
            'issued_books': serializer.data,
            'total_bill': total
        })
        
        
@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([BaseAuthentication])
def save_for_later( request):
    
    data = request.data.copy()
    
    # if request.user.is_authenticated :
    data['user'] = request.user.id
        
    serializer = SavedBookSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)     
        