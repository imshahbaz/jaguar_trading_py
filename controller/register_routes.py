from controller.margin_controller import margin_routes


def register_controllers(app):
    margin_routes(app)
