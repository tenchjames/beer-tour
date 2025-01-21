from pages import Pages


class Router():
    def __init__(self):
        self.routes = {}
        self.stack = []

    def add_route(self, page, component):
        self.routes[page] = component

    def back(self):
        if len(self.stack) == 0 or len(self.stack) == 1:
            return
        self.stack.pop()
        path, props = self.stack[-1]
        self.navigate(path, props)

    def navigate(self, page, props=None):
        if page == Pages.EXIT:
            self.stack = []
            return
        component = self.routes.get(page)
        if component is None:
            print(f"Route {page} not found")
            return
        prior_page = None
        if len(self.stack) > 0:
            prior_page, prior_params = self.stack[-1]

        if prior_page is not None and prior_page != page:
            prior_component = self.routes.get(prior_page)
            prior_component.close()

        component.changes(props)
        self.stack.append((page, props))

    def execute(self):
        if len(self.stack) == 0:
            return
        component = self.routes.get(self.stack[-1][0])
        component.execute()
