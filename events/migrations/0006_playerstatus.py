# Generated by Django 2.0.5 on 2018-08-01 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20180731_1648'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('AT', 'Attending'), ('MB', 'Maybe'), ('PA', 'Passing'), ('AW', 'Awaiting Response')], default='AW', max_length=2)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberstatus', to='events.UserEvent')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberstatus', to='events.Player')),
            ],
        ),
    ]
