from django.db import models

# Create your models here.
KINDS = (
    ('KN', 'Khái niệm'),
    ('QT', 'Qui tắc'),
    ('TD', 'Tốc độ'),
    ('NV', 'Nghiệp vụ'),
    ('VH', 'Văn hóa'),
    ('KT', 'Kỹ thuật'),
    ('CT', 'Cấu tạo'),
    ('BB', 'Biển báo'),
    ('SH', 'Sa hình'),
)

class exam(models.Model):
    name = models.CharField(max_length=255)
    exam_times = models.IntegerField(default=20)
    question_number = models.IntegerField(default=20)
    question_correct = models.IntegerField(default=16)

    def __str__(self):
        return self.name


class QuestionType(models.Model):
    kinds = models.CharField(max_length=2, choices=KINDS)
    number = models.IntegerField()
    exam_type = models.ForeignKey(exam, on_delete=models.CASCADE)

    def __str__(self):
        name = self.kinds + self.exam_type.name
        return name

class Question(models.Model):
    content = models.CharField(max_length=255)
    pic = models.ImageField(upload_to='question', blank=True, null=True)
    kind = models.CharField(max_length=2, choices=KINDS)

    def __str__(self):
        num = self.id
        string = 'Câu ' + str(num)
        return string

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    correct = models.BooleanField(default=False)

    def __str__(self):
        num = self.id
        string = 'Đáp án ' + str(num)
        return string
