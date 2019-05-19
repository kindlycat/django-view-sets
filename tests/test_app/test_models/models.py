from django.db import models


class OtherModel(models.Model):
    char_field = models.CharField(verbose_name='Char field', max_length=100)

    class Meta:
        verbose_name = 'other entry'
        verbose_name_plural = 'other entries'
        ordering = ['pk']

    def __str__(self):
        return self.char_field


class TestModel(models.Model):
    ONE = 1
    TWO = 2
    CHOICES = (
        (ONE, 'One'),
        (TWO, 'Two'),
    )

    char_field = models.CharField(
        verbose_name='Char field',
        max_length=100,
        help_text='Help text'
    )
    fk_field = models.ForeignKey(
        to=OtherModel,
        verbose_name='Fk field',
        related_name='test_entries_fk',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    choice_field = models.PositiveSmallIntegerField(
        verbose_name='Choice field',
        choices=CHOICES,
        default=ONE,
        blank=True,
        null=True
    )
    integer_field = models.IntegerField(
        verbose_name='Integer field',
        blank=True,
        null=True,
    )
    file_field = models.FileField(
        verbose_name='File field',
        upload_to='test_model',
        blank=True
    )
    image_field = models.ImageField(
        verbose_name='Image field',
        upload_to='test_model',
        blank=True
    )

    checkbox_field = models.BooleanField(
        verbose_name='Checkbox field',
        default=False,
        help_text='Help text'
    )

    class Meta:
        verbose_name = 'test entry'
        verbose_name_plural = 'test entries'
        ordering = ['pk']

    def __str__(self):
        return self.char_field


class InlineModel(models.Model):
    fk_field = models.ForeignKey(TestModel, verbose_name='TestModel', related_name='inlines', on_delete=models.CASCADE)
    char_field = models.CharField(verbose_name='Char field', max_length=100)
    checkbox_field = models.BooleanField(verbose_name='Checkbox field', default=False)
    position = models.IntegerField(verbose_name='Position', default=0)

    class Meta:
        verbose_name = 'inline entry'
        verbose_name_plural = 'inline entries'
        ordering = ['position', 'pk']

    def __str__(self):
        return self.char_field


class InlineModel2(models.Model):
    fk_field = models.ForeignKey(TestModel, verbose_name='TestModel', related_name='inlines2', on_delete=models.CASCADE)
    char_field = models.CharField(verbose_name='Char field', max_length=100)
    checkbox_field = models.BooleanField(verbose_name='Checkbox field', default=False)
    other = models.ForeignKey(
        OtherModel,
        verbose_name='OtherModel',
        related_name='inlines2',
        on_delete=models.PROTECT,
        null=True,
    )
    position = models.IntegerField(verbose_name='Position', default=0)

    class Meta:
        verbose_name = 'inline entry 2'
        verbose_name_plural = 'inline entries 2'
        ordering = ['position', 'pk']

    def __str__(self):
        return self.char_field
