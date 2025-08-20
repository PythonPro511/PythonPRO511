from ClassShoppingCart.ClassShoppingCart import ShoppingCart

if __name__ == '__main__':
    cart1 = ShoppingCart()
    cart1.add_item('Яблоки', 50, 2)
    cart1.add_item('Молоко', 80, 1)
    cart2 = ShoppingCart()
    cart2.add_item("Хлеб", 40, 1)

    print(cart1)
    print(len(cart1))

    combined_cart = cart1 + cart2
    print(combined_cart)
    combined_cart.remove_item('Молоко')
    print(combined_cart)