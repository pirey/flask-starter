from marshmallow import Schema, fields as f, validate as v, ValidationError, EXCLUDE


class AdminUserSchema(Schema):
    id = f.Integer()
    username = f.String(required=True, validate=v.Length(max=100))
    password = f.String(required=True, load_only=True,
                        validate=v.Length(max=100))
    status = f.Integer()


admin_user = AdminUserSchema(exclude=['password'])
admin_user_create = AdminUserSchema(only=['username', 'password'])
admin_user_update = AdminUserSchema(
    only=['username', 'password', 'status'])


class AdminUserLoginSchema(Schema):
    username = f.String(required=True, validate=v.Length(max=100))
    password = f.String(required=True, load_only=True,
                        validate=v.Length(max=100))


admin_user_login = AdminUserLoginSchema(only=['username', 'password'])


class AdminUserLoginResponseSchema(Schema):
    admin_user = f.Nested(admin_user)
    token = f.String(dump_only=True)


admin_user_login_response = AdminUserLoginResponseSchema()
