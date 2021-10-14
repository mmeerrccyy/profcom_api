from rest_framework import serializers
from . import models


class WorkTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WorkTimeModel
        fields = '__all__'


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VacancyModel
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['company_direction'] = DirectionSerializer(instance.company_direction).data
        return response


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ResumeModel
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['students_direction'] = DirectionSerializer(instance.students_direction).data
        # response['students_work_time'] = WorkTimeSerializer(instance.students_work_time).data
        return response


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DirectionsModel
        fields = '__all__'


class AmountSerializer(serializers.Serializer):
    vacancy_amount = serializers.IntegerField()
    resume_amount = serializers.IntegerField()
