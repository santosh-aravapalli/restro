from restro_admin.models import StateModel,AreaModel
from rest_framework.serializers import ModelSerializer


class StateSerializer(ModelSerializer):

    class Meta:
        model = StateModel
        fields = ['state_no','state_name']

