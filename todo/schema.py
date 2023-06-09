import graphene
from .models import Todo
from graphene_django import DjangoListField, DjangoObjectType


class TodoType(DjangoObjectType):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'date',)


class Query(graphene.ObjectType):
    todos = DjangoListField(TodoType, id=graphene.Int())

    def resolve_todos(self, info, id=None):
        if id:
            return Todo.objects.filter(id=id)
        return Todo.objects.all()


class CreateTodo(graphene.Mutation):
    todos = graphene.Field(TodoType)

    class Arguments:
        title = graphene.String(required=True)

    def mutate(self, info, title):
        todo = Todo(title=title)
        todo.save()
        return CreateTodo(todos=todo)


class UpdateTodo(graphene.Mutation):
    updatetodos = graphene.Field(TodoType)

    class Arguments:
        id = graphene.Int(required=True)
        title = graphene.String(required=True)

    def mutate(self, info, id, title):
        todo = Todo.objects.get(id=id)
        todo.title = title
        todo.save()
        return UpdateTodo(updatetodos=todo)


class DeleteTodo(graphene.Mutation):
    message = graphene.String()

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):
        todo = Todo.objects.get(id=id)
        todo.delete()
        return DeleteTodo(message=f"ID {id} id Deleted")


class Mutation(graphene.ObjectType):
    postTodo = CreateTodo.Field()
    updateTodo = UpdateTodo.Field()
    deleteTodo = DeleteTodo.Field()
