from django.views.generic import TemplateView


class AppView(TemplateView):
    template_name = 'management/index.html'
    page = "management/btn_and_popup_{}.html".format('app')
    category =  ['Name', 'Flavor', 'IP Address', 'Actions']

    def get(self, request, *args, **kwargs):
        table = {
            'category': self.category,
            'rows': []
        }
        return self.render_to_response({
            'table': table,
            'page': self.page
        })

    def post(self, request, *args, **kwargs):
        table = {
            'category': self.category,
            'rows': []
        }
        return self.render_to_response({
            'table': table,
            'page': self.page
        })


class NetworkView(TemplateView):
    template_name = 'management/index.html'
    page = "management/btn_and_popup_{}.html".format('network')
    category = ['Subnet ID', 'Name', 'CIDR', 'Provider', 'Security_group', 'Actions']

    def get(self, request, *args, **kwargs):
        table = {
            'category': self.category,
            'rows': []
        }
        return self.render_to_response({
            'table': table,
            'page': self.page
        })

    def post(self, request, *args, **kwargs):
        table = {
            'category': self.category,
            'rows': []
        }
        return self.render_to_response({
            'table': table,
            'page': self.page
        })


class ProviderView(TemplateView):
    template_name = 'management/index.html'
    page = "management/btn_and_popup_{}.html".format('provider')
    category = ['Name', 'Cloud Config', 'Actions']

    def get(self, request, *args, **kwargs):
        table = {
            'category': self.category,
            'rows': []
        }
        return self.render_to_response({
            'table': table,
            'page': self.page
        })

    def post(self, request, *args, **kwargs):
        table = {
            'category': self.category,
            'rows': []
        }
        return self.render_to_response({
            'table': table,
            'page': self.page
        })


class AboutView(TemplateView):
    template_name = 'management/about.html'

    def get(self, request, *args, **kwargs):
        return self.render_to_response({})