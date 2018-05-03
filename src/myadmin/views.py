from importlib import import_module


def target(request, controller_name='home', action_name='index'):
    controller = import_module('myadmin.controller.%s' % (controller_name))
    action = getattr(controller, action_name)
    return action(request)
