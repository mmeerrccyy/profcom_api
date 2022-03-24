from rest_framework import serializers
from . import models


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DirectionsModel
        fields = '__all__'


class WorkTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WorkTimeModel
        fields = '__all__'


class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DegreeModel
        fields = '__all__'


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ExperienceModel
        fields = '__all__'


class EnglishLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EnglishLevelModel
        fields = '__all__'


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VacancyModel
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['company_direction'] = DirectionSerializer(instance.company_direction).data
        response['working_time'] = WorkTimeSerializer(instance.working_time, many=True).data
        response['vacancy_degree'] = DegreeSerializer(instance.vacancy_degree, many=True).data
        response['working_experience'] = ExperienceSerializer(instance.working_experience, many=True).data
        response['minimal_english_level'] = EnglishLevelSerializer(instance.minimal_english_level).data
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


class AmountSerializer(serializers.Serializer):
    vacancy_amount = serializers.IntegerField()
    resume_amount = serializers.IntegerField()
