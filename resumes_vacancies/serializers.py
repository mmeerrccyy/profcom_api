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
    company_direction = serializers.SlugRelatedField(slug_field='direction', read_only=True)
    working_time = serializers.SlugRelatedField(slug_field='work_time', read_only=True, many=True)
    vacancy_degree = serializers.SlugRelatedField(slug_field='degree', read_only=True, many=True)
    working_experience = serializers.SlugRelatedField(slug_field='experience', read_only=True, many=True)
    minimal_english_level = serializers.SlugRelatedField(slug_field='level', read_only=True)

    class Meta:
        model = models.VacancyModel
        fields = '__all__'


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
