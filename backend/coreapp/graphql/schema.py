from graphene import relay, Schema, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from ..models import Scratch

class ScratchNode(DjangoObjectType):
    class Meta:
        model = Scratch
        filter_fields = ['name', 'score', 'max_score']
        interfaces = (relay.Node, )

class Query(ObjectType):
    scratch = relay.Node.Field(ScratchNode)
    scratches = DjangoFilterConnectionField(ScratchNode)

schema = Schema(query=Query)
