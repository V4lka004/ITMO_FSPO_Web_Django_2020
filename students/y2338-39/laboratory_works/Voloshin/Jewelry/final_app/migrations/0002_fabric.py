from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('final_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fabric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=300)),
                ('country', models.CharField(max_length=50)),
            ],
        ),
    ]
