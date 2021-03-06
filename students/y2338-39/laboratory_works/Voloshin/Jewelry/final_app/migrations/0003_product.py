from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('final_app', '0002_fabric'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('name', models.CharField(max_length=50)),
                ('vendor_code', models.CharField(max_length=50)),
                ('fabric', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='final_app.Fabric')),
            ],
        ),
    ]
