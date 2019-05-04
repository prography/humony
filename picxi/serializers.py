from rest_framework import serializers

from .models import InPic, OutPic, SegPic

class InPicSerializer(serializers.ModelSerializer):
    class Meta:
        model = InPic
        fields = (
            'guidmodel_ptr_id',
            'created',
            'before'
        )
class SegPicSerializer(serializers.ModelSerializer):
    class Meta:
        model = SegPic
        fields = (
            'guidmodel_ptr_id',
            'origin_id',
            'created',
            'ing'
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


