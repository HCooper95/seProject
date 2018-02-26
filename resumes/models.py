from django.conf import settings
from django.db import models


class Resume(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    @property
    def sections(self):
        return ResumeSection.objects.filter(resume=self)


class ResumeSection(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)


class Experience(ResumeSection):
    title = models.CharField(max_length=150, blank=False)
    start_month_year = models.CharField(max_length=4, blank=False)
    end_month_year = models.CharField(max_length=4, blank=False)

    def __str__(self):
        return '{} - {} {}'.format(self.title, self.start_month_year, self.end_month_year)


class Education(ResumeSection):
    school = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return '{}'.format(self.school)


class Skills(ResumeSection):
    skill = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.skill


class Awards(ResumeSection):
    award = models.CharField(max_length=255, blank=True)
    year = models.IntegerField(blank=True)

    def __str__(self):
        return '{} - {}'.format(self.award, str(self.year))
