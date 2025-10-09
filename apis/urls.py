from django.urls import path
from .views import book_request, register_user,login_user,delete_book,add_to_cart,check_out,save_for_later

urlpatterns = [
    path("books/", book_request, name="book-list"),
    path("register/", register_user, name="user-register"),
    path("login/", login_user, name="user-login"),
    path("add_to_cart/", add_to_cart, name="user-cart"),
    path("check_out/", check_out, name="user-checkout"),
    path("save_later/", save_for_later, name="user-savelater"),
    path("delete_book/", delete_book, name="delete-book"),
    
]