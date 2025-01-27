class DatabaseRouter:
    def db_for_read(self, model, **hints):
        if model._meta.db_table == 'users':
            return 'users_db'
        elif model._meta.db_table == 'products':
            return 'products_db'
        elif model._meta.db_table == 'orders':
            return 'orders_db'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.db_table == 'users':
            return 'users_db'
        elif model._meta.db_table == 'products':
            return 'products_db'
        elif model._meta.db_table == 'orders':
            return 'orders_db'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'data_insertion':
            if model_name == 'users':
                return db == 'users_db'
            elif model_name == 'products':
                return db == 'products_db'
            elif model_name == 'orders':
                return db == 'orders_db'
        return None