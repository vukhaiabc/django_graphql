import graphene
from graphene_django import DjangoObjectType, DjangoListField
from .models import CategoryProduct,Product,Rating

class ProductType(DjangoObjectType):
    class Meta :
        model = Product
        fields = '__all__'
        # fields = ['id','name','price','category']

    rating = graphene.Int()
    def resolve_rating(self, info):
        return 5

    @classmethod
    def get_queryset(cls, queryset, info):
        return Product.objects.filter(is_active=True)
class CategoryProductType(DjangoObjectType):
    class Meta :
        model = CategoryProduct
        fields = "__all__"

    @classmethod
    def get_queryset(cls, queryset, info):
        return CategoryProduct.objects.filter(is_active=True)
class Query(graphene.ObjectType):
    all_products = graphene.List(ProductType)
    products_by_name = graphene.List(ProductType,name=graphene.String())
    product_by_id = graphene.Field(ProductType,id=graphene.Int())
    all_category = DjangoListField(CategoryProductType)

    def resolve_all_products(self,info):
        return Product.objects.filter(is_active=True)
    def resolve_products_by_name(self,info,name):
        products = Product.objects.filter(is_active = True ,name__icontains = name)
        return products
    def resolve_product_by_id(self,info,id):
        try :
            product = Product.objects.get(pk=id,is_active=True)
        except Product.DoesNotExist :
            raise Exception('Không tìm thấy Sản Phẩm')
        return product

# schema = graphene.Schema(query=Query)