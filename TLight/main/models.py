from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class DStatus(BaseModel):
    status_name = models.BooleanField(default=True)

    def __str__(self):
        return 'Активный' if self.status_name == 1 else 'Не активный'

    class Meta:
        db_table = 'd_status'
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class DType(BaseModel):
    type_name = models.CharField(max_length=50)

    def __str__(self):
        return self.type_name

    class Meta:
        db_table = 'd_type'
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


class DGender(BaseModel):
    gender = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.gender

    class Meta:
        db_table = 'd_gender'
        verbose_name = 'Пол'
        verbose_name_plural = 'Пол'


class TMail(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_mail'
        verbose_name = 'Почта'
        verbose_name_plural = 'Почты'


class TClient(BaseModel):
    id = models.CharField(primary_key=True, max_length=30, editable=False, blank=True)
    phone_number = models.CharField(max_length=15, unique=True)
    surname = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    id_status = models.ForeignKey(DStatus, on_delete=models.DO_NOTHING,
                               related_name='client_status')
    mail = models.ForeignKey(TMail, on_delete=models.CASCADE,
                             related_name='client_mails', blank=True, null=True)
    gender = models.ForeignKey(DGender, on_delete=models.DO_NOTHING,
                               related_name='client_gender', blank=True)
    time_zone = models.CharField(max_length=50)
    ok = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)
    telegram = models.CharField(max_length=50)
    whatsapp = models.CharField(max_length=50)
    viber = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        if not TClient.objects.count():
            self.id = '101'
        else:
            last_client_id = TClient.objects.aggregate(
                id_max=models.Max('id')
            )['id_max']
            id = str(int(last_client_id[:-2]) + 1) + '01'
            self.id = id
        super().save(*args, **kwargs)
        self.refresh_from_db()

    def __str__(self):
        return str(self.id) + ' - ' + self.surname + ' ' + self.first_name + ' ' + self.middle_name

    class Meta:
        db_table = 't_client'
        ordering = ('id',)
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class TPhone(BaseModel):
    phone_number = models.CharField(max_length=15)
    client_id = models.ForeignKey(TClient, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.phone_number

    class Meta:
        db_table = 't_phone'
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'


class TSocial(BaseModel):
    name = models.CharField(max_length=100)
    id_client = models.ForeignKey(TClient, on_delete=models.DO_NOTHING,
                                  related_name='client_socials')
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_social'
        verbose_name = 'Социальная сеть'
        verbose_name_plural = 'Соцниальные сети'


class TLegalEntity(BaseModel):
    id = models.IntegerField(primary_key=True, editable=False, blank=True)
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=20)
    inn = models.CharField(max_length=20)
    kpp = models.CharField(max_length=20)

    def save(self, *args, **kwargs):
        if not TLegalEntity.objects.count():
            self.id = 102
        else:
            last_legal_entity_id = TLegalEntity.objects.aggregate(
                id_max=models.Max('id')
            )['id_max']
            id = int(str(int(str(last_legal_entity_id)[:-2])+1) + '02')
            self.id = id
        super().save(*args, **kwargs)


    def __str__(self):
        return str(self.id) + ' - ' + self.name

    class Meta:
        db_table = 't_legal_entity'
        ordering = ('id',)
        verbose_name = 'Юр. Лицо'
        verbose_name_plural = 'Юр. Лица'



class TDepartment(BaseModel):
    id = models.IntegerField(primary_key=True, editable=False, blank=True)
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='child', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not TDepartment.objects.count():
            self.id = 103
        else:
            last_department_id = TDepartment.objects.aggregate(
                id_max=models.Max('id')
            )['id_max']
            id = int(str(int(str(last_department_id)[:-2]) + 1) + '03')
            self.id = id
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id) + ' - ' + self.name

    class Meta:
        db_table = 't_department'
        ordering = ('id',)
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департаменты'


class TLegalEntityDepartment(BaseModel):
    id_legal_entity = models.ForeignKey(TLegalEntity, on_delete=models.DO_NOTHING, related_name='legal_dept')
    id_department = models.ForeignKey(TDepartment, on_delete=models.DO_NOTHING, related_name='dept_legal')

    class Meta:
        db_table = 't_legal_entity_department'
        verbose_name = 'Legal Entity and Department'


class TClientDepartment(BaseModel):
    id_client = models.ForeignKey(TClient, on_delete=models.DO_NOTHING)
    id_department = models.ForeignKey(TDepartment, on_delete=models.DO_NOTHING, related_name='id_dept_cl')

    class Meta:
        db_table = 't_client_department'
        verbose_name = 'Client and Department'
