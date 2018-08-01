# Generated by Django 2.0.5 on 2018-08-01 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20180801_0725'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='playerstatus',
            name='status',
            field=models.CharField(choices=[('Attending', 'Attending'), ('Maybe', 'Maybe'), ('Passing', 'Passing'), ('Awaiting Response', 'Awaiting Response')], default='Awaiting Response', max_length=20),
        ),
        migrations.AddField(
            model_name='userevent',
            name='games',
            field=models.ManyToManyField(related_name='userevent', to='events.Game'),
        ),
    ]
