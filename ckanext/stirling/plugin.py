import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import ckanext.stirling.helpers as h


class StirlingPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IActions)
    plugins.implements(plugins.IRoutes, inherit=True)

    # IConfigurer
    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'stirling')

    # IActions
    def get_actions(self):
        module_root = 'ckanext.stirling.logic.action'
        action_functions = h._get_functions(module_root)
        return action_functions

    # IRoutes
    def before_map(self, map):
        # Handle user index route to check if the user is sysadmin
        user_ctrl = 'ckanext.stirling.controllers.stirling:StirlingController'
        map.connect('user_index', '/user',
                    controller=user_ctrl, action='index')
        return map
