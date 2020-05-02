from django.db import models

setting_kinds = (
    ('text', 'Text'),
    ('number', 'Number'),
    ('boolean', 'Boolean'),
    ('paragraph', 'Paragraph'),
)


class AppSetting(models.Model):
    name = models.CharField(max_length=128)
    kind = models.CharField(max_length=32, choices=setting_kinds)
    text = models.CharField(max_length=128, null=True, blank=True)
    number = models.FloatField(null=True, blank=True)
    boolean = models.BooleanField()
    paragraph = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Chart(models.Model):
    name = models.CharField(max_length=128, help_text='Name of Billboard Chart')
    url = models.URLField(help_text='URL of Chart on Billboard.com')
    positions = models.IntegerField(help_text="Number of positions to fetch")

    def __str__(self):
        return self.name


class Log(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    release = models.CharField(max_length=128)
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.release} ({self.timestamp})"