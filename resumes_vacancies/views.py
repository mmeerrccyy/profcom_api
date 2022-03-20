from rest_framework import views, generics
from rest_framework.response import Response
# from djqscsv import render_to_csv_response
from . import models, serializers


class GetDirectionsAPIView(generics.ListAPIView):
    queryset = models.DirectionsModel.objects.all()
    serializer_class = serializers.DirectionSerializer


class GetWorkTimeAPIView(generics.ListAPIView):
    queryset = models.WorkTimeModel.objects.all()
    serializer_class = serializers.WorkTimeSerializer


class GetDegreeAPIView(generics.ListAPIView):
    queryset = models.DegreeModel.objects.all()
    serializer_class = serializers.DegreeSerializer


class GetExperienceAPIView(generics.ListAPIView):
    queryset = models.ExperienceModel.objects.all()
    serializer_class = serializers.ExperienceSerializer


class GetEnglishLevelAPIView(generics.ListAPIView):
    queryset = models.EnglishLevelModel.objects.all()
    serializer_class = serializers.EnglishLevelSerializer


class VacancyAPIView(generics.ListCreateAPIView):
    queryset = models.VacancyModel.objects.all()
    serializer_class = serializers.VacancySerializer

    # def get(self, request):
    #     # qs = models.VacancyModel.get_for_yesterday()
    #     # serializer = serializers.VacancySerializer(qs, many=True)
    #     # return render_to_csv_response(qs)
    #     qs = models.VacancyModel.objects.all()
    #     serializer = serializers.VacancySerializer(qs, many=True)
    #     return Response(serializer.data)


class ResumeAPIView(generics.ListCreateAPIView):
    queryset = models.ResumeModel.objects.all()
    serializer_class = serializers.ResumeSerializer


class AmountVacancyResumeAPIView(views.APIView):
    @staticmethod
    def get(request):
        vacancy_amount = models.VacancyModel.objects.all().count()
        resume_amount = models.ResumeModel.objects.all().count()
        data = {'vacancy_amount': vacancy_amount, 'resume_amount': resume_amount}
        serializer = serializers.AmountSerializer(data=data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response({'Bad Request'})
