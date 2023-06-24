from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, text, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


#user data
class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    phone_no = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

class Country(Base):
    __tablename__ = 'country'

    id= Column(Integer, primary_key=True, nullable=False)
    country_name = Column(String, nullable=False)

class Address(Base):
    __tablename__ = 'address'

    id= Column(Integer, primary_key=True, nullable=False)
    unit_number = Column(String, nullable=False)
    street_number = Column(String, nullable=False)
    address_line_1= Column(String, nullable=False)
    address_line_2= Column(String, nullable=True)
    city = Column(String, nullable=False)
    region = Column(String, nullable=False)
    postal_code = Column(String, nullable=True, server_default="")
    country = Column(Integer,ForeignKey("country.id", ondelete="CASCADE") ,nullable=False)

class UserAddress(Base):
    __tablename__ = 'user_address'

    id = Column(Integer, primary_key=True, nullable=False)  
    users_id = Column(Integer,ForeignKey("users.id", ondelete="CASCADE"),nullable=False)
    address_id = Column(Integer,ForeignKey("address.id", ondelete="CASCADE"),nullable=False)
    is_default = Column(Boolean, nullable=True)


# #Products Data

class Products(Base):
    __tablename__ = 'products'

    id= Column(Integer, primary_key=True, nullable=False)
    # category_id = Column(Integer, ForeignKey("product_category.id", ondelete="CASCADE"), nullable=False)
    name = Column(String, nullable=False)
    description= Column(String, nullable= False)
    product_image= Column(String, nullable=True)
    qty_in_stock = Column(Integer, nullable=False)
    price = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))


#having both these tables with identical colums seems like a very obvious stupid mistake. Revisit on a later date
class ProductItems(Base):
    __tablename__ = 'product_items'

    id= Column(Integer, primary_key=True, nullable=False)
    product_id = Column(Integer,ForeignKey("products.id", ondelete="CASCADE") ,nullable=False)
    qty_in_stock = Column(Integer, nullable=False)
    product_image = Column(String, nullable=True)
    price = Column(String, nullable=False)

# # class ProductCategory(Base):
# #     __tablename__ = 'product_category'
# #     id= Column(Integer, primary_key=True, nullable=False)
# #     parent_category_id = Column(Integer,ForeignKey("product_category.id", ondelete="CASCADE") ,nullable=False)
# #     category_name = Column(String,nullable=False)

# # class Variation(Base):
# #     __tablename__ = 'variation'

# #     id = Column(Integer, primary_key=True, nullable=False)
# #     category_id = Column(Integer, ForeignKey("product_category.id", ondelete="CASCADE"), nullable=False)
# #     name = Column(String, nullable=False)

# # class VariationOption(Base):
# #     __tablename__ = 'variation_option'

# #     id = Column(Integer, primary_key=True, nullable=False)
# #     category_id = Column(Integer, ForeignKey("variation.id", ondelete="CASCADE"), nullable=False)
# #     value = Column(String, nullable=False)


# # class ProductConfiguration(Base):
# #     __tablename__ = 'product_configuration'
# #     id = Column(Integer, primary_key=True, nullable=False)
# #     product_item_id =  Column(Integer,ForeignKey("product_items.id", ondelete="CASCADE") ,nullable=False)
# #     variation_option_id =  Column(Integer,ForeignKey("variation_option.id", ondelete="CASCADE") ,nullable=False)


class ShoppingCart(Base):
    __tablename__ = 'shopping_cart'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer,ForeignKey("users.id", ondelete="CASCADE") ,nullable=False)


class ShoppingCartItem(Base):
    __tablename__ = 'shopping_cart_item'

    id= Column(Integer, primary_key=True, nullable=False,)
    cart_id = Column(Integer,ForeignKey("shopping_cart.id", ondelete="CASCADE") ,nullable=False)
    product_item_id = Column(Integer,ForeignKey("product_items.id", ondelete="CASCADE") ,nullable=False)
    qty = Column(Integer, nullable=False)
    added_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))


# class ShopOrder(Base):
#     __tablename__= 'shop_order'

#     id= Column(Integer, primary_key=True, nullable=False,)
#     user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
#     order_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     payment_method_id = Column(Integer, ForeignKey('user_payment_method.id', ondelete='CASCADE',), nullable=False)
#     shipping_address = Column(Integer,ForeignKey("address.id", ondelete="CASCADE") ,nullable=False)
#     shipping_method = Column(Integer,ForeignKey("shipping_method.id", ondelete="CASCADE") ,nullable=False)
#     order_total = Column(Integer, nullable=False)
#     order_status = Column(Integer, ForeignKey('order_status.id', ondelete='CASCADE'), nullable=False)


# class OrderStatus(Base):
#     __tablename__ = 'order_status'

#     id= Column(Integer, primary_key=True, nullable=False,)
#     status = Column(String, nullable=False)


# class ShippingMethod(Base):
#     __tablename__ = 'shipping_method'
#     id = Column(Integer, primary_key=True, nullable=False,)
#     name = Column(String, nullable=False)
#     price = Column(String, nullable=False)


# class OrderLine(Base):
#     __tablename__ = 'order_line'
    
#     id = Column(Integer, primary_key=True, nullable=False,)
#     product_item_id = Column(Integer, ForeignKey('product_items.id', ondelete='CASCADE'), nullable=False)
#     order_id = Column(Integer, ForeignKey('shop_order.id', ondelete='CASCADE'), nullable=False)
#     qty = Column(Integer, nullable=False)
#     price = Column(String, nullable=False)

# class UserPaymentMethod(Base):
#     __tablename__ = 'user_payment_method'

#     id = Column(Integer, primary_key=True, nullable=False,)
#     user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
#     payment_type_id = Column(Integer, ForeignKey('payment_type.id', ondelete='CASCADE'))
#     provider = Column(String, nullable=False)
#     account_number = Column(String, nullable=False)
#     expiry_date = Column(TIMESTAMP(timezone=True), nullable=False)
#     is_default = Column(String, nullable=True)

# class PaymentType(Base):
#     __tablename__ = 'payment_type'

#     id = Column(Integer, primary_key=True, nullable=False,)
#     value = Column(String)


# class UserReview(Base):
#     __tablename__ = 'user_review'

#     id = Column(Integer, primary_key=True, nullable=False)
#     user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
#     ordered_product_id = Column(Integer, ForeignKey('order_line.id', ondelete='CASCADE'), nullable=False)
#     rating_value = Column(Integer, nullable=True)
#     comment= Column(String, nullable=True)