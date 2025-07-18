from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('mrn', models.CharField(verbose_name='MRN', max_length=20, unique=True)),
                ('status', models.CharField(max_length=60)),
                ('last_session_date', models.DateField(blank=True, null=True)),
                ('notifications', models.IntegerField(default=0)),
                ('age', models.IntegerField()),
                ('provider', models.ForeignKey(
                    null=True,
                    on_delete=django.db.models.deletion.SET_NULL,
                    to='yourapp.Provider'
                )),
                ('diagnosis', models.ForeignKey(
                    null=True,
                    on_delete=django.db.models.deletion.SET_NULL,
                    to='yourapp.Diagnosis'
                )),
            ],
        ),
        migrations.CreateModel(
            name='PatientSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_date', models.DateField()),
                ('status', models.CharField(max_length=60)),
                ('patient', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='yourapp.Patient'
                )),
            ],
        ),
        migrations.CreateModel(
            name='SessionAlert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alert_type', models.CharField(max_length=50)),
                ('patient', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='yourapp.Patient'
                )),
            ],
        ),
        migrations.CreateModel(
            name='SessionAdherenceResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medication', models.CharField(max_length=50)),
                ('diet', models.CharField(max_length=50)),
                ('exercise', models.CharField(max_length=50)),
                ('session', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='yourapp.PatientSession'
                )),
            ],
        ),
    ]
