from . import exceptions as ex


class static_list(list):
    def format(self, name):
        try:
            for _ in self:
                for i, j in _.items():
                    _[i] = j.format(name)
            return self
        except AttributeError:
            raise ex.NotValidJson()


PYTHON = static_list(
    [
        {"folder": "{}"},
        {"file": "{}/__init__.py"},
        {"folder": "test"},
        {"file": "test/__init__.py"},
        {"file": "README.md"},
        {"file": "LICENSE"},
        {"file": "setup.py"},
        {"file": "setup.cfg"},
        {"file": "pyproject.toml"},
    ]
)

FLASK = static_list(
    [
        {"folder": "{}"},
        {"file": "{}/__init__.py"},
        {"file": "{}/db.py"},
        {"file": "{}/schema.py"},
        {"file": "{}/auth.py"},
        {"file": "{}/blog.py"},
        {"folder": "{}/templates"},
        {"file": "{}/templates/base.html"},
        {"folder": "{}/templates/auth/"},
        {"file": "{}/templates/auth/login.html"},
        {"file": "{}/templates/auth/register.html"},
        {"folder": "{}/blog"},
        {"file": "{}/blog/create.html"},
        {"file": "{}/blog/index.html"},
        {"file": "{}/blog/update.html"},
        {"folder": "{}/static"},
        {"file": "{}/static/style.css"},
        {"folder": "test"},
        {"file": "test/__init__.py"},
        {"file": "test/conftest.py"},
        {"file": "test/data.sql"},
        {"file": "test/test_db.py"},
        {"file": "test/test_auth.py"},
        {"file": "test/test_blog.py"},
        {"file": "README.md"},
        {"file": "LICENSE"},
        {"file": "setup.py"},
        {"file": "pyproject.toml"},
    ]
)

NODE_JS = static_list(
    [
        {"folder": "src"},
        {"folder": "src/api"},
        {"folder": "src/api/controllers"},
        {"folder": "src/api/controllers/user"},
        {"folder": "src/api/controllers/user/auth"},
        {"file": "src/api/controllers/user/auth/forgot-password.js"},
        {"file": "src/api/controllers/user/auth/login.js"},
        {"file": "src/api/controllers/user/auth/logout.js"},
        {"file": "src/api/controllers/user/auth/refresh-token.js"},
        {"file": "src/api/controllers/user/auth/register.js"},
        {"file": "src/api/controllers/user/auth/send-verification-code.js"},
        {"file": "src/api/controllers/user/auth/verify-email.js"},
        {"folder": "src/api/controllers/user/edit"},
        {"file": "src/api/controllers/user/edit/change-password.js"},
        {"file": "src/api/controllers/user/edit/edit-user.js"},
        {"file": "src/api/controllers/user/delete-user.js"},
        {"file": "src/api/controllers/user/get-user.js"},
        {"file": "src/api/controllers/user/index.js"},
        {"folder": "src/api/middlewares"},
        {"folder": "src/api/middlewares/auth"},
        {"file": "src/api/middlewares/auth/check-auth.js"},
        {"file": "src/api/middlewares/auth/check-authority.js"},
        {"file": "src/api/middlewares/image-upload.js"},
        {"file": "src/api/middlewares/index.js"},
        {"file": "src/api/middlewares/object-id-control.js"},
        {"file": "src/api/middlewares/rate-limiter.js"},
        {"folder": "src/api/routes"},
        {"file": "src/api/routes/index.js"},
        {"file": "src/api/routes/user.js"},
        {"folder": "src/api/validators"},
        {"file": "src/api/validators/index.js"},
        {"file": "src/api/validators/user.validator.js"},
        {"folder": "src/config"},
        {"file": "src/config/index.js"},
        {"folder": "src/loaders"},
        {"file": "src/loaders/index.js"},
        {"file": "src/loaders/express.js"},
        {"file": "src/loaders/mongoose.js"},
        {"folder": "src/models"},
        {"file": "src/models/index.js"},
        {"file": "src/models/log.js"},
        {"file": "src/models/token.js"},
        {"file": "src/models/user.js"},
        {"folder": "src/utils"},
        {"folder": "src/utils/helpers"},
        {"file": "src/utils/helpers/error-helper.js"},
        {"file": "src/utils/helpers/generate-random-code.js"},
        {"file": "src/utils/helpers/ip-helper.js"},
        {"file": "src/utils/helpers/jwt-token-helper.js"},
        {"file": "src/utils/helpers/local-text-helper.js"},
        {"folder": "src/utils/lang"},
        {"file": "src/utils/lang/en.json"},
        {"file": "src/utils/lang/get-text.json"},
        {"file": "src/utils/lang/tr.json"},
        {"file": "src/utils/index.js"},
        {"file": "src/utils/logger.js"},
        {"file": "src/utils/send-code-to-email.js"},
        {"file": "src/app.js"},
        {"file": ".env.sample"},
        {"file": "README.md"},
        {"file": "LICENSE"},
        {"file": "package.json"},
        {"file": "package-lock.json"},
    ]
)

templates = {
    "python": PYTHON,
    "node.js": NODE_JS,
    "flask": FLASK,
}
