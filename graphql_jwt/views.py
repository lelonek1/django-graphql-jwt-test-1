import pickle
from django.http import HttpResponse
from django.views import View
class MyVulnerableView(View):

    def insecure_deserialization_view(request):
        user_data = request.GET.get('data')
        deserialized_data = pickle.loads(user_data.encode('latin1'))
        return HttpResponse(f"Deserialized data: {deserialized_data}")
