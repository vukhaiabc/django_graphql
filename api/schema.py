import graphene
from graphene_django import DjangoObjectType,DjangoListField
from .models import Author,Category,Book
from graphene_django.filter import DjangoFilterConnectionField
from graphql_jwt.decorators import login_required

class CategoryType(DjangoObjectType):
    class Meta :
        model = Category
        fields = ['id','name','books']
    des = graphene.String()
    def resolve_des(self,info):
        return "Danh Mục Sản Phẩm"
    @classmethod
    def get_queryset(cls, queryset, info):
        #co the thuc hien lay data theo yeu cau, test lay all()
        return Category.objects.all()
class AuthorNode(DjangoObjectType):
    class Meta :
        model = Author
        filter_fields = {
            'id' : [],
            'name' : ['exact','icontains','istartswith'],
            'books' : [],
        }
        interfaces = (graphene.relay.Node,)
        # fields = ['id','name','email','books']
class BookType(DjangoObjectType):
    class Meta :
        model = Book
        fields =['id','name','headline','category','authors','rating']

class Query(graphene.ObjectType):
    books = graphene.List(BookType,id = graphene.ID(),name = graphene.String())
    # all_category = DjangoListField(CategoryType)
    all_authors = DjangoFilterConnectionField(AuthorNode)

    def resolve_books(self,info,id=None,name = None):
        books =  Book.objects.select_related('category').all().prefetch_related('authors')

        if id is not None :
            try:
                books = books.get(pk = id)
            except Book.DoesNotExist :
                pass
        if name is not None :
            books = books.filter(name__icontains = name)
        return books
    # def resolve_all_category(self,info):
    #     return Category.objects.all()

class UpdateCategoryMutation(graphene.Mutation):
    category = graphene.Field(CategoryType)
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=True)

    @classmethod
    def mutate(cls,root,info,id,name):
        try :
            category = Category.objects.get(pk = id)
            category.name = name
            category.save()
            return UpdateCategoryMutation(category = category)
        except Category.DoesNotExist :
            return None
class CreateCategoryMutation(graphene.Mutation):
    category = graphene.Field(CategoryType)
    class Arguments:
        name = graphene.String()
    @classmethod
    @login_required
    def mutate(cls,root,info,name):
        category = Category(name = name)
        category.save()
        return CreateCategoryMutation(category=category)

class DelateCategoryMutation(graphene.Mutation):
    message = graphene.String()
    class Arguments :
        id = graphene.Int(required= True)

    @classmethod
    def mutate(cls,root,info,id):
        try :
            category = Category.objects.get(pk=id)
            category.delete()
            return DelateCategoryMutation(message= f"Xóa Thành Công id: {id}")
        except Category.DoesNotExist :
            return DelateCategoryMutation(message ="Không tìm thấy id")

class Mutation(graphene.ObjectType):
    update_category = UpdateCategoryMutation.Field()
    create_category = CreateCategoryMutation.Field()
    delete_category = DelateCategoryMutation.Field()
