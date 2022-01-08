import graphene
from graphene_django import DjangoObjectType
from graphql_auth.schema import UserQuery,MeQuery
from graphql_auth import mutations

class Query(UserQuery,MeQuery,graphene.ObjectType):
    pass
class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()
    update_account = mutations.UpdateAccount.Field()
    refresh_token = mutations.RefreshToken.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    send_password_reset_email = mutations.SendPasswordResetEmail.Field()
    password_reset = mutations.PasswordReset.Field()
class Mutation(AuthMutation,graphene.ObjectType):
    pass
# schema = graphene.Schema(query=Query,mutation= Mutation)