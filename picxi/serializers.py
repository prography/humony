from rest_framework import serializers

from .models import InPic, OutPic

class InPicSerializer(serializers.ModelSerializer):
    class Meta:
        model = InPic
        fields = (
            'guidmodel_ptr_id',
            'created',
            'before'
        )

class OutPicSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutPic
        fields = (
            'guidmodel_ptr_id',
            'origin_id',
            'created',
            'after'
        )


