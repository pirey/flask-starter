from marshmallow import Schema, fields as f, validate as v, ValidationError, EXCLUDE


class AdminUserSchema(Schema):
    id = f.Integer()
    username = f.String(required=True, validate=v.Length(min=3, max=100))
    password = f.String(required=True, load_only=True,
                        validate=v.Length(min=4, max=100))
    status = f.Integer()


admin_user = AdminUserSchema(exclude=['password'])
admin_user_create = AdminUserSchema(only=['username', 'password'])
admin_user_update = AdminUserSchema(
    only=['username', 'password', 'status'])


class AdminUserLoginSchema(Schema):
    username = f.String(required=True)
    password = f.String(required=True, load_only=True)


admin_login = AdminUserLoginSchema()
