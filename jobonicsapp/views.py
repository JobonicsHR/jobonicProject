from .models import Industry, Profession, JobStatus, JobType, Country, ApplicationStage, EntitySize
from .serializers import IndustrySerializer, ProfessionSerializer, JobStatusSerializer, JobTypeSerializer, UserSerializer, CountrySerializer, ApplicationStageSerializer, EntitySizeSerializer
from rest_framework import generics, permissions
from jobonicusers.models import JobonicUser as User

# this is just for the holder
from django.http import HttpResponse

# Create your views here.

def index(request):
    content = '''

    <b>jobonicsapp</b><br />
    <a href="industries">/industries/</a><br />
    /industries/[int]<br />
    <a href="users">/users/</a><br />
    /users/[int]<br />
    <a href="professions">/professions/</a><br />
    <a href="jobtypes">/jobtypes/</a><br />
    <a href="countries">/countries/</a><br />
    <a href="entity-sizes">/entity-sizes/</a><br />
    <a href="app-stages">/app-stages/</a><br />
    <hr />
    <b>jobonicsuser</b><br />
    
    '''
    return HttpResponse(content)


class IndustryList(generics.ListCreateAPIView):

    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ProfessionList(generics.ListCreateAPIView):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class JobTypeList(generics.ListCreateAPIView):
    queryset = JobType.objects.all()
    serializer_class = JobTypeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class JobStatusList(generics.ListCreateAPIView):
    queryset = JobStatus.objects.all()
    serializer_class = JobStatusSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class CountryList(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class EntitySizeList(generics.ListCreateAPIView):
    queryset = EntitySize.objects.all()
    serializer_class = EntitySizeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ApplicationStageList(generics.ListCreateAPIView):
    queryset = ApplicationStage.objects.all()
    serializer_class = ApplicationStageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class IndustryDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ProfessionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class JobTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobType.objects.all()
    serializer_class = JobTypeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class JobStatusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobStatus.objects.all()
    serializer_class = JobStatusSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CountryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class EntitySizeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EntitySize.objects.all()
    serializer_class = EntitySizeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ApplicationStageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ApplicationStage.objects.all()
    serializer_class = ApplicationStageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
