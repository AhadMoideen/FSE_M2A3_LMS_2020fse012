class NotificationDBRouter(object):

    def db_for_read(self, model, **hints):
        "Point all operations on app1 models to 'db_app1'"
        from django.conf import settings
        if 'notification_db' not in settings.DATABASES:
            return None
        if model._meta.app_label == 'notification_service':
            return 'notification_db'
        return None

    def db_for_write(self, model, **hints):
        "Point all operations on app1 models to 'db_app1'"
        from django.conf import settings
        if 'notification_db' not in settings.DATABASES:
            return None
        if model._meta.app_label == 'notification_service':
            return 'notification_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a model in app1 is involved"
        from django.conf import settings
        if 'notification_db' not in settings.DATABASES:
            return None
        if obj1._meta.app_label == 'notification_service' or obj2._meta.app_label == 'notification_service':
            return True
        return None

    def allow_syncdb(self, db, model):
        "Make sure the app1 app only appears on the 'app1' db"
        from django.conf import settings
        if 'notification_db' not in settings.DATABASES:
            return None
        if db == 'notification_db':
            return model._meta.app_label == 'notification_service'
        elif model._meta.app_label == 'notification_service':
            return False
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db == 'notification_db':
            return app_label == 'notification_service'
        elif app_label == 'notification_service':
            return False
        return None
