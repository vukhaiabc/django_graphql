import graphene
import api.schema
import users.schema


class Query(api.schema.Query,users.schema.Query,graphene.ObjectType) :
    pass
class Mutation(api.schema.Mutation,users.schema.Mutation,graphene.ObjectType,):
    pass

schema = graphene.Schema(query=Query,mutation=Mutation)